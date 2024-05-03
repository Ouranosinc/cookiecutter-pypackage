=========
Changelog
=========

`Unreleased <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>`_ (latest)
================================
{%- for _ in range((cookiecutter.github_username | length) + (cookiecutter.project_slug | length)) %}={% endfor -%}
=============

{{ cookiecutter.version }} ({% now 'local' %})
{% for _ in cookiecutter.version %}-{% endfor -%}-------------

* First release on PyPI.
