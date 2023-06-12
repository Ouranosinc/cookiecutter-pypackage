#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path().cwd().absolute()


def remove_file(filepath):
    Path(PROJECT_DIRECTORY).joinpath(filepath).unlink()


def remove_folder(folderpath):
    for file in Path(PROJECT_DIRECTORY).joinpath(folderpath).iterdir():
        if not file.is_dir():
            file.unlink()
            continue
        file.rmdir()
    Path(PROJECT_DIRECTORY).joinpath(folderpath).rmdir()


def replace_contents(filepath):
    replacements = {
        "__PYTHON_VERSION__": 'matrix.python-version',
        "__GITHUB_TOKEN__": 'secrets.GITHUB_TOKEN',
        '__TOX_ENV__': 'matrix.tox-env',
        "__PYPI_API_TOKEN__": "secrets.PYPI_API_TOKEN",
        "__TEST_PYPI_API_TOKEN__": "secrets.TEST_PYPI_API_TOKEN"
    }

    lines = []
    with open(filepath) as infile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, " ".join(["${ {".replace(" ", ""), target, "} }".replace(" ", "")]))
            lines.append(line)
    with open(filepath, 'w') as outfile:
        for line in lines:
            outfile.write(line)


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "{{ cookiecutter.make_docs }}" != "y":
        remove_file("requirements_docs.txt")
        remove_folder("docs")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = Path("{{ cookiecutter.project_slug }}").joinpath("cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
        remove_file(".zenodo.json")

    for f in Path(".github/workflows").glob("*.yml"):
        replace_contents(f)
