#!/usr/bin/env python
"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pathlib
from importlib.util import find_spec
{% if cookiecutter.use_pytest == 'n' -%}
import unittest
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}import {{ cookiecutter.project_slug }}.cli as cli{%- endif %}
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}  # noqa: F401
{%- if cookiecutter.use_pytest == 'y' %}


# import pytest

# @pytest.fixture
# def response():
#     """Sample pytest fixture.
#
#     See more at: https://doc.pytest.org/en/latest/explanation/fixtures.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string
{%- if cookiecutter.command_line_interface|lower == 'click' %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_slug }}.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
{%- endif %}
{%- else %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
{%- if cookiecutter.command_line_interface|lower == 'click' %}

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert "{{ cookiecutter.project_slug }}.cli.main" in result.output
        help_result = runner.invoke(cli.main, ["--help"])
        assert help_result.exit_code == 0
        assert "--help  Show this message and exit." in help_result.output
{%- endif %}
{%- endif %}


def test_package_metadata():
    """Test the package metadata."""
    project = find_spec("{{ cookiecutter.project_slug }}")

    assert project is not None
    assert project.submodule_search_locations is not None
    location = project.submodule_search_locations[0]

    metadata = pathlib.Path(location).resolve().joinpath("__init__.py")

    with metadata.open() as f:
        contents = f.read()
        assert """{{ cookiecutter.full_name }}""" in contents
        assert '__email__ = "{{ cookiecutter.email }}"' in contents
        assert '__version__ = "{{ cookiecutter.version }}"' in contents
