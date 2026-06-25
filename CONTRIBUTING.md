# Contributing

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt
pre-commit install
```

On macOS/Linux, activate with `source .venv/bin/activate`.

## Run the App

```bash
streamlit run app.py
```

## Quality Checks

Run the same checks used by CI:

```bash
pre-commit run --all-files
pytest --cov=. --cov-report=term-missing --cov-fail-under=75
bandit -c pyproject.toml -r .
pip-audit -r requirements.txt
```

Install native security/release CLIs separately when you want to run the full release workflow locally:

- `gitleaks` for secret scanning
- `trufflehog` for secret scanning
- `git-cliff` for changelog generation

## Commit Style

Use conventional commits so `git-cliff` can generate useful changelog entries:

```text
feat: add new placement preset
fix: handle empty AI provider response
docs: update local setup instructions
```
