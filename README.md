# facai-ai-orchestrator

AI orchestrator for quantitative research with AKShare, Qlib and Ark API.

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env  # fill in your Ark API settings
```

## CLI Usage

```bash
python -m cli.facai kb create --name stock-kb
python -m cli.facai research "分析600519.SH近三年的均线策略"
```

## FastAPI

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
