"""Stock selection helpers for FACAI."""

from __future__ import annotations

from typing import Dict


def filter_by_price(quotes: Dict[str, Dict], *, min_price: float = 0.0, max_price: float = float("inf")) -> Dict[str, Dict]:
    """Filter quotes by price range.

    Args:
        quotes: Mapping of stock symbol to quote dictionaries as returned by
            :func:`facai.data_collector.fetch_stock_quote`.
        min_price: Minimum acceptable price.
        max_price: Maximum acceptable price.

    Returns:
        A new dictionary containing only the symbols whose current price is
        within the specified range.
    """

    filtered = {}
    for symbol, data in quotes.items():
        price = data.get("regularMarketPrice")
        if price is None:
            continue
        if min_price <= price <= max_price:
            filtered[symbol] = data
    return filtered
