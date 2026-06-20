# Master table — zero-shot image→PlantUML benchmark

**Models included: 1/1** (panel label: supplementary)

Two populations reported side by side as `zeros_for_failed / compiled_only`: `zeros_for_failed` scores all diagrams (non-compiled = 0); `compiled_only` is over compiled cells, with CSR reported separately. chrF++ values in the headline tables are micro (corpus sacrebleu, available at the overall scope only); the macro tables and JSON carry the poolable chrF++ macro for every scope. Type accuracy is the `compiled_only` population by definition.

### Overall (micro)

| Model | CSR | Element F1 | Relationship F1 | chrF++ | Type acc |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 96.8% | 0.918 / 0.943 | 0.729 / 0.748 | 64.32 / 66.73 | 0.938 |

### Overall (macro)

| Model | CSR | Element F1 | Relationship F1 | chrF++ | Type acc |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 96.8% | 0.924 / 0.955 | 0.808 / 0.833 | 67.78 / 70.02 | 0.938 |

### Population gap (compiled-only − all-1000, micro)

The `compiled_only` minus `zeros_for_failed` gap per metric — the headline measure of how much a model's apparent quality rests on selective failure. A model that drops/times out on its hard diagrams is graded on an easier subset, so its `compiled_only` score runs far above its honest all-1000 score; a large gap is that fingerprint (it tracks the answer rate / CSR).

| Model | CSR | Element F1 (all → cmp, Δ) | Relationship F1 (all → cmp, Δ) | chrF++ (all → cmp, Δ) |
|---|---|---|---|---|
| Claude Sonnet 4.6 | 96.8% | 0.918 → 0.943 (+0.025) | 0.729 → 0.748 (+0.019) | 64.32 → 66.73 (+2.41) |

### Relationship F1 by relation type (read-through)

**Claude Sonnet 4.6** — F1 (zeros_for_failed / compiled_only), support_gt:

| Relation | F1 (z / c) | support_gt (z / c) |
|---|---|---|
| inheritance | 0.831 / 0.848 | 940 / 903 |
| composition | 0.483 / 0.517 | 300 / 271 |
| aggregation | 0.521 / 0.537 | 244 / 232 |
| dependency | 0.538 / 0.565 | 393 / 353 |
| association | 0.595 / 0.629 | 1014 / 904 |
| message | 0.763 / 0.778 | 6546 / 6292 |

### Type accuracy by GT entity type (compiled_only, read-through)

**Claude Sonnet 4.6** — pooled accuracy 0.938 (matched 5139, excluded 60, denominator 5079):

| GT type | support | accuracy |
|---|---|---|
| abstract_class | 139 | 0.942 |
| actor | 273 | 0.996 |
| annotation | 1 | 1.000 |
| boundary | 70 | 0.329 |
| class | 2263 | 0.979 |
| collections | 30 | 0.200 |
| control | 79 | 0.354 |
| database | 108 | 0.954 |
| entity | 102 | 0.245 |
| enum | 56 | 0.964 |
| interface | 214 | 0.963 |
| object | 7 | 0.000 |
| participant | 1730 | 0.983 |
| queue | 7 | 0.000 |

## By diagram type

### Type: class (micro)

| Model | CSR | Element F1 | Relationship F1 | chrF++ | Type acc |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 95.8% | 0.919 / 0.955 | 0.650 / 0.678 | — / — | 0.966 |

### Type: sequence (micro)

| Model | CSR | Element F1 | Relationship F1 | chrF++ | Type acc |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 97.8% | 0.918 / 0.929 | 0.763 / 0.778 | — / — | 0.907 |

## By tier

### Tier 1 (micro)

| Model | CSR | Element F1 | Relationship F1 | chrF++ | Type acc |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 99.2% | 0.966 / 0.970 | 0.944 / 0.947 | — / — | 0.975 |

### Tier 2 (micro)

| Model | CSR | Element F1 | Relationship F1 | chrF++ | Type acc |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 97.2% | 0.967 / 0.980 | 0.878 / 0.888 | — / — | 0.941 |

### Tier 3 (micro)

| Model | CSR | Element F1 | Relationship F1 | chrF++ | Type acc |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 96.4% | 0.939 / 0.956 | 0.798 / 0.807 | — / — | 0.913 |

### Tier 4 (micro)

| Model | CSR | Element F1 | Relationship F1 | chrF++ | Type acc |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 94.4% | 0.869 / 0.910 | 0.618 / 0.644 | — / — | 0.941 |

