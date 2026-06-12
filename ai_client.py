import requests


def build_prompt(language_name, hand, position, weakness, bowler_type, special, preset, fielders):
    fielder_lines = "\n".join(
        f"- {f['name']} ({f['zone']}): {f['reason']}" for f in fielders
    )
    return f"""
You are a cricket fielding coach. Reply in {language_name}.
Give a concise coaching note for this field setup.

Batter: {hand}, {position}
Weakness: {weakness}
Bowler: {bowler_type}, special delivery: {special}
Preset: {preset['preset_name']} - {preset['preset_desc']}
Fielders:
{fielder_lines}

Include:
1. why this field works
2. one risk to monitor
3. one quick captain instruction
""".strip()


def onboard_ai_note(lang, preset, weakness, bowler_type, special):
    if lang == "hi":
        return (
            f"{preset['preset_name']} इस matchup के लिए सही है क्योंकि यह {weakness} को target करता है "
            f"और {bowler_type} / {special} plan को support करता है. Captain को catching zone active रखना चाहिए, "
            "single रोकने के लिए inner ring tight रखनी चाहिए, और अगर batter release shot ढूंढे तो deep protection adjust करनी चाहिए."
        )
    if lang == "te":
        return (
            f"{preset['preset_name']} ఈ matchup కి సరిపోతుంది, ఎందుకంటే ఇది {weakness} ను target చేస్తుంది "
            f"మరియు {bowler_type} / {special} plan కు support ఇస్తుంది. Captain catching zone ను active గా ఉంచాలి, "
            "singles తగ్గించేందుకు inner ring tight గా ఉంచాలి, batter release shot ప్రయత్నిస్తే deep protection adjust చేయాలి."
        )
    return (
        f"{preset['preset_name']} fits this matchup because it targets {weakness} while supporting the "
        f"{bowler_type} / {special} bowling plan. Keep the catching zone alert, protect easy singles with a tight ring, "
        "and adjust deep cover if the batter starts finding a release shot."
    )


def call_ollama(base_url, model, prompt):
    url = base_url.rstrip("/") + "/api/generate"
    response = requests.post(
        url,
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=45,
    )
    response.raise_for_status()
    return response.json().get("response", "").strip()


def call_openai_compatible(base_url, api_key, model, prompt):
    url = base_url.rstrip("/") + "/chat/completions"
    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.35,
        },
        timeout=45,
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"].strip()
