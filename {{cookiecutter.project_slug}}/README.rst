{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{%- if is_open_source %}

+----------------------------+-----------------------------------------------------+
| Versions                   | |pypi| |versions|                                   |
+----------------------------+-----------------------------------------------------+
| Documentation and Support  | |docs|                                              |
+----------------------------+-----------------------------------------------------+
{%- if is_open_source %}
| Open Source                | |license| |ossf|                                    |
+----------------------------+-----------------------------------------------------+
{%- endif %}
| Coding Standards           | |black| |ruff| |pre-commit|                         |
+----------------------------+-----------------------------------------------------+
| Development Status         | |status| |build| |coveralls|                        |
+----------------------------+-----------------------------------------------------+

{%- endif %}
{%- if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name | replace(" ", "-") }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name | replace(" ", "-") }}/
     :alt: Updates
{%- endif %}

{{ cookiecutter.project_short_description }}

{%- if is_open_source %}

* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{%- endif %}

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `Ouranosinc/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _`Ouranosinc/cookiecutter-pypackage`: https://github.com/Ouranosinc/cookiecutter-pypackage


.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black
        :alt: Python Black

.. |build| image:: {{ cookiecutter.__gh_slug }}/actions/workflows/main.yml/badge.svg
        :target: {{ cookiecutter.__gh_slug }}/actions
        :alt: Build Status

.. |coveralls| image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name | replace(" ", "-") }}/badge.svg
        :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name | replace(" ", "-") }}
        :alt: Coveralls

.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.project_name | replace(" ", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_name | replace(" ", "-") }}.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

{%- if is_open_source %}

.. |license| image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name | replace(" ", "-") }}.svg
        :target: {{ cookiecutter.__gh_slug }}/blob/main/LICENSE
        :alt: License

.. |ossf| image:: https://api.securityscorecards.dev/projects/github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name | replace(" ", "-") }}/badge
        :target: https://securityscorecards.dev/viewer/?uri=github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name | replace(" ", "-") }}
        :alt: OpenSSF Scorecard

{%- endif %}

.. |pre-commit| image:: https://results.pre-commit.ci/badge/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name | replace(" ", "-") }}/main.svg
        :target: https://results.pre-commit.ci/latest/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name | replace(" ", "-") }}/main
        :alt: pre-commit.ci status

.. |pypi| image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_name | replace(" ", "-") }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_name | replace(" ", "-") }}
        :alt: PyPI

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
        :target: https://github.com/astral-sh/ruff
        :alt: Ruff

.. |status| image:: https://www.repostatus.org/badges/latest/active.svg
        :target: https://www.repostatus.org/#active
        :alt: Project Status: Active – The project has reached a stable, usable state and is being actively developed.

.. |versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name | replace(" ", "-") }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_name | replace(" ", "-") }}
        :alt: Supported Python Versions
