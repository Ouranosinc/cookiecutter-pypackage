"""Console script for {{cookiecutter.project_slug}}."""
{% if cookiecutter.command_line_interface|lower == 'argparse' -%}
import argparse
import sys


def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print(f"Arguments: {args._}")
    print("Replace this message by putting your code into {{cookiecutter.project_slug}}.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

{%- elif cookiecutter.command_line_interface|lower == 'click' -%}
import sys

import click


@click.command()
def main(args=None) -> int:
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo(
        "Replace this message by putting your code into {{cookiecutter.project_slug}}.cli.main",
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
{%- elif cookiecutter.command_line_interface|lower == 'typer' %}
import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()  # type: ignore[misc]
def main() -> None:
    """Console script for {{cookiecutter.project_slug}}."""
    console.print(
        "Replace this message by putting your code into {{cookiecutter.project_slug}}.cli.main",
    )
    console.print("See Typer documentation at https://typer.tiangolo.com/")


if __name__ == "__main__":
    app()
{%- endif %}
