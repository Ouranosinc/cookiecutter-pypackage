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
   modules
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}changes

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
