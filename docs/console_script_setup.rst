.. _console-script-setup:


Console Script Setup
====================

Optionally, your package can include a console script using Click.

How It Works
------------

If the 'command_line_interface' option is set to anything other than ['No command-line interface'] during setup, `cookiecutter` or `cruft` will add a file 'cli.py' in the _project_slug_ subdirectory.
An entry point is added to the ``pyproject.toml`` that points to the main function in ``cli.py``.

Usage
-----
To use the console script in development:

.. code-block:: console

    $ cd projectdir
    $ python -m pip install --editable .

'projectdir' should be the top level project directory with the `pyproject.toml` file

The script will be generated with output for no arguments and --help.

--help
    show help menu and exit

.. code-block:: console

    $ project_slug --help 
                                                                                                                                                                                                
    Usage: project_slug [OPTIONS]                                                                                                                                                            
                                                                                                                                                                                                    
    Console script for project_slug.                                                                                                                                                         
                                                                                                                                                                                                    
    ╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ --install-completion          Install completion for the current shell.                                           │
    │ --show-completion             Show completion for the current shell, to copy it or customize the installation.    │
    │ --help                        Show this message and exit.                                                         │
    ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
