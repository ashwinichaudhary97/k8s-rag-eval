"""Verify that config.yaml exists, parses, and contains the expected keys."""

from pathlib import Path

import yaml

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.yaml"


def test_config_exists() -> None:
    assert CONFIG_PATH.exists(), f"config.yaml not found at {CONFIG_PATH}"


def test_config_parses_and_has_expected_sections() -> None:
    data = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    for section in ("corpus", "chunking", "embedding", "retrieval", "evaluation", "judge", "paths"):
        assert section in data, f"missing section: {section}"


def test_retrieval_top_k_is_int() -> None:
    data = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    assert isinstance(data["retrieval"]["top_k"], int)
    assert data["retrieval"]["top_k"] > 0
