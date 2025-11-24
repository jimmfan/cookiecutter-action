from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def load_csv(path: str | Path, **read_kwargs: Any) -> pd.DataFrame:
    """Load a CSV into a DataFrame."""
    return pd.read_csv(path, **read_kwargs)


def write_parquet(df: pd.DataFrame, path: str | Path, **to_parquet_kwargs: Any) -> None:
    """Write a DataFrame to Parquet."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, **to_parquet_kwargs)
