from __future__ import annotations

from pathlib import Path

import pandas as pd


def build_gains_table(df: pd.DataFrame, target_col: str, score_col: str, bins: int = 10) -> pd.DataFrame:
    """Simple gains table example."""
    df = df.copy()
    df["score_bin"] = pd.qcut(df[score_col], q=bins, duplicates="drop")
    grouped = df.groupby("score_bin", observed=True)[target_col].agg(["count", "sum"])
    grouped.rename(columns={"sum": "events"}, inplace=True)
    grouped["non_events"] = grouped["count"] - grouped["events"]
    return grouped.reset_index()


def main() -> None:
    input_path = Path("data/oot/oot_scored.parquet")
    output_path = Path("data/oot/oot_gains_table.parquet")

    df = pd.read_parquet(input_path)
    gains = build_gains_table(df, target_col="target", score_col="score", bins=10)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    gains.to_parquet(output_path)


if __name__ == "__main__":
    main()
