"""Ark API client placeholders."""

from __future__ import annotations

import logging
from typing import Any, Dict, Iterable, Optional

import requests

from app.config import config

logger = logging.getLogger(__name__)


class ArkClient:
    """Minimal client wrapping Ark API endpoints.

    All network calls are mocked for offline usage. Replace TODO sections with
    real requests when integrating with the actual Ark API.
    """

    def __init__(self, api_base: Optional[str] = None, api_key: Optional[str] = None):
        self.ai_cfg = config.get("ai", {})
        self.api_base = api_base or self.ai_cfg.get("base_url", "https://ark.example.com")
        self.api_key = api_key or self.ai_cfg.get("api_key", "")
        self.session = requests.Session()

    # Knowledge base management -------------------------------------------------
    def create_kb(self, name: str, desc: str = "") -> Dict[str, Any]:
        """Create a knowledge base. Returns mock response."""
        logger.info("Mock create_kb called: %s", name)
        # TODO: implement API call
        return {"kb_id": "mock-kb-id", "name": name, "desc": desc}

    def upsert_document(self, kb_id: str, file: Optional[str] = None, text: str = "") -> Dict[str, Any]:
        """Upload or update a document in the KB."""
        logger.info("Mock upsert_document in %s", kb_id)
        # TODO: implement API call with file or text
        return {"kb_id": kb_id, "status": "mock-upserted"}

    def search(self, kb_id: str, query: str, top_k: int = 5) -> Dict[str, Any]:
        """Search KB and return top results."""
        logger.info("Mock search in %s: %s", kb_id, query)
        # TODO: implement API call
        return {"kb_id": kb_id, "query": query, "results": ["mock result"]}

    # Chat ---------------------------------------------------------------------
    def chat(
        self,
        messages: Iterable[Dict[str, str]],
        model: Optional[str] = None,
        kb_context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, str]:
        """Send chat messages to Ark model.

        In this mock implementation, we simply echo the last user message.
        """

        model = model or self.ai_cfg.get("provider", "mock-model")
        logger.info("Mock chat with model %s", model)
        last = list(messages)[-1]["content"] if messages else ""
        if kb_context:
            last += f" | context: {kb_context.get('results')}"
        # TODO: implement API call
        return {"reply": f"mock-response: {last}"}


__all__ = ["ArkClient"]
