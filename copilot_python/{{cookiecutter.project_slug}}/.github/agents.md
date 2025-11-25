# GitHub Copilot – Agents Guide

## Build & Test

- Install dependencies: `uv sync`
- Run tests: `uv run pytest`
- Optional linting (if configured): `uv run ruff check .`

## Structure

- Library code: `src/{{ cookiecutter.package_name }}/`
- Jobs: `jobs/`
- Config: `config/`
- Tests: `tests/`

## Safe Tasks for Agents

- Refactor Python modules under `src/`.
- Add or update tests under `tests/`.
- Add new jobs following existing patterns.
- Improve documentation in `README.md`.

## Requires Human Review

- Changes to production SQL or Snowflake schemas.
- Changes to model contracts or public interfaces.
- Modifications to job schedules or side-effectful behavior.
