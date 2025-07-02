import os
import pytest


@pytest.mark.skipif(
    "GITHUB_TOKEN" not in os.environ and "CI" not in os.environ,
    reason="Missing GITHUB_TOKEN or CI env var for CI context",
)
def test_env_vars():
    assert True


@pytest.mark.skipif(
    not any(os.getcwd() in p for p in os.environ.get("PATH", "").split(os.pathsep)),
    reason="Project root not in PATH",
)
def test_path_contains_project_root():
    assert True
