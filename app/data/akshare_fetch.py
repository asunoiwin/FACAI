"""Data fetching utilities using AKShare."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def fetch_daily(code: str, start: str, end: str) -> pd.DataFrame:

        )
        df.rename(columns={"日期": "date", "收盘": "close"}, inplace=True)
        df["date"] = pd.to_datetime(df["date"])
        return df[["date", "close"]]
    except Exception as exc:  # pragma: no cover - network dependent



__all__ = ["fetch_daily"]
