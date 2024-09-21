# Supplier Applications
Skeleton to be used as reference for a Python CLI application.

- [1 Prerequisites](#prerequisites)
- [2 Publish Containers](#publishing-the-image)

## Prerequisites

### PDM
This project uses [PDM][link-pdm-docs] to build and manage project dependencies. Follow the 
installation instructions using pip, and verify it's available in your environment with `pdm --help`

## Using python module
To run this python module you can execute next script
```
    pdm reference_python module_cli run_operation --param_option param_value
```
Which follows next structure:
```
    pdm {script_name} {cli-module-name} {method} --{parameter} {parameter_value} 
```
**script_name** is defined in pyproject.toml file inside tool.pdm.script section, and it's pointing to main file to be executed

**run.py** is the entrypoint that has the cli commands that can be executed. If a new command needs to be added this python
file needs to be updated with a new operation
```
    cli.add_command(run_new_operation)
```

All operations or methods are located inside cli/sub_folders 
sub_folders represent a click group module. For the current example, we have: ```reference_python_cli_app``` folder and inside it ```__init__.py```
file there are the methods available for the user to use. Those methods need to be defined as in the next example:
```
@group_module_name.command("method_name")
```

## Publishing the image
CICD naming convention: Please refer to the [Docker ADR][docker-adr]

_NOTE: Please notice that the pulling port is `18443` and the push used to push images is `18444`_

Example:
```
    <image name>:<tag>
```

## Running from Docker
Create image
```
    docker build -t reference_python:dev .
```

Run image

```
    docker run --env OPTION="ValueOption" reference_python:dev
```
## Linting 

**Note: Based off from the [Lint ADR][lint-adr]**

The tools used for this are `flake8` and `black`.

### Installing the Linting Tools

Run on your terminal:

`pip3 install flake8 &&  pip3 install black`

After installation, check the versions installed:

```
$ flake8 --version
6.0.0 (mccabe: 0.7.0, pycodestyle: 2.10.0, pyflakes: 3.0.1) CPython 3.10.6 on Linux
```

```
$ black --version
black, 23.3.0 (compiled: yes)
Python (CPython) 3.10.6
```

### Running the Linting Tools

Since every developer is responsible of the code delivered by her/him, the tools should only be applied to the new code before commiting it ideally. `flake8` should tell which files are not in compliance and `black` will adjust that for you.

```
flake8 --ignore E501,W503  < the files you edited\added >
```

This will tell you which file and lines are not in compliance. You can either manually adjust them or run: 

```
black --diff < the files you edited\added >
```

To make sure you have a clean output, You can run again: 

```
flake8 --ignore E501,W503  < the files you edited\added >
```

_Note: E501 and W503 are PEP guidelines that we ignore for the moment_

## Related
* [PDM Docs][link-pdm-docs]
* [Gitignore standard for Python][link-gitignore-python]
* [Docker ADR][docker-adr]

[link-pdm-docs]: https://pdm.fming.dev/latest
[link-gitignore-python]: https://github.com/github/gitignore/blob/main/Python.gitignore