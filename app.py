import streamlit as st
from field_presets import get_fielders, BATSMAN_WEAKNESSES, BOWLER_TYPES, BOWLER_SPECIALS
from field_renderer import render_field_svg

st.set_page_config(page_title="CricField AI", page_icon="🏏", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
    body, .stApp { background-color: #0f1e0d; color: #f0f0f0; }
    .main-title {
        font-size: 2.4rem; font-weight: 800; color: #f5c518;
        text-align: center; margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1rem; color: #a0c8a0; text-align: center; margin-bottom: 1.5rem;
    }
    .preset-box {
        background: #1a3a17; border: 1px solid #f5c518;
        border-radius: 10px; padding: 14px 20px; margin-top: 1rem;
        text-align: center;
    }
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
    .stSelectbox label { color: #a0c8a0 !important; font-weight: 600; }
    div[data-testid="stSelectbox"] > div { background: #1a3a17 !important; color: #f0f0f0 !important; }
    .section-header {
        color: #f5c518; font-weight: 700; font-size: 1rem;
        border-bottom: 1px solid #2a4a27; padding-bottom: 4px; margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="main-title">🏏 CricField AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Smart Cricket Field Placement Dashboard</div>', unsafe_allow_html=True)

# ---------- Layout ----------
left_col, right_col = st.columns([1, 2], gap="large")

with left_col:
    st.markdown('<div class="section-header">🧢 Batsman Profile</div>', unsafe_allow_html=True)

    hand = st.selectbox("Handedness", ["Right-Handed", "Left-Handed"])
    position = st.selectbox("Batting Position", ["Opener", "Middle Order", "Lower Order"])
    weakness = st.selectbox("Known Weakness", list(BATSMAN_WEAKNESSES.keys()))

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🎯 Bowler Style</div>', unsafe_allow_html=True)

    bowler_type = st.selectbox("Bowler Type", list(BOWLER_TYPES.keys()))
    special = st.selectbox("Special Delivery", list(BOWLER_SPECIALS.keys()))

# ---------- Compute placement ----------
result = get_fielders(hand, weakness, bowler_type, special)
fielders = result["fielders"]
preset_name = result["preset_name"]
preset_desc = result["preset_desc"]

with right_col:
    st.markdown('<div class="section-header">🏟️ Field Map</div>', unsafe_allow_html=True)

    svg = render_field_svg(fielders, hand)
    st.components.v1.html(svg, height=480, scrolling=False)

    st.markdown(f"""
    <div class="preset-box">
        <div class="preset-name">📋 {preset_name}</div>
        <div class="preset-desc">{preset_desc}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Fielder breakdown table ----------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-header">📌 Fielder Placement Breakdown</div>', unsafe_allow_html=True)

rows = ""
for f in fielders:
    badge_class = "badge-catching" if f["zone"] == "Catching" else "badge-saving"
    rows += f"""
    <tr>
        <td><b>{f['name']}</b></td>
        <td><span class="{badge_class}">{f['zone']}</span></td>
        <td>{f['reason']}</td>
    </tr>
    """

st.markdown(f"""
<table class="fielder-table">
  <thead><tr><th>Position</th><th>Zone</th><th>Reason</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    '<p style="text-align:center; color:#4a7a47; font-size:0.8rem;">CricField AI — Hackathon 2 | Solo Project | Theme: Open</p>',
    unsafe_allow_html=True
)
