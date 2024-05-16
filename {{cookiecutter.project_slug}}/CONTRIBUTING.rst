============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at {{ cookiecutter.__gh_slug }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts, articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at {{ cookiecutter.__gh_slug }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome. :)

Get Started!
------------

.. note::

    If you are new to using GitHub and `git`, please read `this guide <https://guides.github.com/activities/hello-world/>`_ first.

{%- if cookiecutter.use_conda == 'y' %}

.. warning::

    Anaconda Python users: Due to the complexity of some packages, the default dependency solver can take a long time to resolve the environment. Consider running the following commands in order to speed up the process:

    .. code-block:: console

        conda install -n base conda-libmamba-solver
        conda config --set solver libmamba

    For more information, please see the following link: https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community

    Alternatively, you can use the `mamba <https://mamba.readthedocs.io/en/latest/index.html>`_ package manager, which is a drop-in replacement for ``conda``. If you are already using `mamba`, replace the following commands with ``mamba`` instead of ``conda``.

{%- endif %}

Ready to contribute? Here's how to set up ``{{ cookiecutter.project_name }}`` for local development.

#. Fork the ``{{ cookiecutter.project_name }}`` repo on GitHub.
#. Clone your fork locally:

    .. code-block:: console

        git clone git@github.com:your_name_here/{{ cookiecutter.project_name | replace(' ', '-') }}.git

#. Install your local copy into a development environment. {% if cookiecutter.use_conda == 'y' -%}

  You can create a new Anaconda development environment with:

    .. code-block:: console

        conda env create -f environment-dev.yml
        conda activate {{ cookiecutter.project_slug }}
        make dev
  {%- else -%}

  Using ``virtualenv`` (``virtualenvwrapper``), you can create a new development environment with:

    .. code-block:: console

        python -m pip install virtualenvwrapper
        mkvirtualenv {{ cookiecutter.project_slug }}
        cd {{ cookiecutter.project_slug }}/
        make dev
  {%- endif %}

  This installs ``{{ cookiecutter.project_slug }}`` in an "editable" state, meaning that changes to the code are immediately seen by the environment. To ensure a consistent coding style, ``make dev`` also installs the ``pre-commit`` hooks to your local clone.

  On commit, ``pre-commit`` will check that{% if cookiecutter.use_black == 'y' %} ``black``, ``blackdoc``, ``isort``,{% endif %} ``flake8``, and ``ruff`` checks are passing, perform automatic fixes if possible, and warn of violations that require intervention. If your commit fails the checks initially, simply fix the errors, re-add the files, and re-commit.

  You can also run the hooks manually with:

    .. code-block:: console

        pre-commit run -a

  If you want to skip the ``pre-commit`` hooks temporarily, you can pass the ``--no-verify`` flag to `git commit`.

#. Create a branch for local development:

    .. code-block:: console

        git checkout -b name-of-your-bugfix-or-feature

  Now you can make your changes locally.

#. When you're done making changes, we **strongly** suggest running the tests in your environment or with the help of ``tox``:

    .. code-block:: console

        make lint
        python -m pytest
        # Or, to run multiple build tests
        python -m tox

#. Commit your changes and push your branch to GitHub:

    .. code-block:: console

        git add .
        git commit -m "Your detailed description of your changes."
        git push origin name-of-your-bugfix-or-feature

    If ``pre-commit`` hooks fail, try re-committing your changes (or, if need be, you can skip them with `git commit --no-verify`).

#. Submit a `Pull Request <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_ through the GitHub website.

#. When pushing your changes to your branch on GitHub, the documentation will automatically be tested to reflect the changes in your Pull Request. This build process can take several minutes at times. If you are actively making changes that affect the documentation and wish to save time, you can compile and test your changes beforehand locally with:

    .. code-block:: console

        # To generate the html and open it in your browser
        make docs
        # To only generate the html
        make autodoc
        make -C docs html
        # To simply test that the docs pass build checks
        python -m tox -e docs

#. Once your Pull Request has been accepted and merged to the ``main`` branch, several automated workflows will be triggered:

    - The ``bump-version.yml`` workflow will automatically bump the patch version when pull requests are pushed to the ``main`` branch on GitHub. **It is not recommended to manually bump the version in your branch when merging (non-release) pull requests (this will cause the version to be bumped twice).**
    - `ReadTheDocs` will automatically build the documentation and publish it to the `latest` branch of `{{ cookiecutter.project_slug }}` documentation website.
    - If your branch is not a fork (ie: you are a maintainer), your branch will be automatically deleted.

    You will have contributed your first changes to ``{{ cookiecutter.project_slug }}``!

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

#. The pull request should include tests and should aim to provide `code coverage <https://en.wikipedia.org/wiki/Code_coverage>`_ for all new lines of code. You can use the ``--cov-report html --cov {{ cookiecutter.project_slug }}`` flags during the call to ``pytest`` to generate an HTML report and analyse the current test coverage.

#. If the pull request adds functionality, the docs should also be updated. Put your new functionality into a function with a docstring, and add the feature to the list in ``README.rst``.

#. The pull request should work for Python 3.8, 3.9, 3.10, 3.11, 3.12 and PyPy. Check that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests:

   .. code-block:: console

{% if cookiecutter.use_pytest == 'y' %}
        pytest tests.test_{{ cookiecutter.project_slug }}
{% else %}
        python -m unittest tests.test_{{ cookiecutter.project_slug }}
{%- endif %}

To run specific code style checks:

    .. code-block:: console

        python -m black --check {{ cookiecutter.project_slug }} tests
        python -m isort --check {{ cookiecutter.project_slug }} tests
        python -m blackdoc --check {{ cookiecutter.project_slug }} docs
        python -m ruff {{ cookiecutter.project_slug }} tests
        python -m flake8 {{ cookiecutter.project_slug }} tests

To get ``black``, ``isort``, ``blackdoc``, ``ruff``, and ``flake8`` (with plugins ``flake8-alphabetize`` and ``flake8-rst-docstrings``) simply install them with `pip` {% if cookiecutter.use_conda == 'y' %}(or `conda`) {% endif %}into your environment.

Code of Conduct
---------------

Please note that this project is released with a `Contributor Code of Conduct <{{ cookiecutter.__gh_slug}}/blob/main/CODE_OF_CONDUCT.rst>`_.
By participating in this project you agree to abide by its terms.
