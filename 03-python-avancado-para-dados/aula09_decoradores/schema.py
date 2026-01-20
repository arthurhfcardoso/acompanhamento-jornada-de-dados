from __future__ import annotations

import pandas as pd
import pandera as pa


def build_schema(df: pd.DataFrame) -> pa.DataFrameSchema:
    """Infer a baseline schema from data and adjust as needed."""
    return pa.infer_schema(df)


def validate_df(
    df: pd.DataFrame, schema: pa.DataFrameSchema | None = None
) -> pd.DataFrame:
    if schema is None:
        schema = build_schema(df)
    return schema.validate(df)
