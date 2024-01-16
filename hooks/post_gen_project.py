#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path().cwd().absolute()


def create_folder(folder_path):
    Path(PROJECT_DIRECTORY).joinpath(folder_path).mkdir(parents=True, exist_ok=True)


def remove_file(filepath):
    Path(PROJECT_DIRECTORY).joinpath(filepath).unlink()


def remove_folder(folder_path):
    for file in Path(PROJECT_DIRECTORY).joinpath(folder_path).iterdir():
        if not file.is_dir():
            file.unlink()
            continue
        file.rmdir()
    Path(PROJECT_DIRECTORY).joinpath(folder_path).rmdir()


def replace_contents(filepath):
    replacements = {
        "__ACTIONS_VERSIONS_UPDATER_TOKEN__": "secrets.ACTIONS_VERSIONS_UPDATER_TOKEN",
        "__BUMP_VERSION_TOKEN__": "secrets.BUMP_VERSION_TOKEN",
        "__GITHUB_REF__": "github.ref",
        "__GITHUB_REF_NAME__": "github.ref_name",
        "__GITHUB_TOKEN__": "secrets.GITHUB_TOKEN",
        "__PYTHON_VERSION__": "matrix.python-version",
        "__TOX_ENV__": "matrix.tox-env",
    }

    lines = []
    with open(filepath) as infile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(
                    src,
                    " ".join(["${ {".replace(" ", ""), target, "} }".replace(" ", "")]),
                )
            lines.append(line)
    with open(filepath, "w") as outfile:
        for line in lines:
            outfile.write(line)


if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "{{ cookiecutter.make_docs }}" != "y":
        remove_file(".readthedocs.yml")
        remove_file("environment-docs.yml")
        remove_folder("docs")
    else:
        create_folder("docs/apidoc")
        if "{{ cookiecutter.add_translations }}" == "y":
            create_folder("docs/locales")

    if "{{ cookiecutter.use_conda }}" != "y":
        remove_file("environment-dev.yml")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = Path("{{ cookiecutter.project_slug }}").joinpath("cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
        remove_file(".zenodo.json")

    for f in Path(".github/workflows").glob("*.yml"):
        replace_contents(f)
