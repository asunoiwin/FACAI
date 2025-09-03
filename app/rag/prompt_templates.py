"""Prompt templates for AI interactions."""

from typing import Any, Dict


def quant_research_template(
    context: Dict[str, Any], metrics: Dict[str, Any]
) -> str:
    """Build prompt for quantitative research summary."""
    return (
        "Quantitative research results for {code}. Metrics: {metrics}. "
        "Provide a short performance summary including "
        "Sharpe ratio and drawdown."
    ).format(code=context.get("code", "unknown"), metrics=metrics)


def announce_summary_template(context: str, query: str) -> str:
    """Template for summarising announcements or news."""
    return f"Given the following context: {context}. Answer the query: {query}"


__all__ = ["quant_research_template", "announce_summary_template"]
