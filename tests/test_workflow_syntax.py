import os
import yaml
import pytest

WORKFLOW_DIR = "workflows"


def test_workflow_yaml_syntax():
    for fname in os.listdir(WORKFLOW_DIR):
        if fname.endswith(".yml") or fname.endswith(".yaml"):
            with open(os.path.join(WORKFLOW_DIR, fname)) as f:
                try:
                    yaml.safe_load(f)
                except Exception as e:
                    pytest.fail(f"Invalid YAML in {fname}: {e}")
