#!/usr/bin/env python3
"""Assemble a per-key review index for the audit-50 manual validation pass.

Joins CSR, Element F1, Relationship F1 and chrF++ results against the audit-50
test set, then writes a JSON record and a Markdown table to smoke_tests/audit50/.
Triage flags surface the cases that are most worth inspecting:

  ANOMALY_LOW_F1_COMPILED       — compiled but element or relationship F1 < 0.5
                                  with non-trivial GT support (≥3 nodes/edges)
  ANOMALY_HIGH_CHRF_NON_COMPILED — non-compiled but chrF++ ≥ 50
  ANOMALY_RELATIONSHIP_DEGENERATE — compiled, GT has edges, prediction has none
"""
from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict


def load_results(path):
    r = json.load(open(path))
    return {d["key"]: d for d in r["diagrams"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit-test-set", default="smoke_tests/audit50/test_set.json")
    ap.add_argument("--csr",   default="smoke_tests/csr/audit50/csr_results.json")
    ap.add_argument("--elem",  default="smoke_tests/element_f1/audit50/element_f1_results.json")
    ap.add_argument("--rel",   default="smoke_tests/relationship_f1/audit50/relationship_f1_results.json")
    ap.add_argument("--chrf",  default="smoke_tests/chrf/audit50/chrf_results.json")
    ap.add_argument("--pred-dir", required=True,
                    help="raw prediction dir, e.g. smoke_tests/smoke_runs/Qwen_Qwen3.5-2B_<stamp>")
    ap.add_argument("--out-dir", default="smoke_tests/audit50")
    args = ap.parse_args()

    ts = json.load(open(args.audit_test_set))
    diagrams = ts["diagrams"]
    csr   = load_results(args.csr)
    elem  = load_results(args.elem)
    rel   = load_results(args.rel)
    chrf  = load_results(args.chrf)

    rows = []
    for d in diagrams:
        key = d["key"]
        stem = key[:-5]
        c = csr.get(stem, {})
        e = elem.get(stem, {})
        r = rel.get(stem, {})
        f = chrf.get(stem, {})

        compiled = bool(c.get("compiled"))
        e_f1 = e.get("f1")
        r_f1 = r.get("f1")
        chrf_score = f.get("score")

        # GT-support proxies: count true positives + false negatives.
        e_gt_support = int(e.get("tp", 0)) + int(e.get("fn", 0))
        r_gt_support = int(r.get("tp", 0)) + int(r.get("fn", 0))
        r_pred_support = int(r.get("tp", 0)) + int(r.get("fp", 0))

        flags = []
        if compiled and e_f1 is not None and e_f1 < 0.5 and e_gt_support >= 3:
            flags.append("ANOMALY_LOW_F1_COMPILED:element")
        if compiled and r_f1 is not None and r_f1 < 0.5 and r_gt_support >= 3:
            flags.append("ANOMALY_LOW_F1_COMPILED:relationship")
        if not compiled and chrf_score is not None and chrf_score >= 50:
            flags.append("ANOMALY_HIGH_CHRF_NON_COMPILED")
        if compiled and r_gt_support >= 3 and r_pred_support == 0:
            flags.append("ANOMALY_RELATIONSHIP_DEGENERATE")

        rows.append({
            "key": key,
            "stem": stem,
            "type": d["primary_type"],
            "tier": d["tier"],
            "repository": d["repository"],
            "elements_total": d.get("elements_total"),
            "content_lines": d.get("content_lines"),
            "compiled": compiled,
            "element": {
                "tp": e.get("tp"), "fp": e.get("fp"), "fn": e.get("fn"),
                "precision": e.get("precision"), "recall": e.get("recall"),
                "f1": e_f1,
            },
            "relationship": {
                "tp": r.get("tp"), "fp": r.get("fp"), "fn": r.get("fn"),
                "precision": r.get("precision"), "recall": r.get("recall"),
                "f1": r_f1,
            },
            "chrf": chrf_score,
            "flags": flags,
            "paths": {
                "image":     f"data/puml_images_1568/{stem}.png",
                "gt":        f"data/puml_files/{stem}.puml",
                "pred_raw":  os.path.join(args.pred_dir, stem + ".puml"),
                "pred_iso":  f"smoke_tests/csr/audit50/extracted/{stem}.puml",
                "pred_png":  f"smoke_tests/csr/audit50/png/{stem}.png",
            },
        })

    os.makedirs(args.out_dir, exist_ok=True)
    json_path = os.path.join(args.out_dir, "review_index.json")
    with open(json_path, "w") as f:
        json.dump({"summary": {
            "n": len(rows),
            "compiled": sum(1 for x in rows if x["compiled"]),
            "with_flags": sum(1 for x in rows if x["flags"]),
            "by_flag": dict_count_flags(rows),
        }, "rows": rows}, f, indent=2)
    print(f"wrote {json_path}")

    md_path = os.path.join(args.out_dir, "review_index.md")
    with open(md_path, "w") as f:
        write_markdown(f, rows, args.pred_dir)
    print(f"wrote {md_path}")


def dict_count_flags(rows):
    c = defaultdict(int)
    for row in rows:
        for flag in row["flags"]:
            c[flag] += 1
    return dict(c)


def fmt(v, prec=2):
    if v is None: return "—"
    if isinstance(v, float): return f"{v:.{prec}f}"
    return str(v)


def write_markdown(f, rows, pred_dir):
    n = len(rows)
    n_compiled = sum(1 for x in rows if x["compiled"])
    n_flagged = sum(1 for x in rows if x["flags"])
    fc = dict_count_flags(rows)
    f.write(f"# Audit-50 review index\n\n")
    f.write(f"- n = {n}\n- compiled = {n_compiled}\n- with_flags = {n_flagged}\n")
    for fl, ct in sorted(fc.items()):
        f.write(f"  - {fl}: {ct}\n")
    f.write(f"\nPrediction dir: `{pred_dir}`\n\n")
    f.write("## Triage table\n\n")
    f.write("| key | cell | el | nl | comp | E-F1 | R-F1 | chrF++ | flags |\n")
    f.write("|-----|------|----|----|------|------|------|--------|-------|\n")
    for x in rows:
        flagshort = ", ".join(s.replace("ANOMALY_", "") for s in x["flags"])
        f.write(
            f"| {x['stem'][:12]} | {x['type'][:3]} T{x['tier']} "
            f"| {fmt(x['elements_total'])} | {fmt(x['content_lines'])} "
            f"| {'Y' if x['compiled'] else 'N'} "
            f"| {fmt(x['element']['f1'])} | {fmt(x['relationship']['f1'])} "
            f"| {fmt(x['chrf'], 1)} | {flagshort} |\n"
        )
    f.write("\n## Per-key files (image / GT / pred)\n\n")
    for x in rows:
        f.write(f"### `{x['stem']}` — {x['type']} T{x['tier']} "
                f"(repo: `{x['repository']}`)\n\n")
        e = x["element"]; r = x["relationship"]
        f.write(f"- CSR: **{'PASS' if x['compiled'] else 'FAIL'}**\n")
        f.write(f"- Element F1: tp={e['tp']} fp={e['fp']} fn={e['fn']} "
                f"P={fmt(e['precision'])} R={fmt(e['recall'])} F1={fmt(e['f1'])}\n")
        f.write(f"- Relationship F1: tp={r['tp']} fp={r['fp']} fn={r['fn']} "
                f"P={fmt(r['precision'])} R={fmt(r['recall'])} F1={fmt(r['f1'])}\n")
        f.write(f"- chrF++: {fmt(x['chrf'], 2)}\n")
        f.write(f"- image: `{x['paths']['image']}`\n")
        f.write(f"- GT:    `{x['paths']['gt']}`\n")
        f.write(f"- pred:  `{x['paths']['pred_raw']}`\n")
        f.write(f"- iso:   `{x['paths']['pred_iso']}`\n")
        if x['flags']:
            f.write(f"- flags: {', '.join(x['flags'])}\n")
        f.write("\n")


if __name__ == "__main__":
    main()
