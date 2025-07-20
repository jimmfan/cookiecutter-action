PROJECT={{cookiecutter.project_name}}
VERSION=0.1.0
PYTHON_VERSION={{cookiecutter.python_version}}
SOURCE_OBJECTS=src tests

# Detect OS using uname
UNAME := $(shell uname -s)

# Set Python and activation path based on platform
ifeq ($(filter Linux Darwin,$(UNAME)),$(UNAME))
	ACTIVATE := .venv/bin/activate
endif

ifneq ($(filter MINGW MSYS CYGWIN,$(UNAME)),)
	ACTIVATE := .venv/Scripts/activate
endif

# Default target
.DEFAULT_GOAL := help

.PHONY: help setup install run format lint test clean debug ensure-uv

# Help message
help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Ensure uv is installed globally
ensure-uv:  ## Ensure uv is installed globally
	@which uv >/dev/null 2>&1 || (echo "Installing uv..." && pip install uv)

# Setup project: create venv, install pip & dependencies
setup: ensure-uv  ## Create virtual environment and install dependencies
	@echo "Detected OS: $(UNAME)"
	uv venv .venv
	. $(ACTIVATE) && uv pip install --upgrade pip && uv pip install -e . --extra dev

# Install dependencies only (assumes venv is created)
install:  # Install project in editable mode with extra dev
	. $(ACTIVATE) && uv pip install -e . --extra dev

# Run main entry point
run:  ## Run main pipeline
	. $(ACTIVATE) && python src/main.py

# Format code
format:  ## Format code with black
	black $(SOURCE_OBJECTS)

# Lint code
lint:  ## Lint code with ruff
	ruff check src tests

# Run unit tests
test:  ## Run tests with pytest
	. $(ACTIVATE) && pytest tests

# Clean artifacts and virtual environment
clean:  ## Remove build artifacts, caches, and venv
	rm -rf .venv .mypy_cache .pytest_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -r {} +

format: 
	uvx ruff format

lints: 
	uvx ruff check --fix ${SOURCE_OBJECTS}

test.coverage: test
	