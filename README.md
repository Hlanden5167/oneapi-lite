# oneapi-lite

Small LLM proxy: cache, health check, latency logging

Small but I use it weekly.

## What it does

- SHA-256 keyed in-memory response cache
- POST /v1/chat with prompt/model/max_tokens
- Latency measured and returned per request
- Provider SDK plugs into one function

## Install

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Usage

```bash
curl localhost:8000/v1/chat \
  -H 'content-type: application/json' \
  -d '{"prompt": "hello", "model": "gpt-4o-mini"}'
```

## Project structure

```text
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── bug_report.md
│   └── dependabot.yml
├── docs/
│   ├── roadmap.md
│   └── usage.md
├── tests/
│   └── test_smoke.py
├── .editorconfig
├── .gitattributes
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── main.py
└── requirements.txt
```

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

## License

MIT - see [LICENSE](LICENSE).
