from __future__ annotations

from pathlib import Path

import pandas as pd

from {{ cookiecutter.package_name }}.utils.io import write_parquet


def write_example_features(output_path: Path) -> None:
    """Example feature-writing job."""
    # In reality, you would load from Snowflake / feature store here.
    df = pd.DataFrame(
        {
            "account_id": [1, 2, 3],
            "feature_example": [0.1, 0.5, 0.9],
        }
    )
    write_parquet(df, output_path)


def main() -> None:
    output_path = Path("data/features/example_features.parquet")
    write_example_features(output_path)


if __name__ == "__main__":
    main()
