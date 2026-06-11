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
