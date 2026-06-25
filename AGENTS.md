# Agent Instructions

## Project Shape

This is a Python Streamlit app for cricket field placement recommendations.

Key files:

- `app.py` - Streamlit UI and provider controls
- `field_presets.py` - rule-based placement presets
- `field_renderer.py` - SVG field rendering
- `ai_client.py` - Ollama, BYOK, and fallback coaching helpers
- `i18n.py` - localized UI labels
- `cricket ai speckit/` - product and technical specification kit

## Working Rules

- Keep secrets out of the repo. Use `.env.example` for variable names only.
- Prefer focused tests around placement logic, prompt generation, and renderer output.
- Run `pytest --cov=. --cov-report=term-missing --cov-fail-under=75` after behavior changes.
- Run security checks before release: `gitleaks detect`, `trufflehog filesystem .`, `bandit -c pyproject.toml -r .`, and `pip-audit -r requirements.txt`.
- Do not rewrite localized content unless the task is specifically about language or encoding cleanup.
