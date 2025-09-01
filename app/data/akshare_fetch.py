"""Data fetching utilities using AKShare."""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional

import pandas as pd

logger = logging.getLogger(__name__)


def fetch_daily(code: str, start: str, end: str) -> pd.DataFrame:
    """Fetch daily bar data for a symbol.

    This function attempts to use AKShare; if unavailable or network blocked,
    it returns a mock DataFrame with a date index and random prices.
    """

    try:
        import akshare as ak  # type: ignore

        logger.info("Fetching data from AKShare for %s", code)
        df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date=start, end_date=end)
        df.rename(columns={"日期": "date", "收盘": "close"}, inplace=True)
        df["date"] = pd.to_datetime(df["date"])
        return df[["date", "close"]]
    except Exception as exc:  # pragma: no cover - network dependent
        logger.warning("AKShare unavailable, returning mock data: %s", exc)
        dates = pd.date_range(start=start, end=end, freq="B")
        prices = pd.Series(range(len(dates)), index=dates)
        return pd.DataFrame({"date": dates, "close": prices.values})


__all__ = ["fetch_daily"]
