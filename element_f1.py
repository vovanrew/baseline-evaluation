"""Element F1 — pure scoring logic (PLAN Phase 1, metric 2).

Operates on the structural graph emitted by the DiagramStatsExtractor fork:
nodes are class-like leaves (class diagrams) or participants (sequence). An
element is matched iff its node name matches after lowercasing and trimming;
matching is multiset (a name repeated k times must appear k times on both sides).

Empty/empty -> perfect (F1 1.0); a non-parsing prediction (empty graph) against
a non-empty ground truth scores F1 0.0, which realizes the zeros-for-failed mode.
"""
from __future__ import annotations

from collections import Counter


def normalize(name):
    return name.strip().lower()


def prf(gt_names, pred_names):
    """Precision/recall/F1 for one diagram, multiset matching on names."""
    gt = Counter(gt_names)
    pred = Counter(pred_names)
    tp = sum((gt & pred).values())
    n_gt = sum(gt.values())
    n_pred = sum(pred.values())
    fp = n_pred - tp
    fn = n_gt - tp

    precision = tp / n_pred if n_pred else (1.0 if n_gt == 0 else 0.0)
    recall = tp / n_gt if n_gt else (1.0 if n_pred == 0 else 0.0)
    f1 = 0.0 if (precision + recall) == 0 else 2 * precision * recall / (precision + recall)

    return {"tp": tp, "fp": fp, "fn": fn,
            "precision": precision, "recall": recall, "f1": f1}


def names_from_record(record):
    """Normalized node names from one extractor JSONL record (empty if no nodes)."""
    return [normalize(n["name"]) for n in (record.get("nodes") or [])]


def _f1(precision, recall):
    return 0.0 if (precision + recall) == 0 else 2 * precision * recall / (precision + recall)


def aggregate(per_diagram):
    """Micro (pooled counts) and macro (mean of per-diagram scores) over rows."""
    n = len(per_diagram)
    if n == 0:
        zero = {"precision": 0.0, "recall": 0.0, "f1": 0.0}
        return {"micro": dict(zero), "macro": dict(zero), "n": 0}

    tp = sum(r["tp"] for r in per_diagram)
    fp = sum(r["fp"] for r in per_diagram)
    fn = sum(r["fn"] for r in per_diagram)
    micro_p = tp / (tp + fp) if (tp + fp) else 1.0
    micro_r = tp / (tp + fn) if (tp + fn) else 1.0
    micro = {"precision": micro_p, "recall": micro_r, "f1": _f1(micro_p, micro_r)}

    macro = {k: sum(r[k] for r in per_diagram) / n
             for k in ("precision", "recall", "f1")}

    return {"micro": micro, "macro": macro, "n": n}


def compute(gt_by_key, pred_by_key, keys):
    """Per-diagram scores over `keys`. Missing prediction -> empty graph -> scored."""
    rows = []
    for key in keys:
        gt_names = names_from_record(gt_by_key[key])
        pred_rec = pred_by_key.get(key)
        pred_names = names_from_record(pred_rec) if pred_rec is not None else []
        row = {"key": key}
        row.update(prf(gt_names, pred_names))
        rows.append(row)
    return rows
