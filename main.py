"""Entry point for the FACAI demo application.

This script demonstrates a minimal workflow:

1. Fetch market data for a set of symbols.
2. Filter the data based on price constraints.
3. Summarise the results using the AI integration layer.

The script targets Windows execution but is cross-platform and can run on
any system with Python and network access.
"""

from __future__ import annotations

from facai.ai_integration import AIClient
from facai.data_collector import fetch_stock_quote, fetch_policy_news
from facai.stock_selector import filter_by_price


def main() -> None:
    symbols = ["000001.SS", "0700.HK"]  # SSE Composite Index and Tencent
    quotes = {sym: fetch_stock_quote(sym) for sym in symbols}

    # Simple selection: keep stocks with price between 1 and 1000
    selected = filter_by_price(quotes, min_price=1, max_price=1000)

    ai = AIClient(model="doubao")

    print("Policy News:")
    print(fetch_policy_news())
    print("\nSelected Stocks:")
    for sym, data in selected.items():
        text = f"{sym} current price is {data.get('regularMarketPrice')} {data.get('currency')}"
        summary = ai.summarize(text)
        print(f"- {summary}")


if __name__ == "__main__":
    main()
