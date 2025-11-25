applyTo:
  - "src/**/features/transformers.py"

# Instructions for Custom Transformers

- Follow sklearn API: `fit`, `transform`, optional `fit_transform`.
- Keep transformers small and focused on a single responsibility.
- Ensure deterministic behavior (no hidden randomness).
- Align categorical handling with `config/features.yaml` definitions.
