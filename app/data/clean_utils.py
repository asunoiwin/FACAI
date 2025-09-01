"""Data cleaning utilities."""

import pandas as pd


def fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values forward then backward."""
    return df.fillna(method="ffill").fillna(method="bfill")


def adjust_prices(df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for price adjustment/stock splits."""
    # TODO: implement real adjustment logic
    return df


__all__ = ["fill_missing", "adjust_prices"]
