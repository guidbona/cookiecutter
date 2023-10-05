"""Tests for `cookiecutter.find` module."""
from pathlib import Path
from jinja2 import Environment

import pytest

from cookiecutter import find
from cookiecutter.environment import StrictEnvironment


@pytest.fixture(params=['fake-repo-pre', 'fake-repo-pre2'])
def repo_dir(request):
    """Fixture returning path for `test_find_template` test."""
    return Path('tests', request.param)


def test_find_template(repo_dir):
    """Verify correctness of `find.find_template` path detection."""
    env = StrictEnvironment()
    template = find.find_template(repo_dir=repo_dir, environment=env)

    test_dir = Path(repo_dir, '{{cookiecutter.repo_name}}')
    assert template == test_dir
