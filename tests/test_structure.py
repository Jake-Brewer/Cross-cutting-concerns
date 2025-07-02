import os
import pytest

REQUIRED_DIRS = [
    'templates',
    'workflows',
    'cookiecutters',
    'org-global-defaults',
    'templates/ISSUE_TEMPLATE',
]
REQUIRED_FILES = [
    'README.md',
    'CONTRIBUTING.md',
    'templates/ISSUE_TEMPLATE/bug_report.md',
    'templates/ISSUE_TEMPLATE/feature_request.md',
    'workflows/ci.yml',
]

def test_required_directories_exist():
    for d in REQUIRED_DIRS:
        assert os.path.isdir(d), f"Missing directory: {d}"

def test_required_files_exist():
    for f in REQUIRED_FILES:
        assert os.path.isfile(f), f"Missing file: {f}" 