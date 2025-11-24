def test_smoke_import() -> None:
    # Basic smoke test to ensure package import works.
    import {{ cookiecutter.package_name }}  # noqa: F401
