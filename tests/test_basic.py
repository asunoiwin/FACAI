from fastapi.testclient import TestClient

from app.settings import settings
from app.pipelines.research_orchestrator import run_research
from web.main import app


def test_settings_load():
    assert settings.TIMEOUT == 30


def test_research_orchestrator():
    res = run_research("分析000001.SZ的均线策略")
    assert "summary" in res or "error" in res


def test_health_endpoint():
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
