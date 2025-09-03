"""Pipeline for knowledge-base augmented chat."""

from __future__ import annotations

from typing import Optional

from app.clients.ark_client import ArkClient
from app.rag.retriever import Retriever
from app.settings import settings


def chat_with_kb(query: str, kb_id: Optional[str] = None) -> dict:
    client = ArkClient()
    retriever = Retriever(client)
    context = None
    if kb_id or settings.ARK_KB_ID:



__all__ = ["chat_with_kb"]
