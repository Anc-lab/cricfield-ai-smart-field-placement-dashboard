import requests
import streamlit as st

from ai_client import (
    build_prompt,
    call_ollama,
    call_openai_compatible,
    onboard_ai_note,
)
from field_presets import BATSMAN_WEAKNESSES, BOWLER_SPECIALS, BOWLER_TYPES, get_fielders
from field_renderer import render_field_svg
from i18n import LANGUAGES, cricket_label, localized_reason, option_label, preset_desc_label, t


st.set_page_config(page_title="CricField AI", page_icon="🏏", layout="wide")


st.markdown(
    """
<style>
    body, .stApp { background-color: #0f1e0d; color: #f0f0f0; }
    .main-title {
        font-size: 2.4rem; font-weight: 800; color: #f5c518;
        text-align: center; margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1rem; color: #a0c8a0; text-align: center; margin-bottom: 1.5rem;
    }
    .preset-box, .ai-box, .market-box {
        background: #1a3a17; border: 1px solid #f5c518;
        border-radius: 8px; padding: 14px 20px; margin-top: 1rem;
    }
    .preset-box { text-align: center; }
    .preset-name { font-size: 1.3rem; font-weight: 700; color: #f5c518; }
    .preset-desc { font-size: 0.9rem; color: #c0e0c0; margin-top: 4px; }
    .fielder-table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
    .fielder-table th {
        background: #1a3a17; color: #f5c518;
        padding: 8px 12px; text-align: left; font-size: 0.85rem;
    }
    .fielder-table td {
        padding: 7px 12px; font-size: 0.82rem;
        border-bottom: 1px solid #2a4a27; color: #e0e0e0;
    }
    .badge-catching {
        background: #ff6b35; color: white;
        border-radius: 4px; padding: 2px 7px; font-size: 0.75rem;
    }
    .badge-saving {
        background: #1a7abf; color: white;
        border-radius: 4px; padding: 2px 7px; font-size: 0.75rem;
    }
    .stSelectbox label, .stTextInput label { color: #a0c8a0 !important; font-weight: 600; }
    div[data-testid="stSelectbox"] > div { background: #1a3a17 !important; color: #f0f0f0 !important; }
    .section-header {
        color: #f5c518; font-weight: 700; font-size: 1rem;
        border-bottom: 1px solid #2a4a27; padding-bottom: 4px; margin-bottom: 10px;
    }
</style>
""",
    unsafe_allow_html=True,
)


def translated_select(label_key, options, lang, default_index=0):
    return st.selectbox(
        t(lang, label_key),
        options,
        index=default_index,
        format_func=lambda value: option_label(lang, value),
    )


with st.sidebar:
    lang = st.selectbox(
        t("en", "language"),
        list(LANGUAGES.keys()),
        index=0,
        format_func=lambda code: LANGUAGES[code],
    )

    st.markdown(f'<div class="section-header">{t(lang, "ai_settings")}</div>', unsafe_allow_html=True)
    ai_modes = ["rule_based_ai", "ollama", "byok"]
    ai_mode = st.radio(
        t(lang, "ai_mode"),
        ai_modes,
        format_func=lambda value: t(lang, value),
    )
    st.caption(t(lang, "ai_help"))

    ollama_url = "http://localhost:11434"
    ollama_model = "llama3.1"
    api_base_url = "https://api.openai.com/v1"
    api_model = "gpt-4o-mini"
    api_key = ""

    if ai_mode == "ollama":
        ollama_url = st.text_input(t(lang, "ollama_url"), value=ollama_url)
        ollama_model = st.text_input(t(lang, "ollama_model"), value=ollama_model)
    elif ai_mode == "byok":
        api_base_url = st.text_input(t(lang, "api_base_url"), value=api_base_url)
        api_model = st.text_input(t(lang, "api_model"), value=api_model)
        api_key = st.text_input(t(lang, "api_key"), type="password")


st.markdown(f'<div class="main-title">🏏 {t(lang, "app_title")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-title">{t(lang, "subtitle")}</div>', unsafe_allow_html=True)

left_col, right_col = st.columns([1, 2], gap="large")

