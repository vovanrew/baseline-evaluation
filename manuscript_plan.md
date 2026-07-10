# Manuscript plan — structure of the LNTU article

> Planning artifact, not the paper. Each bullet is a *thing to include* — a topic, never content,
> numbers, or wording. Later sessions pick one leaf at a time and draft it into `manuscript.md`,
> pulling actual content from the source pointed to in *(→ …)*. Sections map 1:1 to the six
> mandatory LNTU structural elements; front matter and references bracket them. Page budget is
> 5–10 pages nominal, and **exceeding 10 is permitted** (author-confirmed) — so the **Exhibit
> budget** and **condense-flags** below are readability guidance, not a hard cap: prefer selection,
> but do not cut load-bearing material to fit a page count.

---

## 0. Front matter (required by the journal, not a structural element)

- UDC (УДК) code — author to assign
- Header metadata: author name, degree/title, ORCID, organization
- Title (English; Ukrainian rendering is the author's later translation step)
- **Two abstracts** (~200 words each), each headed by surname+initials + title, each with 5–10
  keywords: EN drafted by assistant; UA is the author's translation step
  - Abstract content slots: task in one sentence; data/benchmark in one; framework in one;
    panel in one; headline finding + population-gap finding in one–two; novelty in one
  - Draft LAST, after the body is stable (only summarizes — no fact appears here first)
- Keyword list slots: task keywords, method keywords, model-family keywords

## 1. Problem statement + link to important scientific/practical tasks (element 1)

- UML diagrams in real projects survive as rendered images while source is lost — the
  recover-source-from-image task and who needs it (documentation recovery, reverse engineering,
  model-driven maintenance) *(→ framing; CLAUDE.md one-liner)*
- Multimodal LLMs as the newly plausible instrument for this task; zero-shot capability unknown
- The measurement problem as the core problem: no accepted way to score image→PlantUML output
  (what counts as "recovered"? what about output that doesn't render?)
- Practical stakes of mismeasurement: model selection and fine-tuning decisions made on
  biased metrics *(forward hook to the population-gap contribution — named, not stated)*
- One-sentence bridge to the goal (element 4)

## 2. Analysis of recent research and publications (element 2)

Target ~12–20 references total for the paper; this section carries most of them.

- Image-to-UML-code with multimodal LLMs — the three anchors, each in 1–3 sentences:
  - Conrardy & Cabot: earlier-generation VLMs, manual error counting, small scale *(→ CLAUDE.md prior-work)*
  - Bates et al.: fine-tuned LLaVA, BLEU+SSIM scoring — differentiate: pixel/surface metrics vs
    our structural ones *(→ CLAUDE.md prior-work)*
  - Ranjani & Prabhudesai: component-level metrics for sequence diagrams — differentiate: overlap
    with our metric contribution, narrower scope *(→ CLAUDE.md prior-work)*
- Adjacent literatures, one compact paragraph each (select, don't survey):
  - text-to-UML / diagram generation with LLMs
  - multimodal-LLM benchmark/evaluation practice (incl. chart/diagram understanding)
  - structural diagram similarity / model comparison approaches
- Instrument citations woven in where first relevant (not a separate list): World of Code
  (**mandatory**), PlantUML, chrF++ (Popović), sacrebleu (Post), paired bootstrap (Koehn),
  model reports for the panel *(→ CLAUDE.md "still to gather")*
- Synthesis sentence: common limitations of prior work (small/synthetic data, manual or
  surface-level scoring, no compile-gating, selection bias untreated) — sets up element 3

## 3. Previously unsolved part of the general problem (element 3)

Short section (one paragraph-block); each bullet = one gap, phrased as missing-in-prior-work:

- No large, real-world (in-the-wild) benchmark for image→PlantUML
- No unified multi-level evaluation framework (compilation → elements → relations → types → surface)
- Selective-failure bias of compiled-only scoring never identified or quantified
- No zero-shot capability characterization of an open model family (scaling behaviour) on this task
- Explicit statement that these four gaps are what this article addresses

## 4. Research goal and task statement (element 4)

- Goal in one sentence (measure zero-shot image→PlantUML reconstruction with an unbiased
  multi-level framework on a real-world benchmark)
- Enumerated tasks (numbered list, each maps to a Main-Material subsection):
  benchmark construction; evaluation framework definition; two-arm panel benchmark run;
  quantification of selective-failure bias; qualitative failure analysis
- Scope declaration: class + sequence diagrams (two of the nine corpus types); zero-shot only

## 5. Main material (element 5) — expanded one level deeper

> LNTU requires "presentation of the main material with full justification of results".
> Sub-structure below: Methods (5.1–5.3) → Results (5.4–5.6) → Error analysis (5.7) →
> Discussion & limitations (5.8). Working titles are drafting labels; final headings set at assembly.

### 5.1 Benchmark dataset *(→ methodology/test-set-construction.md)*

- Corpus origin: WoC-mined PlantUML↔PNG pairs from open-source repositories; corpus scale
- Scope restriction to class + sequence; type-agreement filter (corpus label vs parser)
- Selection pipeline in brief: inclusion criteria, degenerate-render exclusion,
  normalized-code deduplication — **condense-flag: one compact paragraph, not the full pipeline**
- Stratified design: type × complexity-tier × cell size; tiering variable (source-line quartiles)
  and its visual-complexity monotonicity rationale
- Repository-disjoint sampling + per-repository cap (and its role for future fine-tuning)
- Image standardization: single resize standard, identical image to every model
  (controlled-comparison rationale, stated at model level only)
- Label-quality manual validation (type / element agreement rates) *(→ CLAUDE.md data facts)*
- Published reproducibility artifact: filename-key list, fixed seed

### 5.2 Evaluation framework *(→ methodology/evaluation-framework.md)*

- Typed-graph extraction: parser-based extractor applied identically to ground truth and
  prediction; node/edge definitions in brief
- The metric suite, in priority order, one definition each (definitions live HERE, nowhere else):
  - CSR — render-gated compilation success; precondition role; how truncation/absence count
  - Element F1 — display-name match key; rationale for name-only keying (stereotypes stripped)
  - Relationship F1 — (source, target, relation-type) key; the six-relation vocabulary;
    direction rules; label/multiplicity excluded
  - Type accuracy — companion metric over name-matched pairs
  - chrF++ — surface catch-all; what it covers that structural metrics ignore
- The two reporting populations (honest all-N vs compiled-only) — **definition** and notation here;
  the *finding* about their divergence belongs to 5.5 only
- Micro vs macro aggregation, one sentence each
- Statistical procedure: paired bootstrap CIs; paired-difference reading rule
  *(→ methodology/analysis-protocol.md)*

### 5.3 Experimental setup: models and protocol *(→ methodology/benchmark-protocol.md)*

- Two-arm panel design and its rationale (reference points vs study object, not one leaderboard):
  - Arm A: one flagship per lab, fixed upper-bound reference points
  - Arm B: Qwen dense ladder as a scaling curve + MoE as a separate capability ceiling
    (total vs active parameters distinction; not a fourth dense rung)
- Single frozen zero-shot prompt; no diagram-type hint (type recognition is part of the task);
  output-block constraint
- Reasoning configuration: minimum/non-thinking for all; the Gemini floor asymmetry and its
  mitigant (measured zero thinking tokens) — one–two sentences
- Decoding and caps: greedy, token-ceiling sizing rationale; failure handling stated at model
  level only (no provider/API detail)
- Reproducibility provenance: exact snapshots, seeds, committed predictions, public repo
  *(→ exhibits.md Exhibit 7; cite repo as open release)*

### 5.4 Results: compilation and structure recovery *(→ exhibits.md Ex. 1–2; results_explained.md §2–4)*

- Headline two-arm table (selected columns; CIs) — **the** results table [Table slot]
- Frontier reading: near-saturated compilation; which model leads and that the lead is
  CI-separated; relationship recovery as the discriminating metric [Figure slot: frontier bars]
- Dense-ladder reading: monotonic scaling on every metric; the "scale buys compiling at all,
  not per-diagram polish" observation [Figure slot: scaling curve]
- MoE ceiling reading: position relative to ladder and frontier band; reported off the dense axis
- Token-footprint note: inverse size↔output-volume relation as the runaway-generation signal —
  **condense-flag: two–three sentences, no table; forward hook to 5.7 runaway category**
  *(→ exhibits.md Ex. 7; results_explained.md §8)*

### 5.5 The population gap: selective-failure bias *(→ exhibits.md Ex. 3; results_explained.md §5)*

The central methodological finding — gets its own subsection despite its small size.

- Gap magnitudes across the panel (table or in-prose; the only place these numbers appear)
  [Table slot: gap table — **condense-flag: may merge into 5.4's headline table as a Δ column**]
- The mechanism: weak models compile only the easy subset → compiled-only grades a self-selected
  population
- The gap-tracks-CSR relation (near-zero at frontier, large at weak rungs)
- The methodological rule this licenses: honest all-N as the only fair headline; compiled-only
  readable only next to CSR — phrased as guidance for future benchmark reporting

### 5.6 Difficulty structure: relations, complexity, diagram type *(→ exhibits.md Ex. 4–6; results_explained.md §6–7)*

- Per-relation difficulty ordering: frequent/simple relations easy; the rare decorated relations
  (composition/aggregation/dependency) hard for every model; support imbalance noted
  [Figure slot: per-relation F1]
- Per-tier degradation: panel-wide decline; frontier near-flat vs weak-rung collapse
  [Figure slot: per-tier breakdown]
- Image-crowding descriptor as the legibility context for the tier curve (definition + reading)
- Class vs sequence asymmetry: general class advantage; the model-specific sequence exceptions
  worth flagging for fine-tuning — **condense-flag: one short paragraph, no per-type tables**

### 5.7 Qualitative error analysis *(→ analysis/error_analysis.md)*

- Method in brief: stratified failure index → verified case sample spanning models, types,
  tiers, outcome classes — **condense-flag: two–three sentences on method, not the sampling spec**
- Failure taxonomy: grouped category families (reliability / generation-compilation /
  structural-semantic / measurement) [Table slot: compact taxonomy table — categories × metric hit]
- Key mechanisms, one short paragraph each (select the load-bearing ones):
  - frontier vs open-arm contrast: rare near-miss (single-token) failures vs gross generative
    failures — the case-level explanation of the population gap (back-reference to 5.5)
  - runaway/truncation loops (back-reference to token footprint in 5.4)
  - diagram-family confusion as the sequence-collapse mechanism
  - relation-type substitution as the mechanism behind 5.6's hard-relations result
  - measurement/normalization artifacts inflating the frontier's residual gap — honest
    instrument-limitation finding
- At most one–two concrete case vignettes total — **condense-flag: page budget; cases cited by
  category, not walked through**

### 5.8 Discussion and limitations

- What the results mean for practice: choosing a model for diagram reconstruction; what the
  open-arm profile implies for fine-tuning feasibility (brief — details are future work, element 6)
- Interpretation caveat: part of the frontier's residual structural deficit is measurement, not
  comprehension (from 5.7) — implication for reading the absolute scores
- Metric-brittleness note (zero-edge ground truths) — one sentence *(→ error_analysis.md §4.4)*
- Limitations, one sentence each, each with its defense *(→ CLAUDE.md limitations list)*:
  class+sequence only; zero-shot only; single frozen prompt; non-thinking only (Gemini mitigant);
  structural+surface metrics only (vs visual/SSIM — differentiate from Bates); MoE ceiling not
  backend-matched to the dense ladder

## 6. Conclusions (closes element 5 — must state naukova novyzna explicitly)

- Explicit scientific-novelty statement, enumerated (the three contributions, in this order):
  first large real-world WoC-sourced image-to-PlantUML benchmark; unified multi-level structural
  evaluation framework; identification + quantification of selective-failure bias
  *(→ CLAUDE.md contribution list — lead with these, not the ranking)*
- Compressed answer to each enumerated task from element 4 (one sentence each; reference back to
  5.4–5.7, no numbers restated beyond at most the single headline figure)
- Practical significance sentence (who can use the benchmark/framework/release)

## 7. Prospects for further research (element 6)

- Fine-tuning the open family on the corpus — the failure-taxonomy → training-mix mapping in one
  compact list *(→ error_analysis.md §5, heavily condensed)*
- Extending scope: remaining diagram types; thinking-mode comparison; prompt ablation
- Instrument refinement: name-normalization gaps, notes-as-nodes accounting *(→ error_analysis.md §3.10)*
- Complementary metric axes (visual/graph-edit/LLM-judge) as open evaluation questions

## 8. References

- Dual-format block per DSTU 8302:2015: Ukrainian bibliographic list + romanized "References"
  (assistant drafts entries; author verifies formatting)
- Mandatory members: World of Code; the three prior-work anchors; model reports (panel);
  chrF++ / sacrebleu / bootstrap / PlantUML tool citations; this study's public repo (open release)
- Target count ~12–20; every entry cited in text as [n]

---

## Exhibit budget (selection for readability — decide at assembly)

Page count is soft (over 10 pages allowed), so this is a preference ordering, not a quota.
Baseline selection ~3–4 tables + ~3–4 figures; the "Drop / fold" column marks second-choice
material to add back only if it earns its space:

| Slot | Take | Drop / fold |
|---|---|---|
| Table: headline two-arm (5.4) | selected columns, both populations | full micro+macro duplication (Ex. 2) |
| Table: population gap (5.5) | own table OR Δ-column folded into headline | separate chrF++ gap detail |
| Table: error taxonomy (5.7) | compact category×metric version | per-case tables, secondary counts |
| Figure: scaling curve (5.4) | yes — the Arm-B story in one image | — |
| Figure: per-relation F1 (5.6) | yes | per-relation table with full CIs (Ex. 4) |
| Figure: per-tier breakdown (5.6) | yes (or fold into scaling figure if space) | per-tier tables (Ex. 6), per-type tables (Ex. 5) |
| Frontier bars figure | only if space remains | — |
| Token-footprint table | never — prose only | Ex. 7 token table |

All captions bilingual («Рис./Fig.», «Табл./Table»); every exhibit referenced in text.

## Non-redundancy map (each fact's single home)

- Metric definitions, population definitions → 5.2 only; everywhere else by name
- Panel/arm rationale → 5.3 only (element 4 names the arms, doesn't justify them)
- Headline numbers → 5.4 only; Conclusions may repeat at most one
- Gap magnitudes + honest-headline rule → 5.5 only; 5.7 back-references, Abstract summarizes
- Hard-relations result → 5.6 (quantitative) with mechanism in 5.7 (qualitative) — split, not repeated
- Contribution/novelty statement → Conclusions in full; element 3 states the *gaps*, element 1 the
  *stakes* — three different sentences, no overlap
- Limitations → 5.8 only; Prospects (7) states futures without re-listing limitations

## Suggested drafting order (one leaf per session)

Front-to-back: viable here because the analysis is frozen and this plan fixes the structure the
framing sections must promise — element 1's forward hooks are written against the plan, not
against drafted prose. Elements 1–4 get a consistency pass after the body is done.

1. `manuscript.md` skeleton (headings only) + **element 1 Problem statement**
2. Element 2 Related work — reference gathering first (the "still to gather" list), then draft
3. Elements 3 + 4 (short; gaps and tasks are fixed in this plan)
4. 5.1 Benchmark dataset → 5. 5.2 Evaluation framework → 6. 5.3 Experimental setup
7. 5.4 Results headline → 8. 5.5 Population gap → 9. 5.6 Difficulty structure
10. 5.7 Error analysis → 11. 5.8 Discussion & limitations
12. Conclusions + Prospects
13. Abstracts + keywords (pure summary — always last); references pass; exhibit-budget assembly
    check; consistency pass over elements 1–4 against the finished body
