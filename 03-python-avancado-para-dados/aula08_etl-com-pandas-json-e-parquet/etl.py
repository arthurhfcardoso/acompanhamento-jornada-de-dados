from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def load_json(paths: str | Path | Iterable[str | Path]) -> pd.DataFrame:
    """Load one or more JSON files into a single DataFrame."""
    if isinstance(paths, (str, Path)):
        paths = [paths]
    frames = [pd.read_json(Path(p)) for p in paths]
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def transform_df(df: pd.DataFrame) -> pd.DataFrame:
    """Apply a simple, generic transformation to standardize data."""
    if df.empty:
        return df
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    object_cols = df.select_dtypes(include=["object"]).columns
    for col in object_cols:
        df[col] = df[col].map(lambda v: v.strip() if isinstance(v, str) else v)
    return df


def save_csv(df: pd.DataFrame, output_path: str | Path) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def save_parquet(df: pd.DataFrame, output_path: str | Path) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)
