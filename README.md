# CricField AI - Smart Cricket Field Placement Dashboard

Select a batter profile and bowler style, then get an explainable AI-assisted cricket field placement instantly.

## Features

- Interactive 2D cricket field rendered with SVG
- Rule-based AI placement engine for common batter/bowler matchups
- Explanations for each fielder position
- Multilingual UI with English as the default plus Hindi, Telugu, Bengali, and Tamil
- Local AI inference option through Ollama
- BYOK support for OpenAI-compatible chat completion APIs
- Built-in fallback coaching note so demos work without external services
- User-centric market adoption panel highlighting accessibility, cost control, and coach/captain workflows

## i18n and l10n

The app separates user-facing text from cricket placement logic:

- `i18n.py` stores translations for English, Hindi, Telugu, Bengali, and Tamil.
- English is the default language.
- Select boxes use localized labels while preserving stable internal values for the placement engine.
- Preset names, fielder names, zone labels, and fielder explanations are localized for Hindi, Telugu, Bengali, and Tamil users.
- Localized UI and coaching notes make the dashboard easier for Indian coaches, captains, academies, and young players to adopt.

## AI Options

The sidebar includes three AI modes:

- **Onboard rule-based AI**: no setup needed; uses the local placement rules and fallback coaching note.
- **Local AI via Ollama**: calls `http://localhost:11434/api/generate` by default. Change the URL/model in the sidebar.
- **BYOK OpenAI-compatible API**: enter your own API base URL, model, and token. The token is entered at runtime and is not stored in the repo.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

For Ollama mode, start Ollama separately and make sure the selected model is available:

```bash
ollama pull llama3.1
ollama serve
```

## Deploy

This is a Streamlit app, so deploy it to Streamlit Community Cloud, Render, or another host that can run a long-lived web process.

Do not deploy this app directly to Vercel as a Python serverless project. Vercel expects `app.py` to export a top-level WSGI/ASGI variable such as `app`, `application`, or `handler`, while Streamlit apps are launched with `streamlit run app.py`.

See `DEPLOYMENT.md` for working deployment options.

## Development

```bash
pip install -r requirements.txt -r requirements-dev.txt
pre-commit install
pytest
```

The test suite is configured in `pyproject.toml` with coverage reporting and a `75%` fail-under threshold.

## Security and CI

This repo includes:

- Secret scanning with Gitleaks and TruffleHog
- Dependency auditing with `pip-audit`
- Static analysis with Bandit
- GitLab CI in `.gitlab-ci.yml`
- Pre-commit hooks in `.pre-commit-config.yaml`
- Automated changelog configuration with `git-cliff` in `cliff.toml`
- Docker build support with `Dockerfile` and `.dockerignore`

See `SECURITY.md`, `CONTRIBUTING.md`, `USER_MANUAL.md`, `AGENTS.md`, and `SPEC_KIT.md` for operating guidance.

## Files

- `app.py` - Streamlit UI, language switcher, AI provider controls
- `i18n.py` - translation dictionaries and localized option labels
- `ai_client.py` - Ollama, BYOK, and onboard AI helper functions
- `field_presets.py` - placement presets and selection rules
- `field_renderer.py` - SVG cricket field renderer
