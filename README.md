# TelegramBotTemplate

![Ruff](https://github.com/sudoskys/TelegramBotTemplate/actions/workflows/ruff.yml/badge.svg)

## Project Description

This project is a template for creating Telegram bots using Python.

## Usage

Provide instructions on how to use your project. For example:

```shell
pip install pdm

```

- Change Configuration

```shell
nano pyproject.toml # Fix the name and email

```

### Pydantic V2

Pydantic is a library for data validation and settings management based on Python type annotations.

```shell
nano .env
```

### PM2

pm2 is a run-time and deployment management tool.

```shell
pm2 start pm2.json
pm2 monit
pm2 restart pm2.json
pm2 stop pm2.json

```

### dynaconf

dynaconf is a Python library that provides a flexible and dynamic configuration management solution for your
applications. It allows you to easily manage and access configuration settings from various sources such as environment
variables, YAML files, JSON files, INI files, and more.

### Pre-commit

pre-commit is a framework for managing and maintaining multi-language pre-commit hooks.

```shell
pre-commit install
pre-commit run --all-files

```

### PDM

pdm is a modern Python package manager with PEP 582 support.

```shell
add        # Add package(s) to pyproject.toml and install them
build      # Build artifacts for distribution
cache      # Control the caches of PDM
completion # Generate completion scripts for the given shell
config     # Display the current configuration
export     # Export the locked packages set to other formats
fix        # Fix the project problems according to the latest version of PDM
import     # Import project metadata from other formats
info       # Show the project information
init       # Initialize a pyproject.toml for PDM
install    # Install dependencies from lock file
list       # List packages installed in the current working set
lock       # Resolve and lock dependencies
publish    # Build and publish the project to PyPI
remove     # Remove packages from pyproject.toml
run        # Run commands or scripts with local packages loaded
search     # Search for PyPI packages
show       # Show the package information
sync       # Synchronize the current working set with lock file
update     # Update package(s) in pyproject.toml
use        # Use the given python version or path as base interpreter
venv       # Virtualenv management

```

## License

Provide information about the license your project is under. For example, if your project is under the MIT license, you
could include the following text:
This project is licensed under the MIT License - see the LICENSE.md file for details
