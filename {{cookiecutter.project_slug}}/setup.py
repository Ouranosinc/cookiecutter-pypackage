#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [{%- if cookiecutter.command_line_interface|lower == 'click' %}"Click>=8.0"{%- endif -%}]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}"pytest>=3"{%- endif -%}]

docs_requirements = [{%- if cookiecutter.make_docs ==  'y' %}
    dependency for dependency in open("requirements_docs.txt").readlines()
{% endif -%}]

dev_requirements = [
    dependency for dependency in open("requirements_dev.txt").readlines()
]

{%- set license_classifiers = {
    'MIT': 'License :: OSI Approved :: MIT License',
    'BSD-3-Clause': 'License :: OSI Approved :: BSD License',
    'ISC': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache-2.0': 'License :: OSI Approved :: Apache Software License',
    'GPL-3.0-or-later': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main",
        ],
    },
    {%- endif %}
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages(include=["{{ cookiecutter.project_slug }}", "{{ cookiecutter.project_slug }}.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={
        {% if cookiecutter.make_docs ==  'y' -%}
        "docs": docs_requirements,{%- endif %}
        "dev": dev_requirements,
    },
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    zip_safe=False,
)
