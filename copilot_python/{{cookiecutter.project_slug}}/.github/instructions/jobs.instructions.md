applyTo:
  - "jobs/**"

# Instructions for Job Files

- Jobs orchestrate workflows, they should be thin.
- Put reusable logic in `src/{{ cookiecutter.package_name }}/`.
- Each job should define a `main()` and:

  ```python
  if __name__ == "__main__":
      main()
  ```

- Make feature-writing jobs idempotent and safe to rerun.
- Prefer configuration via YAML files in `config/`.
