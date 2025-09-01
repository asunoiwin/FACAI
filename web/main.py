"""FastAPI entry point."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from app.pipelines.chat_with_kb import chat_with_kb
from app.pipelines.research_orchestrator import run_research

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


class ResearchRequest(BaseModel):
    query: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):
    return chat_with_kb(req.message)


@app.post("/research")
def research(req: ResearchRequest):
    return run_research(req.query)


# Knowledge base endpoints ----------------------------------------------------
class KBCreateRequest(BaseModel):
    name: str
    desc: str = ""


@app.post("/kb/create")
def kb_create(req: KBCreateRequest):
    from app.rag.kb_manager import KBManager
    from app.clients.ark_client import ArkClient

    manager = KBManager(ArkClient())
    return manager.create_kb(req.name, req.desc)


class KBUpsertRequest(BaseModel):
    kb_id: str
    text: str = ""


@app.post("/kb/upsert")
def kb_upsert(req: KBUpsertRequest):
    from app.rag.kb_manager import KBManager
    from app.clients.ark_client import ArkClient

    manager = KBManager(ArkClient())
    return manager.upsert_document(req.kb_id, text=req.text)
