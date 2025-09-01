"""Qlib analysis helpers (mocked)."""

from __future__ import annotations

import logging
from typing import Dict, Iterable, List, Tuple

import pandas as pd

logger = logging.getLogger(__name__)


def run_factor_analysis(df: pd.DataFrame, factors: Iterable[str] | None = None) -> Tuple[Dict[str, float], pd.DataFrame]:
    """Run factor analysis using Qlib.

    In this placeholder implementation, we compute simple momentum as example and
    return mock metrics.
    """

    logger.info("Running mock factor analysis")
    df = df.copy()
    df["momentum"] = df["close"].pct_change().rolling(5).mean()
    metrics = {"IC": df["momentum"].corr(df["close"].pct_change())}
    return metrics, df


def backtest_strategy(features: pd.DataFrame, label: str) -> Tuple[Dict[str, float], pd.DataFrame]:
    """Run backtest on provided features.

    This mock computes cumulative returns and returns simple performance metrics.
    """

    logger.info("Running mock backtest")
    returns = features[label].fillna(0)
    equity = (1 + returns).cumprod()
    sharpe = returns.mean() / (returns.std() + 1e-9) * (252 ** 0.5)
    max_drawdown = (equity.cummax() - equity).max()
    metrics = {"sharpe": float(sharpe), "max_drawdown": float(max_drawdown)}
    return metrics, pd.DataFrame({"equity": equity})


__all__ = ["run_factor_analysis", "backtest_strategy"]
