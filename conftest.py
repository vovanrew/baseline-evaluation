"""Pytest path config: expose evaluation/ as a flat module root.

Tests under tests/ import scorers (chrf, element_f1, ...) and runners
(element_f1_runner, ...) with plain `import name` style, mirroring how the
runners themselves import their siblings inside evaluation/. Adding the
directory to sys.path here matches what Python does automatically when a
runner is invoked as `python evaluation/<runner>.py` from the project root.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "evaluation"))
