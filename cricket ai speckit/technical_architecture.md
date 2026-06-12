Technical Architecture
System Overview
```
┌──────────────────────────────────────────────────┐
│                  Browser (React App)              │
│                                                  │
│  ┌─────────────────┐    ┌──────────────────────┐ │
│  │  Selector Panel  │───▶│  Placement Engine    │ │
│  │  - Batsman type  │    │  (JSON Rule Maps)    │ │
│  │  - Bowler style  │    └──────────┬───────────┘ │
│  └─────────────────┘               │             │
│                                    ▼             │
│                     ┌──────────────────────────┐ │
│                     │   SVG Field Renderer      │ │
│                     │   - Oval ground           │ │
│                     │   - 9 fielder markers     │ │
│                     │   - Tooltips              │ │
│                     └──────────────────────────┘ │
└──────────────────────────────────────────────────┘
```
---
Frontend Architecture
Component Tree
```
App
├── Header
├── SelectorPanel
│   ├── BatsmanSelector
│   └── BowlerSelector
├── FieldMap
│   ├── GroundSVG
│   ├── FielderMarker (x9)
│   └── TooltipOverlay
└── FieldInfo
    ├── FieldPresetName
    └── ResetButton
```
State Shape
```json
{
  "batsman": {
    "hand": "left",
    "position": "opener",
    "weakness": "short_ball"
  },
  "bowler": {
    "type": "right_arm_fast",
    "special": "bouncer"
  },
  "fielders": [
    {
      "id": "slip_1",
      "name": "First Slip",
      "x": 52,
      "y": 38,
      "reason": "Catching edge from outside off stump"
    }
    // ... 8 more
  ],
  "presetName": "Short Ball Trap — Off Side"
}
```
---
Placement Engine
Logic
A lookup map of `batsman_profile + bowler_type → fielder_positions[]`
Each combination maps to a named preset + 9 (x, y) coordinates on the SVG canvas
Coordinates are normalized (0–100) and mapped to SVG viewBox
Example Rule
```json
"left_opener_short_ball_weakness + right_arm_fast_bouncer": {
  "preset": "Short Ball Trap",
  "fielders": [
    { "name": "Fine Leg", "x": 48, "y": 88, "reason": "Catches/saves the pull shot" },
    { "name": "Square Leg", "x": 30, "y": 62, "reason": "Cuts off leg glance" },
    { "name": "Mid Wicket", "x": 25, "y": 50, "reason": "Stops the flick off pads" },
    { "name": "Mid On", "x": 38, "y": 35, "reason": "Straight drive cover" },
    { "name": "Mid Off", "x": 62, "y": 35, "reason": "Off drive coverage" },
    { "name": "Cover", "x": 72, "y": 48, "reason": "Drive off front foot" },
    { "name": "Point", "x": 78, "y": 58, "reason": "Cut shot off short ball" },
    { "name": "Gully", "x": 70, "y": 38, "reason": "Top edge off short ball" },
    { "name": "Third Man", "x": 55, "y": 88, "reason": "Edge past keeper going fine" }
  ]
}
```
---
Tech Stack
Component	Choice	Reason
UI Framework	React (Vite)	Fast setup, component model
Styling	Tailwind CSS	Rapid layout without CSS files
Field Rendering	Inline SVG	Full control, no canvas complexity
Logic	JSON map	No backend needed, fast lookup
Deployment	Vercel	One-command deploy
---
File Structure
```
cricfield-ai/
├── public/
├── src/
│   ├── components/
│   │   ├── FieldMap.jsx
│   │   ├── FielderMarker.jsx
│   │   ├── SelectorPanel.jsx
│   │   ├── BatsmanSelector.jsx
│   │   └── BowlerSelector.jsx
│   ├── data/
│   │   └── fieldPresets.json
│   ├── utils/
│   │   └── placementEngine.js
│   ├── App.jsx
│   └── main.jsx
├── index.html
├── package.json
└── vite.config.js
```

---
Implemented Streamlit Architecture
- `app.py`: Streamlit interface, language selector, AI provider selector, and dashboard layout.
- `i18n.py`: translation dictionaries for English, Hindi, and Telugu plus localized option labels.
- `ai_client.py`: prompt builder, local Ollama client, OpenAI-compatible BYOK client, and onboard fallback AI note.
- `field_presets.py`: deterministic placement engine that keeps stable English keys for reliable rule matching.
- `field_renderer.py`: SVG renderer with localized zone legend labels.

AI Provider Flow
1. Onboard rule-based AI returns an immediate coaching note with no network or token.
2. Ollama mode sends the coaching prompt to a local `/api/generate` endpoint.
3. BYOK mode sends the prompt to the user's OpenAI-compatible `/chat/completions` endpoint with their runtime token.
4. If a provider fails, the app falls back to onboard AI guidance so the user can continue.

i18n/l10n Flow
1. English is loaded by default.
2. The user picks English, Hindi, or Telugu in the sidebar.
3. UI labels and option display text come from `i18n.py`.
4. Internal cricket values remain stable so changing language does not break placement lookup.
