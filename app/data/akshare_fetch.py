"""Data fetching utilities using AKShare."""

from __future__ import annotations

import logging

import pandas as pd

from app.utils.deps import ensure_package

logger = logging.getLogger(__name__)


def fetch_daily(code: str, start: str, end: str) -> pd.DataFrame:
    """Fetch daily bar data for a symbol using AKShare.

    This function no longer returns mock data when AKShare is unavailable. If
    the ``akshare`` package is missing or data retrieval fails, a
    ``RuntimeError`` is raised instead, guiding the caller to address the
    dependency or network issue.
    """

    ensure_package("akshare", "1.9.3")
    try:
        import akshare as ak  # type: ignore
    except Exception as exc:  # pragma: no cover - import error
        raise RuntimeError("无法导入 akshare，请先安装或检查环境。") from exc

    logger.info("Fetching data from AKShare for %s", code)
    try:
        df = ak.stock_zh_a_hist(
            symbol=code, period="daily", start_date=start, end_date=end
        )
        df.rename(columns={"日期": "date", "收盘": "close"}, inplace=True)
        df["date"] = pd.to_datetime(df["date"])
        return df[["date", "close"]]
    except Exception as exc:  # pragma: no cover - network dependent
        raise RuntimeError(
            "无法获取行情数据，请确认已安装 akshare 且网络可用。"
        ) from exc


__all__ = ["fetch_daily"]
