import datetime
import importlib.util
import os
import shlex
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

import pytest
from click.testing import CliRunner
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    kwargs.update(template=Path(__file__).parents[1].as_posix())
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project_path.joinpath("LICENSE")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read_text()


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    assert result.exception is None
    assert result.project_path.is_dir()

    project_path = result.project_path
    project_slug = project_path.name
    project_dir = project_path.joinpath("src").joinpath(project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "LICENSE" in found_toplevel_files
        assert "Makefile" in found_toplevel_files
        assert "README.rst" in found_toplevel_files
        assert "environment-dev.yml" in found_toplevel_files
        assert "pyproject.toml" in found_toplevel_files
        assert "src" in found_toplevel_files
        assert (
            "python_boilerplate"
            in next(result.project_path.joinpath("src").iterdir()).name
        )
        assert "tests" in found_toplevel_files
        assert "tox.toml" in found_toplevel_files


def test_bake_and_run_unittests(cookies):
    with bake_in_temp_dir(cookies, extra_context={"use_pytest": "n"}) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("python -m coverage", str(result.project_path)) == 0
        print("test_bake_and_run_unittests path", str(result.project_path))


def test_bake_and_build_package(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("python -m flit build", str(result.project_path)) == 0
        assert run_inside_dir("twine check dist/*", str(result.project_path)) == 0
        print("test_bake_and_build_package path", str(result.project_path))


@pytest.mark.precommit
def test_bake_and_run_pre_commit(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("git init", str(result.project_path)) == 0
        assert run_inside_dir("git add *", str(result.project_path)) == 0
        assert run_inside_dir("pre-commit install", str(result.project_path)) == 0
        assert (
            run_inside_dir(
                "pre-commit run --all-files --show-diff-on-failure",
                str(result.project_path),
            )
            == 0
        )
        print("test_bake_and_run_pre_commit path", str(result.project_path))


def test_bake_with_special_chars_and_run_tests(cookies):
    """Ensure that a `full_name` with double quotes does not break pyproject.toml."""
    with bake_in_temp_dir(
        cookies, extra_context={"full_name": 'name "quote" name', "use_pytest": "n"}
    ) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("python -m coverage", str(result.project_path)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies):
    """Ensure that a `full_name` with apostrophes does not break pyproject.toml."""
    with bake_in_temp_dir(
        cookies, extra_context={"full_name": "O'connor", "use_pytest": "n"}
    ) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("python -m coverage", str(result.project_path)) == 0


def test_bake_without_translations(cookies):
    with bake_in_temp_dir(cookies, extra_context={"add_translations": "n"}) as result:
        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "docs" in found_toplevel_files
        assert ".readthedocs.yml" in found_toplevel_files
        assert "environment-docs.yml" in found_toplevel_files

        pyproject_path = result.project_path.joinpath("pyproject.toml")
        with open(str(pyproject_path)) as pyproject_file:
            assert "sphinx-intl" not in pyproject_file.read()


def test_bake_without_docs(cookies):
    with bake_in_temp_dir(cookies, extra_context={"make_docs": "n"}) as result:
        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "docs" not in found_toplevel_files
        assert ".readthedocs.yml" not in found_toplevel_files
        assert "environment-docs.yml" not in found_toplevel_files
        docs_files = {
            "docs/**/*.rst",
            "docs/**/*.jpg",
            "docs/**/*.png",
            "docs/**/*.gif",
            "docs/Makefile",
            "docs/conf.py",
            "docs/make.bat",
        }
        pyproject_path = result.project_path.joinpath("pyproject.toml")
        with open(str(pyproject_path)) as pyproject_file:
            for file in docs_files:
                assert file not in pyproject_file.read()


def test_bake_without_author_file(cookies):
    with bake_in_temp_dir(cookies, extra_context={"create_author_file": "n"}) as result:
        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "AUTHORS.rst" not in found_toplevel_files
        doc_files = [f.name for f in result.project_path.joinpath("docs").iterdir()]
        assert "authors.rst" not in doc_files

        # Assert there are no spaces in the toc tree
        docs_index_path = result.project_path.joinpath("docs/index.rst")
        with open(str(docs_index_path)) as index_file:
            assert "releasing\n   changelog" in index_file.read()

        # Check that
        pyproject_path = result.project_path.joinpath("pyproject.toml")
        with open(str(pyproject_path)) as pyproject_file:
            assert "AUTHORS.rst" not in pyproject_file.read()


def test_make_help(cookies):
    with bake_in_temp_dir(cookies) as result:
        # The supplied Makefile does not support win32
        if sys.platform != "win32":
            output = check_output_inside_dir("make help", str(result.project_path))
            assert b"check code coverage quickly with the default Python" in output


def test_bake_selecting_license(cookies):
    license_strings = {
        "MIT license": ("MIT", "MIT"),
        "BSD license": (
            "Redistributions of source code must retain the above copyright notice, this",
            "BSD-3-Clause",
        ),
        "ISC license": ("ISC License", "ISC"),
        "Apache Software License 2.0": (
            "Licensed under the Apache License, Version 2.0",
            "Apache-2.0",
        ),
        "GNU General Public License v3": (
            "GNU GENERAL PUBLIC LICENSE",
            "GPL-3.0-or-later",
        ),
    }
    for license_code, target_strings in license_strings.items():
        with bake_in_temp_dir(
            cookies, extra_context={"open_source_license": license_code}
        ) as result:
            assert (
                target_strings[0] in result.project_path.joinpath("LICENSE").read_text()
            )
            assert (
                target_strings[1]
                in result.project_path.joinpath("pyproject.toml").read_text()
            )


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "pyproject.toml" in found_toplevel_files
        assert "LICENSE" not in found_toplevel_files
        assert "License" not in result.project_path.joinpath("README.rst").read_text()


def _running_tox():
    return os.getenv("TOX", False)


@pytest.mark.skipif("not _running_tox()", reason="Not running on tox")
def test_using_pytest(cookies):
    with bake_in_temp_dir(cookies, extra_context={"use_pytest": "y"}) as result:
        assert result.project_path.is_dir()
        test_file_path = result.project_path.joinpath(
            "tests/test_python_boilerplate.py"
        )
        text = test_file_path.read_text()
        assert "import pytest" in text
        # Test the new pytest target
        assert run_inside_dir("pip install --editable .", str(result.project_path)) == 0
        assert run_inside_dir("pytest", str(result.project_path)) == 0


def test_not_using_pytest(cookies):
    with bake_in_temp_dir(cookies, extra_context={"use_pytest": "n"}) as result:
        assert result.project_path.is_dir()
        test_file_path = result.project_path.joinpath(
            "tests/test_python_boilerplate.py"
        )
        text = test_file_path.read_text()
        assert "import unittest" in text
        assert "import pytest" not in text


# def test_project_with_hyphen_in_module_name(cookies):
#     result = cookies.bake(extra_context={"project_name": "something-with-a-dash"})
#     assert result.project is not None
#     project_path = str(result.project)
#
#     # when:
#     travis_setup_cmd = (
#         "python travis_pypi_setup.py"
#         " --repo audreyr/cookiecutter-pypackage"
#         " --password invalidpass"
#     )
#     run_inside_dir(travis_setup_cmd, project_path)
#
#     # then:
#     result_travis_config = yaml.load(open(os.path.join(project_path, ".travis.yml")))
#     assert (
#         "secure" in result_travis_config["deploy"]["password"]
#     ), "missing password config in .travis.yml"


def test_bake_with_no_console_script(cookies):
    context = {"command_line_interface": "No command-line interface"}
    result = cookies.bake(
        extra_context=context, template=Path(__file__).parents[1].as_posix()
    )
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" not in found_project_files

    pyproject_path = os.path.join(project_path, "pyproject.toml")
    with open(pyproject_path) as setup_file:
        assert "[project.scripts]" not in setup_file.read()


@pytest.mark.parametrize("option", ["Click", "Argparse", "Typer"])
def test_bake_with_console_options_script_files(cookies, option):
    context = {"command_line_interface": option}
    result = cookies.bake(
        extra_context=context, template=Path(__file__).parents[1].as_posix()
    )
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" in found_project_files

    pyproject_path = os.path.join(project_path, "pyproject.toml")
    with open(pyproject_path) as setup_file:
        assert "[project.scripts]" in setup_file.read()


def test_bake_with_console_options_script_click(cookies):
    context = {"command_line_interface": "Click"}
    result = cookies.bake(
        extra_context=context, template=Path(__file__).parents[1].as_posix()
    )
    project_path, project_slug, project_dir = project_info(result)
    module_path = os.path.join(project_dir, "cli.py")
    module_name = ".".join([project_slug, "cli"])
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0
    noarg_output = " ".join(
        ["Replace this message by putting your code into", project_slug]
    )
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output


@pytest.mark.parametrize("orcid,expected", [("N/A", False), ("1234-5678-9abc", True)])
def test_orcid(cookies, orcid, expected):
    with bake_in_temp_dir(cookies, extra_context={"orcid_id": orcid}) as result:
        assert result.project_path.is_dir()
        cff_path = result.project_path.joinpath("CITATION.cff")
        assert (f"orcid: \"https://orcid.org/{orcid}\"" in cff_path.read_text()) is expected
        zenodo_path = result.project_path.joinpath(".zenodo.json")
        assert (f"\"orcid\": \"{orcid}\"" in zenodo_path.read_text()) is expected
