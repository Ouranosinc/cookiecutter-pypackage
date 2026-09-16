.. cookiecutter-pypackage documentation master file, created by
   sphinx-quickstart on Sun Dec 13 09:13:01 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cookiecutter PyPackage Ouranos
==============================

Why use this Cookiecutter?
--------------------------

* **Actively maintained**: This recipe receives and has been receiving regularly updates since 2022.
  Testing of the template is performed using modern Python and PyPy versions.
  It also is tested against the latest versions of linting and code formatting libraries (`ruff` and others).

* **No Frills**: Projects generated from this recipe use a handful of concise libraries that adhere to the UNIX philosophy (**"DOTADIW"**). The default configurations use:
    * **pytest** for the testing framework;
    * **tox** for build testing;
    * **sphinx** for serving documentation;
    * **make** for running tasks; and
    * **flit** for package build management.

* **Modern (not Hypermodern)**: This recipe adopts PEPs as they become available by modern tools and aims to ensure that older Python versions remain viable until their End-of-Life dates.
  The tooling used here is new but retains reasonable Python-endorsed (`pip` ) and scientific (`conda`) toolsets.
  Developers should not need to familiarize themselves with bleeding-edge packaging and dependency-management tools to get their projects up and running.

* **Fully Automated**: GitHub CI is extensively used here to ensure that dependencies are automatically kept up-to-date and that changes to core files are always accompanied by a version bump (`bump-my-version bump build`).
  For packaging deployment, Trusted Publishing is pre-configured to ensure that packages are deployed to PyPI as soon as they are released.
  Other automations include a welcome message for new contributors, Pull Request labelling, and warnings for when outside contributors touch CI files.

* **Security Practices**: All GitHub Actions and Python dependencies used in CI are pinned by their commit SHA256 sums and not their versions tags (which are mutable).
  For added CI security, mishandled CI configurations are flagged by `zizmor`, which suggests ways forward for correcting issues.
  Python linters are set up to emit errors when insecure coding practices are detected and CodeQL evaluations are run on all pushed commits.
  Automated evaluations via the Open Source Software Foundation (OpenSSF) Security Scorecard are configured from the first commit.
  Dependabot is also configured to automatically open and merge security patches to vulnerable libraries and GitHub Actions.

* **Publication-Ready**: Projects generated here come along with all necessary boilerplate to ensure they are easily citable (`CITATION.cff`) and archivable (`.zenodo.json`).
  Many of the configurations adopted here are compatible with best practices suggested by groups such as `pyOpenSci <https://www.pyopensci.org/python-packaging-science/>`_ and `JOSS <https://joss.theoj.org/>`_.

* **AI Policies**: Preconfigured options for `AGENTS.md`, `AI_POLICY.md`, and contributor guidelines for various degrees of openness to AI-based contributions.
  AI disclosures are always demanded, and Ai-tooled commits should always included an `assisted-by` in their messages.
  If you don't want any AI contributions in your project, these files and guideliens will not be added.

How to make the most of this Cookiecutter
-----------------------------------------

If your goal is to:
  - Build and maintain a scientific Python project on PyPI and `conda-forge`;
  - Ensure that your project is rigourously-tested across many different builds;
  - Adopt new PEPs as they become available to build tools.
Then, this is the template for you.

This cookiecutter is best used in conjunction with `cruft <https://cruft.github.io/cruft/>`_ for keeping your projects up-to-date.
Updates are performed on this recipe every **3-6 months**, sometimes sooner. New automations are added from time-to-time if they provide a clear benefit to many kinds of projects.
For the latest Python dependencies and GitHub Actions updates, this recipe relies on Dependabot to push updates when projects are created, so do not expect the latest versions here.

Getting Started
---------------

The :doc:`tutorial <tutorial>` is the best place to start.

.. toctree::
   :maxdepth: 2
   :hidden:

   readme
   tutorial
   prompts
   console_script_setup
   pypi_release_checklist
   troubleshooting

.. toctree::
   :caption: GitHub Repository
   :hidden:

   Ouranosinc/cookiecutter-pypackage <https://github.com/Ouranosinc/cookiecutter-pypackage>
