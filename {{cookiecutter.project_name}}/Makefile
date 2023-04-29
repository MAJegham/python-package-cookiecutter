# Makefile

# Settings
###################################################################################################
.ONESHELL:
.DEFAULT_GOAL := help

# Environment variables
VENV_NAME ?= venv
VENV_PYTHON ?= $(VENV_NAME)/bin/python
SYS_PYTHON ?= python3
SYS_PIP ?= pip

# Install extra requirements
EXTRAS := [dev,deploy]

# Package settings
DIST_DIR := dist
DIST_REPO := testpypi # the deployment token or credentials should be set in home/.pypirc

# Utilities
###################################################################################################

ifeq ($(OS),Windows_NT)
	DETECTED_OS := Windows
else
	DETECTED_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
endif
ifeq ($(DETECTED_OS),Unknown)
	echo "Unknown OS" && exit 1
endif

VENV_ACTIVATE := . $(VENV_NAME)/bin/activate

PARENT_VENV = $(if $(VIRTUAL_ENV), $(shell basename $(value VIRTUAL_ENV))," ")

# Targets
###################################################################################################

.PHONY: help \
		clean-venv set-venv check-inactive-venv \
			$(VENV_ACTIVATE)
		lint black black-diff black-format \
		test cover \
		build deploy e-install \
		clean clean-build clean-pyc clean-test

# help
#########################################

help: ## prints the help
	@echo "this Makefile provides helpers to launch python development utilities and commands."
	@echo "Please use \`make <target>\` where target is one of the following:"
	@awk -F  ':|##' '/^[a-zA-Z-]+: [a-zA-Z- ]*## (.+)/ { print $$1 " : " $$3; }' $(MAKEFILE_LIST)

# environment setting
#########################################

check-inactive-venv: ##_ exits if a virtual env is active
ifneq ($(PARENT_VENV)," ")
	@echo "current active virtual environment (in make's parent shell) :" $(PARENT_VENV)
	@echo "deactivate the current virtual environment before setting the new one!"
	exit 1
endif

clean-venv: check-inactive-venv ## removes the virtual environment
	rm -r $(VENV_NAME)
	@echo cleaned $(VENV_NAME)

set-venv: check-inactive-venv ## creates the virtual environment and install the developped package in editable mode
	$(MAKE) clean-venv
	$(SYS_PYTHON) -m venv $(VENV_NAME)
	$(MAKE) e-install

e-install: check-inactive-venv ## installs the package from source in editable mode
	$(VENV_ACTIVATE)
	$(VENV_PYTHON) -m pip install -e .$(EXTRAS)

# linting and code quality
#########################################

lint: check-inactive-venv ## run pylint on sources and tests
	$(VENV_ACTIVATE)
	$(VENV_PYTHON) -m pylint --exit-zero src tests

{% if cookiecutter.use_black == 'y' -%}
black: check-inactive-venv ## check style with black printing name of files that require updates
	$(VENV_ACTIVATE)
	$(VENV_PYTHON) -m black --check src tests || exit 0

black-diff: check-inactive-venv ## checks style with black printing the changes that would be produced
	$(VENV_ACTIVATE)
	$(VENV_PYTHON) -m black --diff src tests || exit 0

black-format: check-inactive-venv ## checks style with black and apply required file changes
	$(VENV_ACTIVATE)
	$(VENV_PYTHON) -m black src tests || exit 0
{%- endif %}

{% if cookiecutter.use_isort == 'y' -%}
isort: check-inactive-venv ## format imports
	$(VENV_ACTIVATE)
	$(VENV_PYTHON) -m isort src tests || exit 0
{%- endif %}

# testing
#########################################

test: check-inactive-venv ## run pytest
	$(VENV_ACTIVATE)
	$(VENV_PYTHON) -m pytest

{% if cookiecutter.use_cover == 'y' -%}
cover: check-inactive-venv ## produce covr reports with pytest
	$(VENV_ACTIVATE)
	$(VENV_PYTHON) -m pytest --cov src --cov-report html --cov-report term
	open htmlcov/index.html
{%- endif %}

# packaging
#########################################

build: check-inactive-venv clean ## builds source and wheel package
	$(VENV_ACTIVATE)
	$(VENV_PYTHON) -m build
	ls -l $(DIST_DIR)

deploy: check-inactive-venv ##_ deploys the python package to a PyPI-like server
	$(VENV_ACTIVATE)
	twine check dist/*
	twine upload --repository $(DIST_REPO) dist/*

# cleaning
#########################################

clean-build: ## remove build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.egg-info' -exec rm -rf {} +

clean-pyc: ## remove python comiled and cached artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache

clean: clean-build clean-pyc clean-test ## removes all build, python cache and test artifacts
