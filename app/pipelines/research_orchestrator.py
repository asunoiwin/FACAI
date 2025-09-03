"""Orchestrates AKShare data fetching, Qlib analysis and AI summarisation."""

from __future__ import annotations

import re
from datetime import datetime, timedelta
from typing import Dict

from app.clients.ark_client import ArkClient
from app.data.akshare_fetch import fetch_daily
from app.data.clean_utils import fill_missing, adjust_prices
from app.rag.prompt_templates import quant_research_template
from app.research.qlib_runner import run_factor_analysis, backtest_strategy
from app.settings import settings


def parse_code(query: str) -> str | None:
    match = re.search(r"\b\d{6}\.\w{2}\b", query)
    if match:
        return match.group(0)
    return None


def run_research(query: str) -> Dict[str, object]:

    """Execute research pipeline from natural language instruction.

    If any stage fails (e.g. missing dependencies or network issues), the
    error message is returned instead of continuing with subsequent steps.
    """


    code = parse_code(query) or "000001.SZ"
    end = datetime.today()
    start = end - timedelta(days=365 * 3)


    try:
        df = fetch_daily(
            code, start.strftime("%Y%m%d"), end.strftime("%Y%m%d")
        )
        df = fill_missing(adjust_prices(df))
        factor_metrics, features = run_factor_analysis(df)
        bt_metrics, equity = backtest_strategy(features, label="momentum")
    except Exception as exc:
        return {"error": str(exc)}

    client = ArkClient()
    prompt = quant_research_template(
        {"code": code}, {**factor_metrics, **bt_metrics}
    )
    ai_resp = client.chat(
        [{"role": "user", "content": prompt}],
        model=settings.ARK_DEFAULT_MODEL,
    )

    summary = ai_resp.get("reply", "")

    return {
        "code": code,
        "factor_metrics": factor_metrics,
        "bt_metrics": bt_metrics,
        "summary": summary,
        "equity": equity,
    }


__all__ = ["run_research"]
