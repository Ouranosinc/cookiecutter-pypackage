======================
Cookiecutter PyPackage
======================

|build|

Cookiecutter_ template for a Python package.

* GitHub repo (fork): https://github.com/Ouranosinc/cookiecutter-pypackage/
* Documentation (upstream): https://cookiecutter-pypackage.readthedocs.io/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` with ``coverage run`` or ``pytest``
* `pyproject.toml`_ with flit_ backend for PEP 517/621-compliant packaging.
* `GitHub Actions`_: Ready for GitHub Actions Continuous Integration testing.
* `Conda`_ environment file: Optionally use ``conda env create -f environment-dev.yml`` to create a new environment with the correct Python version.
* Tox_ testing: Setup to easily test for Python 3.8, 3.9, 3.10, 3.11, 3.12, and PyPy3.
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* pre-commit_ hook: Run your tests and linting (e.g. `black`, `flake8`, `pylint`, etc.) before you commit your code!
* `pre-commit.ci`_: Automate `pre-commit` checks and corrections in your Pull Requests.
* bump-my-version_: Pre-configured `SemVer-2.0-compliant`_ version bumping with a single command.
* dependabot_ for automated dependency updates of both project dependencies and GitHub Actions.
* `sphinx-intl`_ for French internationalization (i18n) and localization (l10n) of Sphinx docs (optional)
* Auto-release to TestPyPI_ and PyPI_ when you push a new tag to main (optional)
* Command line interface using Click (optional)

Build Status
-------------

Upstream (audreyfeldroy/cookiecutter-pypackage): |docs-upstream| |pyup-upstream|

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet ::

    $ pip install -U cookiecutter

Or, if using Conda::

    $ conda install -c conda-forge cookiecutter

Generate a Python package project::

    $ cookiecutter https://github.com/Ouranosinc/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Install the development requirements into an environment::

    $ pip install -e ".[dev]"

Or, if using Conda::

    $ conda env create -f environment-dev.yml
    $ pip install -e . --no-deps

* `Register your project with PyPI <https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives>`_.
* Enable GitHub Actions and Workflows (see below).
* Activate automated deployment with `Trusted Publishing`_ to PyPI when you push a new tag to the `main` branch.
* Add the repo to your `Read the Docs`_ account and turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to `main`.
* Update the `dependencies` field of your `pyproject.toml` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`_.
* Register your project with `pre-commit.ci`_.
* Activate `dependabot`_ for your project.

For more details, see the `cookiecutter-pypackage tutorial`_.

GitHub Actions
~~~~~~~~~~~~~~

In order to use GitHub Actions, you will need to enable them in your repo. To do so, go to the `Actions` tab of your repo and click the green button to enable them. Afterwards, you will need to ~generate a few Personal Access Tokens (PATs) <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`_ to allow the workflows to run. To do so, go to the `Settings` tab of your repo and click on `Secrets` in the left sidebar. Then, click on the `New repository secret` button and add the following secrets:

* `BUMP_VERSION_TOKEN` with the following privileges:
    - Contents: Read and Write
    - Metadata: Read-Only
    - Pull Requests: Read and Write

* `OPENSSF_SCORECARD_TOKEN` with the following privileges:
    - Administration: Read-Only
    - Metadata: Read-Only
    - Webhooks: Read-Only

Trusted Publishing
~~~~~~~~~~~~~~~~~~

For Trusted Publishing with PyPI_ and TestPyPI_, you will need to create deployment environments in your repo. To do so, go to the `Settings` tab of your repo and click on `Environments` in the left sidebar. Then, click on the `New environment` button and add the following environments:

* `staging`
* `production`

Afterwards, you will need to configure your project on both PyPI_ and TestPyPI_ to accept uploads from GitHub Actions. To do so, go to the `Manage` tab of your project on PyPI and click on `Publishing` in the left sidebar. Then, click on the `Add a new publisher` button and fill in the following information:

* Owner: `my_username`
* Repository name: `my_project`
* Workflow name:
    * For TestPyPI: `tag-testpypi.yml`
    * For PyPI: `publish-pypi.yml`
* Environment name:
    * For TestPyPI: `staging`
    * For PyPI: `production`

Once this is configured, all you need to do is push a new tag to the `main` branch and your package will be automatically published to TestPyPI_, while performing a release on GitHub will then trigger an upload to PyPI_.

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `Nekroze/cookiecutter-pypackage`_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and ``setup.py`` differences.

