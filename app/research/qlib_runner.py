"""Qlib analysis helpers (mocked)."""

from __future__ import annotations

import logging
from typing import Dict, Iterable, Tuple

import pandas as pd

from app.utils.deps import ensure_package

logger = logging.getLogger(__name__)


def run_factor_analysis(
    df: pd.DataFrame, factors: Iterable[str] | None = None
) -> Tuple[Dict[str, float], pd.DataFrame]:
    """Run factor analysis using Qlib.

    The function ensures ``pyqlib`` is available and initialised. If the package
    cannot be imported or initialisation fails, a ``RuntimeError`` is raised.
    Currently a simple momentum example is computed to demonstrate the flow.
    """

    ensure_package("pyqlib", "0.8.6")
    try:
        import qlib
    except Exception as exc:  # pragma: no cover - import error
        raise RuntimeError("无法导入 pyqlib，请先安装或检查环境。") from exc

    qlib.init()
    logger.info("Running factor analysis")
    df = df.copy()
    df["momentum"] = df["close"].pct_change().rolling(5).mean()
    metrics = {"IC": df["momentum"].corr(df["close"].pct_change())}
    return metrics, df


def backtest_strategy(
    features: pd.DataFrame, label: str
) -> Tuple[Dict[str, float], pd.DataFrame]:
    """Run backtest on provided features using Qlib.

    ``pyqlib`` is required; missing dependencies raise ``RuntimeError``. A
    simplified performance calculation is provided for demonstration.
    """

    ensure_package("pyqlib", "0.8.6")
    try:
        import qlib
    except Exception as exc:  # pragma: no cover - import error
        raise RuntimeError("无法导入 pyqlib，请先安装或检查环境。") from exc

    qlib.init()
    logger.info("Running backtest")
    returns = features[label].fillna(0)
    equity = (1 + returns).cumprod()
    sharpe = returns.mean() / (returns.std() + 1e-9) * (252 ** 0.5)
    max_drawdown = (equity.cummax() - equity).max()
    metrics = {"sharpe": float(sharpe), "max_drawdown": float(max_drawdown)}
    return metrics, pd.DataFrame({"equity": equity})


__all__ = ["run_factor_analysis", "backtest_strategy"]
