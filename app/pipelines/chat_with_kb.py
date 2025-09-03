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

        context = retriever.search(
            kb_id or settings.ARK_KB_ID, query, top_k=3
        )
    return client.chat(
        [{"role": "user", "content": query}],
        model=settings.ARK_DEFAULT_MODEL,
        kb_context=context,
    )



__all__ = ["chat_with_kb"]
