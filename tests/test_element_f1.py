"""Tests for the pure Element F1 logic (element_f1.py)."""
import math

import element_f1 as ef


def approx(a, b):
    return math.isclose(a, b, rel_tol=0, abs_tol=1e-9)


# --- normalize ---

def test_normalize_lowercases_and_strips():
    assert ef.normalize("  Order ") == "order"


def test_normalize_collapses_case_only_difference():
    assert ef.normalize("ApplicationTemplate") == ef.normalize("applicationtemplate")


# --- prf: exact / partial ---

def test_prf_perfect_match():
    r = ef.prf(["a", "b", "c"], ["a", "b", "c"])
    assert r["tp"] == 3 and r["fp"] == 0 and r["fn"] == 0
    assert approx(r["precision"], 1.0) and approx(r["recall"], 1.0) and approx(r["f1"], 1.0)


def test_prf_partial_overlap():
    r = ef.prf(["a", "b", "c"], ["a", "b", "d"])
    assert r["tp"] == 2 and r["fp"] == 1 and r["fn"] == 1
    assert approx(r["precision"], 2 / 3)
    assert approx(r["recall"], 2 / 3)
    assert approx(r["f1"], 2 / 3)


def test_prf_precision_recall_differ():
    # gt has 2, pred has 3, 2 correct -> recall 1.0, precision 2/3
    r = ef.prf(["a", "b"], ["a", "b", "c"])
    assert r["tp"] == 2 and r["fp"] == 1 and r["fn"] == 0
    assert approx(r["precision"], 2 / 3)
    assert approx(r["recall"], 1.0)
    assert approx(r["f1"], 2 * (2 / 3) * 1.0 / (2 / 3 + 1.0))


# --- prf: empty edge cases ---

def test_prf_both_empty_is_perfect():
    r = ef.prf([], [])
    assert approx(r["precision"], 1.0) and approx(r["recall"], 1.0) and approx(r["f1"], 1.0)


def test_prf_empty_prediction_against_nonempty_gt_is_zero():
    r = ef.prf(["a", "b"], [])
    assert r["tp"] == 0 and r["fn"] == 2
    assert approx(r["f1"], 0.0)


def test_prf_hallucination_against_empty_gt_is_zero():
    r = ef.prf([], ["a"])
    assert r["tp"] == 0 and r["fp"] == 1
    assert approx(r["f1"], 0.0)


# --- prf: duplicate names (multiset semantics) ---

def test_prf_duplicates_counted_as_multiset():
    r = ef.prf(["a", "a", "b"], ["a", "b"])
    assert r["tp"] == 2 and r["fp"] == 0 and r["fn"] == 1
    assert approx(r["precision"], 1.0)
    assert approx(r["recall"], 2 / 3)


# --- names_from_record ---

def test_names_from_record_extracts_and_normalizes():
    rec = {"nodes": [{"name": "Order", "type": "class"},
                     {"name": " Customer ", "type": "class"}]}
    assert ef.names_from_record(rec) == ["order", "customer"]


def test_names_from_record_empty_on_error():
    rec = {"nodes": [], "error": "no_block"}
    assert ef.names_from_record(rec) == []


def test_names_from_record_handles_missing_nodes_key():
    assert ef.names_from_record({"error": "parse_error"}) == []


# --- aggregate: micro + macro ---

def test_aggregate_micro_pools_counts():
    per = [
        ef.prf(["a", "b"], ["a", "b"]),       # tp2 fp0 fn0
        ef.prf(["c", "d"], ["c", "x"]),       # tp1 fp1 fn1
    ]
    agg = ef.aggregate(per)
    # micro: TP=3, FP=1, FN=1 -> p=3/4, r=3/4
    assert approx(agg["micro"]["precision"], 3 / 4)
    assert approx(agg["micro"]["recall"], 3 / 4)
    assert approx(agg["micro"]["f1"], 3 / 4)
    assert agg["n"] == 2


def test_aggregate_macro_means_per_diagram():
    per = [
        ef.prf(["a", "b"], ["a", "b"]),       # f1 1.0
        ef.prf(["c", "d"], ["c", "x"]),       # f1 0.5
    ]
    agg = ef.aggregate(per)
    assert approx(agg["macro"]["f1"], 0.75)


def test_aggregate_empty_list():
    agg = ef.aggregate([])
    assert agg["n"] == 0


# --- compute over keys with missing predictions ---

def test_compute_missing_prediction_scores_zero():
    gt = {
        "k1": {"nodes": [{"name": "A"}, {"name": "B"}]},
        "k2": {"nodes": [{"name": "C"}]},
    }
    pred = {"k1": {"nodes": [{"name": "A"}, {"name": "B"}]}}  # k2 missing
    rows = ef.compute(gt, pred, ["k1", "k2"])
    by_key = {r["key"]: r for r in rows}
    assert approx(by_key["k1"]["f1"], 1.0)
    assert approx(by_key["k2"]["f1"], 0.0)  # missing pred -> empty -> 0 vs nonempty gt


def test_compute_normalizes_case_across_sides():
    gt = {"k": {"nodes": [{"name": "Order"}]}}
    pred = {"k": {"nodes": [{"name": "order"}]}}
    rows = ef.compute(gt, pred, ["k"])
    assert approx(rows[0]["f1"], 1.0)
