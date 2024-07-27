# Cookiecutter DS Template

## What is this?

A quick cookie-cutter template that has linting, formatting, and testing with pytest built in.  Used to kickstart my ds/ml projects.

## How Do I Use This?

### Prereqs

Install [Cookiecutter][16]:

```shell
pip install cookiecutter
```

(_Optional_) Install [Just][15].  Follow the guide for your OS in the docs.

### Get the Template

Use the `cookiecutter` command to create the template, filling in the values as you'd like.

```shell
cookiecutter ssh://git@github.com/jsal13/cookiecutter-dstemplate.git
```

### Use it

Go into the root of the cloned repo and run:

```shell
just env  
```

Then go into your IDE and code some stuff up!

[15]: <https://github.com/casey/just> "Just"
[16]: <https://cookiecutter.readthedocs.io/en/stable/> "Cookiecutter"
