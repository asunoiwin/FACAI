# facai-ai-orchestrator

Scaffold project for a RAG‑powered quantitative research assistant.  It wires
AKShare for data collection, Qlib for factor analysis/backtesting and Ark API
for knowledge‑base chat.  The repository only contains lightweight mocks so it
can run without external keys.

## Installation

Requirements are intentionally minimal.  Install dependencies and create a
local environment file to configure the Ark client and runtime behaviour:

```bash
pip install -r requirements.txt
cp .env.example .env  # then edit to add your own API settings
```

## Configuration

All settings are loaded via `pydantic` models from the `.env` file.  Important
variables include `ARK_API_BASE`, `ARK_API_KEY`, `ARK_DEFAULT_MODEL` and
`ARK_KB_ID` alongside runtime knobs such as `TIMEOUT`, `MAX_RETRIES` and
`LOG_LEVEL`.

## CLI Usage

The Typer based CLI exposes convenience commands for knowledge‑base management
and research execution:

```bash
python -m cli.facai kb create --name stock-kb
python -m cli.facai research "分析600519.SH近三年的均线策略"
```

## FastAPI

Run the web service locally for HTTP access to `/chat` and `/research`
endpoints:

```bash
uvicorn web.main:app --reload
```

Example request:

```bash
curl -X POST http://localhost:8000/research -H 'Content-Type: application/json' \
  -d '{"query":"分析贵州茅台"}'
```

## Development

- `make run` – start FastAPI server
- `make test` – run tests
