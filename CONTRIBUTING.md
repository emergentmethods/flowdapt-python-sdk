# Contributor Guide

This guide is intended for developers of Flowdapt Python SDK, people who want to contribute to the Flowdapt Python SDK codebase or documentation, or people who want to understand the source code of the application they're running.

There are a few things you can do ensure your environment is ready for development on Flowdapt Python SDK. First, ensure that you have `poetry` installed on your system. For more details on how to install `poetry`, see the [Poetry documentation](https://python-poetry.org/docs/#installation).

Next, clone the repo and create the virtual environment:

```bash
git clone https://gitlab.com/emergentmethods/flowdapt-python-sdk.git
cd flowdapt-python-sdk
python3 -m venv .venv
source .venv/bin/activate
```

Then, install the dependencies:

```bash
poetry install --with dev
```

???+ note "Note"
    The `--with dev` flag is on by default, but it is good to be explicit.

Finally, install the pre-commit hooks:

```bash
pre-commit install
```

These are required to ensure that the code is formatted correctly and that the tests pass before committing. If you NEED to skip the pre-commit hooks, you can use the `--no-verify` flag when committing. However CI will still run the hooks and fail if they do not pass.

## Commit messages

Commit messages should follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification (specifically the Angular convention). This allows us to automatically generate changelogs and version numbers for releases. The commit message should be in the following format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```