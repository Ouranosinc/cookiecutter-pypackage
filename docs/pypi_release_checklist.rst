PyPI Release Checklist
======================

Before Your First Release
-------------------------

Ensure that the name you have chosen has not already been registered on PyPI. This can be performed by checking the PyPI Index (https://pypi.python.org/) or by using the following command:

.. code-block:: console

    $ pip search <package name>

For Every Release
-------------------

#. Update CHANGELOG.rst

#. Commit the changes:

   .. code-block:: console

       $ git add CHANGELOG.rst
       $ git commit -m "Changelog for upcoming release 0.1.1."

#. Update version number (can also be patch or major)

   .. code-block:: console

       $ bump-my-version minor

#. Install the package again for local development, but with the new version number:

   .. code-block:: console

       $ pip install --editable .

#. Run the tests:

   .. code-block:: console

       $ tox

#. Push the commit:

   .. code-block:: console

       $ git push

#. Push the tags, creating the new release on both GitHub and PyPI:

   .. code-block:: console

       $ git push --tags

#. Check the PyPI listing page to make sure that the README, release notes, and roadmap display properly. If not, try one of these:

    #. Copy and paste the RestructuredText into http://rst.ninjs.org/ to find out what broke the formatting.

    #. Check your long_description locally:

       .. code-block:: console

           $ pip install build flit twine
           $ python -m build --sdist --wheel
           $ python -m twine check dist/*

#. Edit the release on GitHub (e.g. https://github.com/audreyr/cookiecutter/releases). Paste the release notes into the release's release page, and come up with a title for the release.

About This Checklist
--------------------

This checklist is adapted from:

* https://github.com/audreyfeldroy/cookiecutter-pypackage

It assumes that you are using all features of Cookiecutter PyPackage.
