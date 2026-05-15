{% set line = 'Welcome to ' ~ cookiecutter.project_name ~ '\'s documentation!' -%}
{{ line }}
{% set underline = '=' * line|length -%}
{{ underline }}

**{{ cookiecutter.project_name }}**: {{ cookiecutter.project_short_description }}

Need help?
^^^^^^^^^^

* If you encounter any errors or problems with `{{ cookiecutter.project_name }}`, please let us know! Open an issue at the `GitHub main repository <{{ cookiecutter.__gh_slug }}>`_.
* To be aware of changes in `{{ cookiecutter.project_name }}`, feel free to “watch” the GitHub repository. You can customize the watch function to notify you of new releases or more.

Navigation
==========

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents

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
