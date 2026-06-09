"""Extractor external-message direction tests (shell out to the fork JAR).

A sequence message with one endpoint off the diagram must keep its direction:
the empty external endpoint occupies the semantically correct side, mirroring
internal sender->receiver normalization (evaluation-framework.md §2.2). Inbound
`[-> A` (external is the sender) emits ('', 'A', message); outbound `A ->]`
(external is the receiver) emits ('A', '', message). Without this an inbound and
an outbound external message collapse to the same edge, so a prediction that
reverses one would spuriously match.
"""
import pytest

from element_f1_runner import EXTRACTOR_JAR, extract_graphs

FIXTURE_DIR = "data/relationship_f1/exo_fixtures"

EXPECTED = {
    "exo_in": ("", "A", "message"),    # [-> A : external sender -> A
    "exo_out": ("A", "", "message"),   # A ->] : A -> external receiver
}


@pytest.fixture(scope="module")
def graphs():
    return extract_graphs(FIXTURE_DIR, EXTRACTOR_JAR)


def _only_edge(record):
    edges = record["edges"]
    assert len(edges) == 1, f"expected exactly one edge, got {edges}"
    e = edges[0]
    return (e["source"], e["target"], e["relation"])


@pytest.mark.parametrize("stem,expected", list(EXPECTED.items()))
def test_exo_direction(graphs, stem, expected):
    assert _only_edge(graphs[stem]) == expected
