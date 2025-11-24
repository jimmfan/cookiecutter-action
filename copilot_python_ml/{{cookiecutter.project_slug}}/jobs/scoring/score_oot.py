from __future__ import annotations

from pathlib import Path

import pandas as pd
import joblib


def load_model(model_path: Path):
    return joblib.load(model_path)


def score_oot(model_path: Path, input_path: Path, output_path: Path) -> None:
    model = load_model(model_path)
    df = pd.read_parquet(input_path)
    df["score"] = model.predict_proba(df)[:, 1]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path)


def main() -> None:
    model_path = Path("models/final_model.joblib")
    input_path = Path("data/oot/oot_features.parquet")
    output_path = Path("data/oot/oot_scored.parquet")
    score_oot(model_path, input_path, output_path)


if __name__ == "__main__":
    main()
