"""Verify the package imports and exposes a version."""

import k8s_rag_eval


def test_version_is_string() -> None:
    assert isinstance(k8s_rag_eval.__version__, str)
    assert k8s_rag_eval.__version__.count(".") >= 1
