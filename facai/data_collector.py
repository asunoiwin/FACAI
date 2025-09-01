"""Data collection utilities for FACAI.

This module contains minimal functions to fetch market and policy
information for A shares and Hong Kong stocks. The implementation uses
Yahoo Finance's public quote API via the standard library so it has no
third-party dependencies.
"""

from __future__ import annotations

import json
import logging
from typing import Dict
from urllib.request import urlopen
from urllib.parse import urlencode

YAHOO_QUOTE_URL = "https://query1.finance.yahoo.com/v7/finance/quote"


def fetch_stock_quote(symbol: str) -> Dict:
    """Fetch real-time quote for a given stock symbol.

    Args:
        symbol: Stock symbol compatible with Yahoo Finance. Examples:
            ``"000001.SS"`` for the SSE Composite Index or ``"0700.HK"`` for
            Tencent Holdings.

    Returns:
        A dictionary with quote information. The function returns an empty
        dictionary if the symbol is not found or a network error occurs.
    """

    try:
        url = f"{YAHOO_QUOTE_URL}?{urlencode({'symbols': symbol})}"
        with urlopen(url, timeout=10) as response:  # nosec B310
            payload = json.loads(response.read().decode("utf-8"))
        data = payload.get("quoteResponse", {}).get("result", [])
        if data:
            return data[0]
    except Exception as exc:  # pragma: no cover - network errors
        logging.warning("Failed to fetch quote for %s: %s", symbol, exc)
    return {}


def fetch_policy_news() -> str:
    """Placeholder for policy news scraping.

    This function should eventually scrape or query official policy and
    regulatory news relevant to A shares and Hong Kong markets. For now, it
    simply returns a static string.
    """

    return (
        "No policy news fetching implemented yet. This function acts as a "
        "placeholder to demonstrate where such logic would live."
    )
