applyTo:
  - "src/**/features/**"
  - "jobs/features/**"

# Instructions for Feature Logic

- Source-of-truth for features and dtypes is `config/features.yaml`.
- Keep feature transformations deterministic and testable.
- Use `write_*_features.py` for jobs that persist feature tables.
- Avoid mixing heavy business logic directly in jobs; call functions from `src/{{ cookiecutter.package_name }}/`.
