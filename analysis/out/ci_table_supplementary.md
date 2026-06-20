# Paired bootstrap CIs — zero-shot image→PlantUML benchmark

**Models included: 1/1**

Method: paired percentile bootstrap (2.5/97.5), resample diagrams, shared draws across models; n=1000 resamples, seed=20260614. Cells are `point [2.5th, 97.5th]`. CSR / F1 / type-accuracy on the 0–1 scale (3 dp); chrF++ on its native scale (2 dp). chrF++ **micro** is a corpus statistic with no per-diagram component — reported as a point estimate, no CI.

## Per-model 95% CIs (headline metrics)

| Model | CSR | Element F1 micro (zeros) | Element F1 micro (compiled) | Rel F1 micro (zeros) | Rel F1 micro (compiled) | chrF++ macro (zeros) | chrF++ macro (compiled) | Type acc |
|---|---|---|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 0.968 [0.956, 0.978] | 0.918 [0.897, 0.936] | 0.943 [0.926, 0.959] | 0.729 [0.693, 0.762] | 0.748 [0.713, 0.784] | 67.78 [66.40, 69.16] | 70.02 [68.90, 71.21] | 0.938 [0.922, 0.953] |

chrF++ micro (point estimate, no CI), zeros / compiled:

- **Claude Sonnet 4.6**: 64.32 / 66.73

## Pairwise model-difference CIs

Δ = row model − column model (positive ⇒ the first model scores higher). `excludes 0` flags a CI that does not contain zero (significant at 95%).

### CSR

| Pair (A − B) | Δ | 95% CI | excludes 0 |
|---|---|---|---|

### Element F1 micro (zeros)

| Pair (A − B) | Δ | 95% CI | excludes 0 |
|---|---|---|---|

### Element F1 micro (compiled)

| Pair (A − B) | Δ | 95% CI | excludes 0 |
|---|---|---|---|

### Rel F1 micro (zeros)

| Pair (A − B) | Δ | 95% CI | excludes 0 |
|---|---|---|---|

### Rel F1 micro (compiled)

| Pair (A − B) | Δ | 95% CI | excludes 0 |
|---|---|---|---|

### chrF++ macro (zeros)

| Pair (A − B) | Δ | 95% CI | excludes 0 |
|---|---|---|---|

### chrF++ macro (compiled)

| Pair (A − B) | Δ | 95% CI | excludes 0 |
|---|---|---|---|

### Type acc

| Pair (A − B) | Δ | 95% CI | excludes 0 |
|---|---|---|---|

## Relationship F1 by relation type — per-model 95% CIs

### Population: zeros_for_failed (micro F1)

| Model | inheritance | composition | aggregation | dependency | association | message |
|---|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 0.831 [0.794, 0.868] | 0.483 [0.367, 0.594] | 0.521 [0.418, 0.622] | 0.538 [0.456, 0.623] | 0.595 [0.524, 0.661] | 0.763 [0.716, 0.809] |

### Population: compiled_only (micro F1)

| Model | inheritance | composition | aggregation | dependency | association | message |
|---|---|---|---|---|---|---|
| Claude Sonnet 4.6 | 0.848 [0.814, 0.883] | 0.517 [0.397, 0.628] | 0.537 [0.432, 0.639] | 0.565 [0.486, 0.651] | 0.629 [0.559, 0.693] | 0.778 [0.730, 0.825] |

