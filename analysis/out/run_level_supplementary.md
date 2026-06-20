# Run-level aggregator — zero-shot image→PlantUML benchmark

**Models included: 1/1** (panel: supplementary).

## Token totals (all 1000 cells incl. failures)

Output already includes reasoning (no double count); Gemini output = candidates + thoughts. No dollar pricing (out of scope).

| Model | cells | input | output | reasoning | total |
|---|--:|--:|--:|--:|--:|
| Claude Sonnet 4.6 | 1000 | 1.415M | 0.341M | 0.000M | 1.756M |

## Failure / outcome inventory

Provider/harness failure (source B) vs model compile-fail (source A CSR). `no_response` reconciles with source-A `has_pred==false`.

| Model | compiled | compile-fail | no-response | timeout | image_dropped | http_error | network_error | reconcile |
|---|--:|--:|--:|--:|--:|--:|--:|:--:|
| Claude Sonnet 4.6 | 968 | 32 | 0 | 0 | 0 | 0 | 0 | ✓ |

## Provenance manifest

| Model | snapshot | provider | base_url | reasoning config | max_tokens | temp | started | leak |
|---|---|---|---|---|--:|--:|---|--:|
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | openai | https://api.anthropic.com/v1 | `{"thinking": {"type": "disabled"}}` | 5376 | 0 | 20260613T154151Z | 0 |

## Per-tier crowding descriptor (model-independent)

content_lines per megapixel after 1568px resize (pooled total/total); from the real `data/puml_images_1568/` PNG dimensions (1000 diagrams). Machine artifact: `crowding.json` (Task-3 `crowding=` hook).

| Tier | n | content_lines | MP | lines/MP |
|---|--:|--:|--:|--:|
| 1 | 250 | 1864 | 213.15 | 8.74 |
| 2 | 250 | 4268 | 322.15 | 13.25 |
| 3 | 250 | 8331 | 394.50 | 21.12 |
| 4 | 250 | 19668 | 392.64 | 50.09 |

