# !/usr/bin/env python

from pathlib import Path

from setuptools import setup

setup(
    name="cookiecutter-pypackage-ouranos",
    packages=[],
    version="0.1.0",
    description="Cookiecutter template for a Python package",
    long_description=Path(__file__).parent.joinpath("README.rst").read_text(),
    long_description_content_type="text/x-rst",
    author="Trevor James Smith",
    license="BSD",
    author_email="smith.trevorj@ouranos.ca",
    url="https://github.com/Ouranosinc/cookiecutter-pypackage",
    keywords=[
        "cookiecutter",
        "template",
        "package",
    ],
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],
    extras_require={
        "dev": [
            "build >=1.2.2",
            "cookiecutter >=2.6.0",
            "coverage >=7.5.1",
            "flit >=3.10.1,<4.0",
            "pre-commit >=3.5.0",
            "pytest-cookies >=0.7.0",
            "pytest >=8.2.3",
            "tox >=4.26.0",
            "twine >=5.1.1",
            "watchdog >=4.0.0",
        ],
        "docs": [
            "alabaster >=0.7.13",
            "sphinx >=7.1.0",
        ],
    },
)
