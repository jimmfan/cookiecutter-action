PROJECT={{cookiecutter.project_name}}
VERSION=0.1.0
PYTHON_VERSION={{cookiecutter.python_version}}
SOURCE_OBJECTS=src tests

setup: |
	curl -LsSf https://astral.sh/uv/install.sh # uvx install
	python -m pip install --upgrade pip

format: uvx ruff format

lints: uvx ruff check --fix ${SOURCE_OBJECTS}

test: setup
	# poetry run coverage run -m pytest -s .

test.coverage: test
	# poetry run coverage report -m --fail-under=90