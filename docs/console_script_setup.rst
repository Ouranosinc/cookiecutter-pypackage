.. _console-script-setup:


Console Script Setup
====================

Optionally, your package can include a console script using Click.

How It Works
------------

If the 'command_line_interface' option is set to ['click'] during setup, cookiecutter will add a file 'cli.py' in the project_slug subdirectory. An entry point is added to the `pyproject.toml` that points to the main function in `cli.py`.

Usage
-----
To use the console script in development:

.. code-block:: bash

    python -m flit install --symlink projectdir

'projectdir' should be the top level project directory with the `pyproject.toml` file

The script will be generated with output for no arguments and --help.

--help
    show help menu and exit

Known Issues
------------
Using `flit`, installing the project from sources in a development environment using:

.. code-block:: bash

    python -m pip install --editable projectdir

will not necessarily create an editable install. This is a known issue with `flit`. The following will work as expected:

.. code-block:: bash

    python -m flit install --symlink projectdir

More Details
------------

You can read more about `--editable` installations and flit at:
 - https://github.com/pypa/flit/issues/512
 - https://github.com/pypa/flit/issues/522

