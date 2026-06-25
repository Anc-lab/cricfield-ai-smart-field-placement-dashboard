# Deployment

## Important: Vercel Is Not the Right Target

This project is a Streamlit app. Vercel detected `app.py` as a Python serverless function and expected a top-level WSGI/ASGI variable named `app`, `application`, or `handler`.

Streamlit apps do not expose that kind of variable. They run as a long-lived web process with:

```bash
streamlit run app.py
```

That is why Vercel fails with:

```text
Found app.py but it does not export a top-level "app", "application", or "handler" variable.
```

## Recommended: Streamlit Community Cloud

Use Streamlit Community Cloud for the simplest deployment.

Settings:

- Repository: `Anc-lab/cricfield-ai-smart-field-placement-dashboard`
- Branch: `main`
- Main file path: `app.py`
- Python dependencies: `requirements.txt`

No build command is needed.

## Alternative: Render

Render can run Streamlit as a web service.

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

## Alternative: Docker

The included `Dockerfile` starts the app on port `8501`.

```bash
docker build -t cricfield-ai .
docker run -p 8501:8501 cricfield-ai
```
