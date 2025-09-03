"""Command line interface for facai-ai-orchestrator."""

import typer

from app.clients.ark_client import ArkClient
from app.pipelines.chat_with_kb import chat_with_kb
from app.pipelines.research_orchestrator import run_research
from app.rag.kb_manager import KBManager


app = typer.Typer()
kb_app = typer.Typer()
app.add_typer(kb_app, name="kb")


@kb_app.command("create")
def kb_create(name: str, desc: str = ""):
    manager = KBManager(ArkClient())
    res = manager.create_kb(name, desc)
    typer.echo(res)


@kb_app.command("upsert")
def kb_upsert(kb_id: str = typer.Option(...), file: str = "", text: str = ""):
    manager = KBManager(ArkClient())
    res = manager.upsert_document(kb_id, file=file or None, text=text)
    typer.echo(res)


@app.command()
def chat(message: str):
    res = chat_with_kb(message)
    typer.echo(res["reply"])


@app.command()
def research(query: str):
    res = run_research(query)
    typer.echo(res["summary"])


if __name__ == "__main__":
    app()
