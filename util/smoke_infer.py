#!/usr/bin/env python3
"""End-to-end inference smoke test (PLAN Phase 0).

Sends a handful of real, standardized test-set diagrams to one hosted model with
the zero-shot image->PlantUML prompt, validates that the image was actually
ingested (prompt_tokens > text-only baseline), and stores every raw response
untouched. Confirms the path returns code at acceptable cost/latency before
scaling.

Usage (invoke from project root):
  FEATHERLESS_API_KEY=$(cat API-KEY.txt) python util/smoke_infer.py
  (override --model / --n / --base-url for other OpenAI-compatible providers)
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import signal
import ssl
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

try:
    import certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    _SSL_CTX = ssl.create_default_context()

PROMPT = (
    "This image is a UML diagram. Reproduce it as valid PlantUML code that, when "
    "rendered, matches the diagram as closely as possible: capture every element, "
    "its members, and every relationship. Output only the PlantUML code starting "
    "with @startuml and ending with @enduml, with no explanation."
)


def image_data_url(path):
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{b64}"


def call(base_url, key, model, content, max_tokens, timeout):
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "max_tokens": max_tokens,
        "temperature": 0,
    }).encode()
    req = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/124.0 Safari/537.36",
        },
    )
    # Hard wall-clock deadline: urllib's socket timeout only trips on byte-level
    # inactivity, so a server that trickles bytes can hang forever. SIGALRM fires
    # regardless. (Main thread only; fine for this single-threaded smoke.)
    def _on_alarm(signum, frame):
        raise TimeoutError(f"hard deadline {timeout}s")
    old = signal.signal(signal.SIGALRM, _on_alarm)
    signal.alarm(timeout)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
            return json.loads(resp.read()), time.time() - t0
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        raise SystemExit(f"HTTP {e.code} {e.reason}\nresponse body:\n{detail}")
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


def pick(diagrams, n):
    """Deterministic spread across types/tiers: stride through the frozen list."""
    step = max(1, len(diagrams) // n)
    return [diagrams[i * step] for i in range(n)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default="https://api.featherless.ai/v1")
    ap.add_argument("--model", default="Qwen/Qwen3.5-2B")
    ap.add_argument("--test-set", default="data/test_set.json")
    ap.add_argument("--images", default="data/puml_images_1568")
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--keys", default="", help="comma-separated blob_id prefixes to target instead of the spread; repeats each --repeat times")
    ap.add_argument("--repeat", type=int, default=1, help="send each selected diagram this many times (cold-start/stall test)")
    ap.add_argument("--max-tokens", type=int, default=2048)
    ap.add_argument("--timeout", type=int, default=10, help="per-call seconds (smoke default; raise for the real run, see note below)")
    ap.add_argument("--out", default="data/smoke_runs")
    args = ap.parse_args()

    key = os.environ.get("FEATHERLESS_API_KEY")
    if not key:
        raise SystemExit("set FEATHERLESS_API_KEY (e.g. FEATHERLESS_API_KEY=$(cat API-KEY.txt))")

    all_diagrams = json.load(open(args.test_set))["diagrams"]
    if args.keys:
        wanted = [k.strip() for k in args.keys.split(",") if k.strip()]
        selected = [r for r in all_diagrams
                    if any(r["blob_id"].startswith(w) for w in wanted)]
    else:
        selected = pick(all_diagrams, args.n)
    diagrams = [r for r in selected for _ in range(args.repeat)]

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(args.out, f"{args.model.replace('/', '_')}_{stamp}")
    os.makedirs(run_dir, exist_ok=True)

    # Text-only baseline: prompt_tokens for an image-bearing call must exceed this.
    base_resp, _ = call(args.base_url, key, args.model,
                        [{"type": "text", "text": PROMPT}], max_tokens=1,
                        timeout=args.timeout)
    baseline = base_resp["usage"]["prompt_tokens"]
    print(f"model={args.model}")
    print(f"text-only baseline prompt_tokens = {baseline}")
    print(f"run dir = {run_dir}", flush=True)

    for attempt, r in enumerate(diagrams):
        base = r["key"][:-5]
        stem = f"{base}_a{attempt}" if args.repeat > 1 else base
        print(f"\n-> {base[:18]} ({r['primary_type']} T{r['tier']}, "
              f"{r['image_width']}x{r['image_height']}) sending...", flush=True)
        img = image_data_url(os.path.join(args.images, base + ".png"))
        try:
            resp, secs = call(args.base_url, key, args.model,
                              [{"type": "text", "text": PROMPT},
                               {"type": "image_url", "image_url": {"url": img}}],
                              max_tokens=args.max_tokens, timeout=args.timeout)
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"   FAIL after ~{args.timeout}s: {e}", flush=True)
            continue
        # Persist the raw response verbatim before touching it.
        with open(os.path.join(run_dir, stem + ".json"), "w") as f:
            json.dump(resp, f, indent=2)

        usage = resp.get("usage", {})
        ptok = usage.get("prompt_tokens", 0)
        ctok = usage.get("completion_tokens", 0)
        code = resp["choices"][0]["message"]["content"] or ""
        with open(os.path.join(run_dir, stem + ".puml"), "w") as f:
            f.write(code)

        ingested = "OK" if ptok > baseline else "DROP!"
        print(f"   ptok={ptok} ingest={ingested} ctok={ctok} {secs:.1f}s "
              f"@startuml={'@startuml' in code} @enduml={'@enduml' in code}",
              flush=True)

    print(f"\nraw responses + extracted .puml in {run_dir}")
    print("ingest must read OK for every row (DROP! = image not encoded; retry/warm up).")


if __name__ == "__main__":
    main()
