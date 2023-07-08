# {{ cookiecutter.project_name }}

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## What is this?

A quick cookie-cutter template that has linting, formatting, and testing with pytest built in.

## How Do I Use This?

### Prereqs

Install [Poetry][8]:

```shell
pip install poetry
```

Install [Cookiecutter][16]:

```shell
pip install cookiecutter
```

(_Optional_) Install [Just][15].  Follow the guide for your OS in the docs.

### Get the Template

Use the `cookiecutter` command to create the template, filling in the values as you'd like.

```shell
cookiecutter https://github.com/jsal13/cookiecutter-pytemplate.git
```

### Use it.

```shell
just env  # Get into the poetry env.
```

Then go into your IDE!

[8]: <https://python-poetry.org/docs/basic-usage/> "Poetry"
[15]: <https://github.com/casey/just> "Just"
[16]: <https://cookiecutter.readthedocs.io/en/stable/> "Cookiecutter"
