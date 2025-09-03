"""AI integration layer for FACAI.

This module provides a minimal interface to interact with AI services
such as Volcengine's Doubao or DeepSeek. For demonstration purposes, the
functions below do not perform real API calls but illustrate the expected
interface for future expansion.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AIClient:
    """Simple AI client placeholder.

    Attributes:
        model: Name of the model being used. Supported values include
            ``"doubao"`` and ``"deepseek"``. The client does not enforce the
            model choice in this initial version.
    """

    model: str = "doubao"

    def summarize(self, text: str) -> str:
        """Return a dummy summary of ``text``.

        A real implementation would call the respective AI model's API to
        analyze the text. Here, we simply truncate the text to demonstrate
        the integration point.
        """

        if len(text) > 200:
            return text[:200] + "..."
        return text
