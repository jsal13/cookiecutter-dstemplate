# {{ cookiecutter.project_slug }}

This page serves as the homepage for {{ cookiecutter.project_slug }}.  The documentation follows the [diataxis](https://diataxis.fr/) style and is split up into four parts:

- Tutorial
- How-to Guide
- Explanation
- Reference Material

## Quickstart

1. Go to the repo root.
2. Run `just env` to create the poetry env and go into the poetry shell.
3. Develop while in the poetry shell.

To generate docs, fill in anything you'd like in the **docs** section and run `just serve-docs`.

## Commands

Look at the `justfile` to see the various available commands.

## Project layout

```text
mkdocs.yml    # The configuration file.
docs/
├── explanation.md
├── how-to-guides.md
├── index.md
├── reference.md
└── tutorials.md
```

TODO: Add the other parts.