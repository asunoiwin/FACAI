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


    code = parse_code(query) or "000001.SZ"
    end = datetime.today()
    start = end - timedelta(days=365 * 3)

    summary = ai_resp.get("reply", "")

    return {
        "code": code,
        "factor_metrics": factor_metrics,
        "bt_metrics": bt_metrics,
        "summary": summary,
        "equity": equity,
    }


__all__ = ["run_research"]
