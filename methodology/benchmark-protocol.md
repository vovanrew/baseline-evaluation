# Benchmark Protocol

Methodological record for the zero-shot benchmark runs: the inference-side
protocol applied identically to every model. Metric definitions are recorded in
`evaluation-framework.md`; test-set construction in `test-set-construction.md`.

## 1. Prompt

Every model receives a single zero-shot prompt, identical across models and
diagram types, frozen verbatim at `prompts/zero_shot.txt` and read from that
file by the inference harness:

> This image is a UML diagram. Reproduce it as valid PlantUML code that, when
> rendered, matches the diagram as closely as possible: capture every element
> with the UML notation shown (e.g. actor, interface, database), its contents
> and labels, and every relationship. Output only the PlantUML code starting
> with @startuml and ending with @enduml, with no explanation.

The prompt identifies the input only as "a UML diagram", without naming the
diagram type, so recognizing the diagram kind is part of the measured task.
Its instruction enumerates the dimensions the evaluation scores: element
recovery with the rendered UML notation preserved (Element F1 and its
type-accuracy companion), element contents and labels (chrF++), and
relationship recovery (Relationship F1). The output constraint — a bare
PlantUML block from `@startuml` to `@enduml` with no surrounding explanation —
matches the block-isolation step applied to every prediction before scoring.
The prompt contains no PlantUML syntax guidance, no examples, and no
model-specific phrasing.

The frozen text is pinned by `tests/test_prompt.py`, which asserts the file
content verbatim together with the properties above (single line, no diagram-
type hint, output-block constraint); any re-freeze updates the file, the test,
and this record together.

## 2. Inference protocol

Inference runs through `evaluation/infer_runner.py` (greedy decoding,
temperature 0; `max_tokens` 5376 per methodology §1 of the evaluation
framework; a 90-second per-call hard wall-clock deadline sized to the worst
legitimate generation at observed throughput). Each run stores one record per
test-set cell and a `run_meta.json` pinning the model identifier, endpoint,
prompt text, and decoding parameters.

Image ingestion is validated on every call: the response's `prompt_tokens`
must exceed a text-only baseline measured at run start, since a hosted
endpoint can accept an image-bearing request yet silently drop the image and
answer from the text alone (observed on Featherless cold starts). Before the
batch, throwaway image-bearing calls warm the endpoint until ingestion is
confirmed; the run aborts if it never is. During the batch, a call whose
image is dropped is retried a bounded number of times; a persistent drop is
recorded as an `image_dropped` failure and its blind completion is excluded
from scoring.

Transient transport failures (HTTP 408, 429, and 5xx; network-level errors)
are retried with exponential backoff. A call that exceeds the hard deadline is
recorded as a `timeout` failure without retry, because observed timeout causes
(no-EOS repetition spirals) reproduce deterministically. Every failed cell —
`timeout`, `image_dropped`, `http_error`, or `network_error` — yields a stored
failure record and no prediction file, so Compilation Success Rate scores the
cell as a failure while the cause remains on disk for error analysis. Stored
successful responses are immutable: re-invoking a run directory skips them and
re-attempts only recorded failures.

## 3. Reasoning configuration

Every model runs at its minimum available reasoning configuration, fixed per
model from provider documentation (verified 2026-06-11) and recorded in each
run's `run_meta.json`:

| Model | Setting | Reasoning state |
|---|---|---|
| `gpt-5.2-2025-12-11` | `reasoning_effort: "none"` | off (also the model default; "does not perform reasoning") |
| `claude-sonnet-4-6` | `thinking: {"type": "disabled"}` | off |
| `gemini-3.1-pro-preview` | `thinking_level: "low"` | minimum available — thinking cannot be disabled on the Pro tier (`minimal` is unsupported there); `low` is the floor, below the dynamic `high` default |
| Qwen3.5-2B / 9B / 27B | `chat_template_kwargs: {"enable_thinking": false}` | off |

Qwen3.5 is a hybrid thinking family whose default differs by size: 2B
defaults to non-thinking while 9B and 27B default to thinking, so the
non-thinking flag is sent explicitly and uniformly to all three sizes
(the 2B chat template enables thinking only on an explicit `true`, so the
uniform flag is a no-op there). The flag follows the official model-card
usage; Featherless passes `chat_template_kwargs` through as a documented
request-body field. Non-thinking is realized in the chat template as an empty
`<think>\n\n</think>` block prefilled into the prompt, so the completion
itself contains no reasoning content.

The Gemini setting is an asymmetry of the comparison rather than a silent
confound: thinking tokens generated at `thinking_level: "low"` are billed and
reported by the API in the per-response `thoughtsTokenCount` field, which is
preserved in the stored raw responses; the benchmark reports the measured
residual thinking-token volume alongside the results. As of 2026-06-11
Gemini 3.1 Pro exists only as the preview id `gemini-3.1-pro-preview` with no
dated snapshot, so the literal id and the run date are recorded together.

The harness passes the per-model configuration verbatim into every request
body (`--extra-body`, stored in `run_meta.json`) and checks each completion
for inline reasoning content: a `<think>` block in a stored completion is
counted and reported as a `reasoning_leak` in the run tally, because block
isolation would otherwise strip leaked reasoning before scoring and a
wrongly-enabled thinking mode would be invisible downstream. The per-family
pilot run (10 samples) must show zero leaked completions and, for GPT-5.2,
zero `reasoning_tokens` in the reported usage before a full run is launched.
