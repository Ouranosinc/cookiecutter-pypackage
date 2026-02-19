{% set line = 'Welcome to ' ~ cookiecutter.project_name ~ '\'s documentation!' -%}
{{ line }}
{% set underline = '=' * line|length -%}
{{ underline }}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation
   usage
   contributing
   releasing
{%- if cookiecutter.create_author_file == 'y' %}
   authors
{%- endif %}
   changelog

.. toctree::
   :maxdepth: 1
   :caption: All Modules

   apidoc/modules

.. toctree::
   :caption: GitHub Repository

   {{ cookiecutter.github_username }}/{{ cookiecutter.project_name.replace(' ', '-') }} <{{ cookiecutter.__gh_slug }}>

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
