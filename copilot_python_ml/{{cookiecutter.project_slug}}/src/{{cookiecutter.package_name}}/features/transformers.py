from __future__ import annotations

from typing import Optional

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class HourFromTimestamp(BaseEstimator, TransformerMixin):
    """
    Example transformer: extract hour from a timestamp column.

    Parameters
    ----------
    col : str
        Name of the input timestamp column.
    out_col : str
        Name of the output hour column.
    """

    def __init__(self, col: str, out_col: str):
        self.col = col
        self.out_col = out_col

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> "HourFromTimestamp":
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        X[self.out_col] = pd.to_datetime(X[self.col]).dt.hour.astype(np.int16)
        return X
