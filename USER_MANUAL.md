# User Manual

## Purpose

CricField AI helps a captain, coach, or analyst choose a cricket field based on batter handedness, batting role, known weakness, bowler type, and special delivery plan.

## Running the Dashboard

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open the Streamlit URL shown in the terminal, usually `http://localhost:8501`.

## Basic Workflow

1. Choose the interface language in the sidebar.
2. Select the AI mode:
   - Onboard rule-based AI for offline guidance.
   - Local AI via Ollama for local model generation.
   - BYOK OpenAI-compatible API for a provider token entered at runtime.
3. Select the batter profile.
4. Select the bowler style and special delivery.
5. Review the field map, preset name, placement explanation, and AI coaching note.

## Ollama Mode

Start Ollama separately:

```bash
ollama pull llama3.1
ollama serve
```

Then select `Local AI via Ollama` and confirm the URL/model in the sidebar.

## BYOK Mode

Enter an OpenAI-compatible API base URL, model name, and token in the sidebar. The app does not commit or persist that token.
