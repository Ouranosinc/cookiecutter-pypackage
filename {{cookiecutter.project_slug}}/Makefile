.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint lint/flake8
        {%- if cookiecutter.use_black == 'y' %} lint/black{% endif %}
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

{%- if cookiecutter.make_docs == 'y' and cookiecutter.add_translations == 'y' %}
LOCALES := docs/locales
{%- endif %}

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

{%- if cookiecutter.make_docs == 'y' %}

clean-docs: ## remove docs artifacts
	rm -f docs/apidoc/{{ cookiecutter.project_slug }}*.rst
	rm -f docs/apidoc/modules.rst
	{%- if cookiecutter.add_translations == 'y' %}
	rm -fr docs/locales/fr/LC_MESSAGES/*.mo
	{%- endif %}
	$(MAKE) -C docs clean

{% endif -%}
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint/flake8: ## check style with flake8
	ruff {{ cookiecutter.project_slug }} tests
	flake8 --config=.flake8 {{ cookiecutter.project_slug }} tests

{% if cookiecutter.use_black == 'y' -%}
lint/black: ## check style with black
	black --check {{ cookiecutter.project_slug }} tests
	blackdoc --check {{ cookiecutter.project_slug }} docs
	isort --check {{ cookiecutter.project_slug }} tests

{% endif -%}
lint: lint/flake8{%- if cookiecutter.use_black == 'y' %} lint/black{%- endif %} ## check style

test: ## run tests quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	python -m pytest
{%- else %}
	coverage run
{%- endif %}

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	coverage run --source {{ cookiecutter.project_slug }} -m pytest
{%- else %}
	coverage run --source {{ cookiecutter.project_slug }} -m unittest discover -s tests/
{%- endif %}
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

{%- if cookiecutter.make_docs == 'y' %}
{%- if cookiecutter.add_translations == 'y' %}
initialize-translations: clean-docs ## initialize translations, ignoring autodoc-generated files
	${MAKE} -C docs gettext
	sphinx-intl update -p docs/_build/gettext -d docs/locales -l fr
{%- endif %}

autodoc: clean-docs ## create sphinx-apidoc files:
	sphinx-apidoc -o docs/apidoc --private --module-first {{ cookiecutter.project_slug }}

linkcheck: autodoc ## run checks over all external links found throughout the documentation
	$(MAKE) -C docs linkcheck

docs: autodoc ## generate Sphinx HTML documentation, including API docs
{%- if cookiecutter.add_translations == 'y' %}
	$(MAKE) -C docs html BUILDDIR="_build/html/en"
ifneq ("$(wildcard $(LOCALES))","")
	${MAKE} -C docs gettext
	$(MAKE) -C docs html BUILDDIR="_build/html/fr" SPHINXOPTS="-D language='fr'"
endif
ifndef READTHEDOCS
	$(BROWSER) docs/_build/html/en/html/index.html
endif
{%- else %}
	$(MAKE) -C docs html
ifndef READTHEDOCS
	$(BROWSER) docs/_build/html/index.html
endif
{%- endif %}

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

{% endif -%}
dist: clean ## builds source and wheel package
	python -m flit build
	ls -l dist

release: dist ## package and upload a release
	python -m flit publish dist/*

install: clean ## install the package to the active Python's site-packages
	python -m flit install

dev: clean ## install the package to the active Python's site-packages
	python -m flit install --symlink