* `tony/cookiecutter-pypackage-pythonic`_: Fork with py2.7+3.3 optimizations.
  Flask/Werkzeug-style test runner, ``_compat`` module and module/doc conventions.
  See ``README.rst`` or the `GitHub comparison view`_ for an exhaustive list of
  additions and modifications.

* `ardydedase/cookiecutter-pypackage`_: A fork with separate requirements files rather than a requirements list in the ``setup.py`` file.

* `lgiordani/cookiecutter-pypackage`_: A fork of Cookiecutter that uses Punch_ instead of bump2version_ and with separate requirements files.

* `briggySmalls/cookiecutter-pypackage`_: A fork using Poetry_ for neat package management and deployment, with linting, formatting, no makefiles and more.

* `veit/cookiecutter-namespace-template`_: A cookiecutter template for python modules with a namespace

* `zillionare/cookiecutter-pypackage`_: A template containing Poetry_, Mkdocs_, Github CI and many more. It's a template and a package also (can be installed with `pip`)

* `waynerv/cookiecutter-pypackage`_: A fork using Poetry_, Mkdocs_, Pre-commit_, Black_ and Mypy_. Run test, staging and release workflows with GitHub Actions, automatically generate release notes from CHANGELOG.

* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this to create your own version. Or create your own; it doesn't strictly have to be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they make my own packaging experience better.


.. _Black: https://black.readthedocs.io/en/stable/
.. _Conda: https://docs.conda.io/en/latest/
.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _GitHub Actions: https://docs.github.com/en/actions
.. _Mkdocs: https://pypi.org/project/mkdocs/
.. _Mypy: https://mypy.readthedocs.io/en/stable/
.. _Poetry: https://python-poetry.org/
.. _Punch: https://github.com/lgiordani/punch
.. _Read the Docs: https://readthedocs.io/
.. _SemVer-2.0-compliant: https://semver.org/spec/v2.0.0.html
.. _Sphinx: http://sphinx-doc.org/
.. _Tox: http://testrun.org/tox/
.. _bump-my-version: https://github.com/callowayproject/bump-my-version
.. _bump2version: https://github.com/c4urself/bump2version
.. _cookiecutter-pypackage tutorial: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
.. _dependabot: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates
.. _flit: https://flit.pypa.io/en/stable/
.. _pre-commit.ci: https://pre-commit.ci/
.. _pre-commit: https://pre-commit.com/
.. _pypi: https://pypi.org/
.. _pyproject.toml: https://www.python.org/dev/peps/pep-0518/
.. _pyup.io: https://pyup.io/
.. _sphinx-intl: https://sphinx-intl.readthedocs.io/en/master/
.. _testpypi: https://test.pypi.org/

.. _GitHub comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
.. _Nekroze/cookiecutter-pypackage: https://github.com/Nekroze/cookiecutter-pypackage
.. _ardydedase/cookiecutter-pypackage: https://github.com/ardydedase/cookiecutter-pypackage
.. _briggySmalls/cookiecutter-pypackage: https://github.com/briggySmalls/cookiecutter-pypackage
.. _family tree: https://github.com/audreyr/cookiecutter-pypackage/network/members
.. _lgiordani/cookiecutter-pypackage: https://github.com/lgiordani/cookiecutter-pypackage
.. _network: https://github.com/audreyr/cookiecutter-pypackage/network
.. _tony/cookiecutter-pypackage-pythonic: https://github.com/tony/cookiecutter-pypackage-pythonic
.. _veit/cookiecutter-namespace-template: https://github.com/veit/cookiecutter-namespace-template
.. _waynerv/cookiecutter-pypackage: https://waynerv.github.io/cookiecutter-pypackage/
.. _zillionare/cookiecutter-pypackage: https://zillionare.github.io/cookiecutter-pypackage/

.. |build| image:: https://github.com/Ouranosinc/cookiecutter-pypackage/actions/workflows/main.yml/badge.svg
    :target: https://github.com/Ouranosinc/cookiecutter-pypackage/actions/workflows/main.yml
    :alt: Build Status

.. |docs-upstream|  image:: https://readthedocs.org/projects/cookiecutter-pypackage/badge/?version=latest
    :target: https://cookiecutter-pypackage.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |pyup-upstream| image:: https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/shield.svg
    :target: https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/
    :alt: Updates
