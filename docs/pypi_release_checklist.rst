PyPI Release Checklist
======================

Before Your First Release
-------------------------

#. Update any `[project.urls]` in ``pyproject.toml`` to match the documentation, homepage, and any other external URLs.

#. Ensure that the name you have chosen has not already been registered on PyPI. This can be performed by checking the PyPI Index (https://pypi.python.org/) or by using the following command:

   .. code-block:: console

       $ pip search <package name>

#. Create accounts at both `testpypi.org` and `pypi.org` if you don't have them.

#. On both TestPyPI and PyPI accounts go to: Publishing > Add a new pending publisher.

#. Fill in the form:
    * TestPyPI/PyPI Project Name: Your package name (e.g., my-package)
    * Owner: Your GitHub username or organization
    * Repository name: Your repo name
    * Workflow name: publish.yml
    * Environment name: 
        * TestPyPI: "staging"
        * PyPI: "production"

#. Go to Settings > Environments > New environment and create both a "staging" and "production" environments.
   Optionally add required reviewers and restrict deployments to ``v*`` tags.

For Every Release
-----------------

In a new branch based off the latest commit of `main` open a Pull Request (PR):

#. Update CHANGELOG.rst under the "unreleased" entry.

#. Commit the changes:

   .. code-block:: console

       $ git add CHANGELOG.rst
       $ git commit -m "Changelog for upcoming release 0.1.1."

#. Update (bump) the version number (by ``major``, ``minor``, or ``patch``)

   .. code-block:: console

       $ bump-my-version bump { major | minor | patch }

#. Push the commit to your branch:

   .. code-block:: console

       $ git push

#. Merge your branch to `main` and checkout the `main` branch locally.

#. Tag the last commit of `main` and push the tags, creating the new release on TestPyPI:

   .. code-block:: console

       $ git tag -s vX.Y.Z -m "vX.Y.Z (or any other message you want associated with the tag)"
       $ git push --tags

#. (Optionally) Check the TestPyPI listing page to make sure that the README, metadata URLs, and necessary package contents are all available and accurate.
   If not, try one of these:

    #. Copy and paste the RestructuredText into an RST checker (such as https://rsted.info.ucl.ac.be/) to find out what broke the formatting.

    #. Check your long_description locally:

       .. code-block:: console

           $ pip install build twine
           $ python -m build --sdist --wheel
           $ python -m twine check dist/*

#. If corrections are required, update `main` from a new Pull Request, merge and push updates to the affected tag.

#. Prepare the release on GitHub, pointing to the tagged version (e.g. https://github.com/audreyr/cookiecutter/releases).
   Paste the release notes into the release's release page. If you're feeling it, come up with a title for the release!

.. note::

    For security purposes, we recommend clicking the `Enable release immutability` checkbox in your project settings page.
    
    This prevents maintainers and administrators from modifying a tagged version once it has been formally released.
    TestPyPI and PyPI already enable this level of security by default, so any bugged/broken versions can only be removed ("yanked"), never overwritten.

About This Checklist
--------------------

This checklist is generally adapted from:

* https://github.com/audreyfeldroy/cookiecutter-pypackage

It assumes that you are using all features of the Ouranos Cookiecutter PyPackage.
