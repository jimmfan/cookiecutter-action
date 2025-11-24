# {{ cookiecutter.project_name }}

Author: {{ cookiecutter.author }}  
Email: {{ cookiecutter.email }}

## Layout

- Library code: `src/{{ cookiecutter.package_name }}/`
- Jobs: `jobs/`
- Config: `config/`
- Tests: `tests/`
- Devcontainer: `.devcontainer/`
- Copilot configuration: `.github/`

## Quickstart

```bash
uv sync
uv run pytest
```

To work in a devcontainer (VS Code or Codespaces), open the folder and reopen in container.
