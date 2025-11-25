# GitHub Copilot – Project Instructions

## Project Layout
- Python `src/` layout.
- Main package: `src/{{ cookiecutter.package_name }}/`.
- Jobs: `jobs/` (features, scoring, evaluation).
- Config: `config/` (YAML).

## Coding Conventions
- Prefer functions over classes unless they provide clear benefit.
- Use verbs:
  - `load_*` for reading data
  - `write_*` for persisting tables/datasets
  - `build_*` for assembling pipelines or preprocessors
- Avoid redundant filenames when folder names already give meaning.

## Configuration & Tools
- Dependencies managed with `uv`.
- Source-of-truth for features and dtypes is `config/features.yaml`.
- Use `pytest` for tests.
- Keep Snowpark/Snowflake logic testable and separate from I/O.
