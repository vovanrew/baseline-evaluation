# Design: named-graph extraction in DiagramStatsExtractor

Date: 2026-06-08
Subtask: Phase 1 "A" — extend the custom PlantUML parser to emit a named graph.
Status: approved, pre-implementation.

## Motivation

CSR (metric #1) is done. The next metrics — Element F1 (#2) and Relationship F1
(#3) — require **name-matched** comparison of predicted vs ground-truth diagrams:
match classes/participants by visible name, match relationships by typed
endpoints. The custom parser (`DiagramStatsExtractor`, the DiagramStatsExtractor
fork of PlantUML) currently emits **counts by type only** — no entity names, no
edge endpoints — so it cannot feed those metrics. This subtask extends it to emit
a typed graph. It gates B (Element F1) and C (Relationship F1); both consume the
graph for GT and predictions alike.

## Location & build

- Fork: `/Users/vovapolischuk/indiehacker/projects/university/dataset/plantuml`.
- New branch off `stats-extractor-compat`.
- File: `src/main/java/net/sourceforge/plantuml/stats/DiagramStatsExtractor.java`.
- Rebuild: `./gradlew build -x test -x javadoc` → `build/libs/plantuml-1.2025.9.jar`.
- All required getters are already public upstream (`Entity.getName/getDisplay/
  getLeafType`, `Link.getEntity1/2/getType/getLabel`, `Participant.getCode/
  getDisplay/getType`, `AbstractMessage.getParticipant1/2/getLabel`). **No new
  getters needed** — the change is confined to `DiagramStatsExtractor`.

## Output: additive

The existing per-block JSON (one object per line, stdout) is preserved. The
`elements` / `elements_total` / `connections` / `connections_total` count fields
stay (the corpus pipeline depends on them). Two arrays are **added**: `nodes` and
`edges`. No existing field changes meaning.

## Node identity = visible display name

The task is image -> code: a model can only reproduce what is *visible in the
rendered image*, never an invisible alias. So node identity is the **display
name**, not the alias/code. Example: `class "ApplicationTemplate" as Model`
yields node key `ApplicationTemplate` (not `Model`). Edge endpoints reference
nodes by this same display string, so Element F1 and Relationship F1 join on one
consistent key. Raw casing and whitespace are preserved in the JSON; the Python
metrics lowercase + strip at match time.

`Display` objects are flattened to their plain visible text (lines joined).

## Schema (uniform across class & sequence)

```json
{
  "file": "<id>",
  "diagram_type": "class",
  "elements": { "class": 2 },
  "elements_total": 2,
  "connections": { "arrow": 1 },
  "connections_total": 1,
  "nodes": [
    { "name": "ApplicationTemplate", "type": "class" }
  ],
  "edges": [
    { "source": "ApplicationTemplate", "target": "Application",
      "relation": "dependency", "label": "app" }
  ],
  "error": null
}
```

### Nodes
- **Class diagrams:** one node per *leaf entity* (class / interface / enum /
  abstract / ...). `type` = the PlantUML leaf type, lowercased.
- **Sequence diagrams:** one node per participant. `type` = participant type
  (actor / participant / boundary / ...), lowercased.
- Packages / namespaces / other groups are **containers**, excluded from `nodes`
  (they remain counted in the `elements` field). Element F1 scope is
  classes/participants only.
- `name` = flattened display name. No members (fields/methods) in v1 — deferred,
  not used by any current metric.

### Edges
- Uniform shape `{source, target, relation, label}`. `source`/`target` are node
  display names. `label` = flattened edge/message label (empty string if none).
- **Relation canonicalization happens in Java** (the PlantUML-aware layer), so
  the schema is identical for both types and the Python F1 code only compares
  strings.
- Class `relation` is mapped from link decoration + line style to one of:
  - `inheritance` — extends / triangle head.
  - `composition` — filled diamond.
  - `aggregation` — hollow diamond.
  - `dependency` — dashed line carrying an arrow head (e.g. `..>`).
  - `association` — solid line, none of the above (with or without a plain arrow).
- **Sequence:** every message edge has `relation: "message"`.

## Deferred (explicit YAGNI cuts)

- Class members (attributes / methods) on nodes — no current metric uses them.
- Multiplicities / qualifiers on edges.
- Arrow sub-kinds for sequence (sync / async / return) — Relationship F1 treats
  sequence relations as a single `message` type per CLAUDE.md.

## Smoke test

Run the rebuilt JAR on the 4 smoke predictions
(`data/smoke_runs/Qwen_Qwen3.5-2B_20260607T181823Z/*.puml`) and their GT
(`data/puml_files/<key>.puml`). Eyeball that `nodes`, `edges`, and `relation`
values match the diagrams by hand, specifically covering:
- a class diagram with inheritance + an association/composition,
- a sequence diagram with messages,
- the known `..>` dependency case (a sequence prediction that used
  class-diagram dependency syntax — confirm `relation` classification is honest).

## Downstream (out of scope here, recorded for context)

- B (Element F1): match `nodes` by lowercased+stripped `name`.
- C (Relationship F1): match `edges` by (source, target, relation), stratified by
  `relation`.