with left_col:
    st.markdown(f'<div class="section-header">{t(lang, "batsman_profile")}</div>', unsafe_allow_html=True)

    hand_options = ["Right-Handed", "Left-Handed"]
    hand_labels = {
        "Right-Handed": t(lang, "right_handed"),
        "Left-Handed": t(lang, "left_handed"),
    }
    hand = st.selectbox(
        t(lang, "handedness"),
        hand_options,
        format_func=lambda value: hand_labels[value],
    )

    position_options = ["Opener", "Middle Order", "Lower Order"]
    position_labels = {
        "Opener": t(lang, "opener"),
        "Middle Order": t(lang, "middle_order"),
        "Lower Order": t(lang, "lower_order"),
    }
    position = st.selectbox(
        t(lang, "batting_position"),
        position_options,
        format_func=lambda value: position_labels[value],
    )
    weakness = translated_select("known_weakness", list(BATSMAN_WEAKNESSES.keys()), lang)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<div class="section-header">{t(lang, "bowler_style")}</div>', unsafe_allow_html=True)

    bowler_type = translated_select("bowler_type", list(BOWLER_TYPES.keys()), lang)
    special = translated_select("special_delivery", list(BOWLER_SPECIALS.keys()), lang)


result = get_fielders(hand, weakness, bowler_type, special)
fielders = result["fielders"]
display_fielders = []
for fielder in fielders:
    display_fielder = fielder.copy()
    display_fielder["name"] = cricket_label(lang, fielder["name"])
    display_fielder["reason"] = localized_reason(lang, fielder["name"], fielder["zone"]) or fielder["reason"]
    display_fielders.append(display_fielder)

display_preset_name = cricket_label(lang, result["preset_name"])
display_preset_desc = preset_desc_label(lang, result["preset_desc"])

with right_col:
    st.markdown(f'<div class="section-header">{t(lang, "field_map")}</div>', unsafe_allow_html=True)

    svg = render_field_svg(
        display_fielders,
        hand,
        catching_label=t(lang, "catching"),
        saving_label=t(lang, "saving"),
    )
    st.components.v1.html(svg, height=480, scrolling=False)

    st.markdown(
        f"""
    <div class="preset-box">
        <div class="preset-name">{display_preset_name}</div>
        <div class="preset-desc">{display_preset_desc}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f'<div class="section-header">{t(lang, "ai_note")}</div>', unsafe_allow_html=True)

language_name = LANGUAGES[lang]
display_result = result.copy()
display_result["preset_name"] = display_preset_name
display_result["preset_desc"] = display_preset_desc
prompt = build_prompt(language_name, hand, position, weakness, bowler_type, special, display_result, display_fielders)
note = onboard_ai_note(lang, display_result, option_label(lang, weakness), option_label(lang, bowler_type), option_label(lang, special))

if st.button(t(lang, "generate_ai")):
    try:
        if ai_mode == "ollama":
            note = call_ollama(ollama_url, ollama_model, prompt)
        elif ai_mode == "byok" and api_key:
            note = call_openai_compatible(api_base_url, api_key, api_model, prompt)
    except requests.exceptions.RequestException:
        st.warning(t(lang, "ai_error"))
    except (KeyError, IndexError, ValueError):
        st.warning(t(lang, "ai_error"))

st.markdown(f'<div class="ai-box">{note}</div>', unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f'<div class="section-header">{t(lang, "fielder_breakdown")}</div>', unsafe_allow_html=True)

rows = ""
for fielder in display_fielders:
    zone_key = "catching" if fielder["zone"] == "Catching" else "saving"
    badge_class = "badge-catching" if fielder["zone"] == "Catching" else "badge-saving"
    rows += f"""
    <tr>
        <td><b>{fielder['name']}</b></td>
        <td><span class="{badge_class}">{t(lang, zone_key)}</span></td>
        <td>{fielder['reason']}</td>
    </tr>
    """

st.markdown(
    f"""
<table class="fielder-table">
  <thead><tr><th>{t(lang, "position")}</th><th>{t(lang, "zone")}</th><th>{t(lang, "reason")}</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
""",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="market-box">
    <b>{t(lang, "market_alignment")}</b><br>
    {t(lang, "market_text")}
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    f'<p style="text-align:center; color:#4a7a47; font-size:0.8rem;">{t(lang, "footer")}</p>',
    unsafe_allow_html=True,
)
