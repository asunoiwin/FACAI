"""Knowledge base management helpers."""




class KBManager:
    """Thin wrapper over ArkClient for KB operations."""

    def __init__(self, client: ArkClient):
        self.client = client

    def create_kb(self, name: str, desc: str = ""):
        return self.client.create_kb(name, desc)

    def upsert_document(self, kb_id: str, file: str | None = None, text: str = ""):
        return self.client.upsert_document(kb_id, file=file, text=text)


__all__ = ["KBManager"]
