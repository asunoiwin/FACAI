"""Retriever using ArkClient search API."""


from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - type checking import
    from app.clients.ark_client import ArkClient


class Retriever:
    def __init__(self, client: "ArkClient"):

        self.client = client

    def search(self, kb_id: str, query: str, top_k: int = 5):
        return self.client.search(kb_id, query, top_k)


__all__ = ["Retriever"]
