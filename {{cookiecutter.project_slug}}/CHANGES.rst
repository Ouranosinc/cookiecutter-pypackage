=========
Changelog
=========

`Unreleased <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>`_ (latest)
====================={% for _ in cookiecutter.github_username %}={% endfor -%}{% for _ in cookiecutter.project_slug %}={% endfor -%}

{{ cookiecutter.version }} ({% now 'local' %})
{% for _ in cookiecutter.version %}-{% endfor -%}-----------

* First release on PyPI.
