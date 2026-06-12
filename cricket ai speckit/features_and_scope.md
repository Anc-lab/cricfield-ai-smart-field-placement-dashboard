Features & Scope
✅ In Scope (MVP for Hackathon)
Core Features
1. Batsman Profile Selector
Handedness: Left / Right
Batting position: Opener / Middle Order / Lower Order
Known weakness:
Weak against short balls
Weak outside off stump
Weak against spin (turning in)
Plays across the line
Strong on the leg side (punish gaps there)
2. Bowler Style Selector
Pace: Right-arm Fast / Left-arm Fast / Right-arm Medium / Left-arm Medium
Spin: Right-arm Off-spin / Left-arm Orthodox / Leg Spin
Special: Swing (In/Out), Yorker specialist, Bouncer specialist
3. 2D Interactive Field Map
SVG oval cricket ground
9 fielder markers placed automatically
Fielder labels (Slip, Gully, Point, Mid-off, etc.)
Colour-coded by region (catching/saving)
Draggable markers to manually adjust positions
4. Placement Explanation Tooltips
Each fielder marker shows a tooltip on hover/tap
Explains why this position was chosen
Example: "Fine Leg — Protects against the pull shot, exploiting weakness vs short balls"
5. Field Preset Display
Shows field name (e.g., "Attacking Off-side Trap", "Leg-side Loaded")
Reset to AI suggestion button
6. Multilingual Experience
English is the default language.
Hindi and Telugu are available from the sidebar.
Selectors, headings, table labels, AI controls, and adoption guidance are localized.
7. AI Provider Choice
Onboard rule-based AI for instant no-token demos.
Local AI inference through Ollama.
BYOK support for OpenAI-compatible APIs using the user's own token.
8. User-Centric Market Adoption
Localized UI for Indian cricket users.
Explainable recommendations for trust.
Local inference and BYOK for cost, privacy, and deployment flexibility.
---
🔮 Stretch Goals (if time permits)
Side-by-side field comparison (e.g., Powerplay vs Death)
Export field as PNG image
Share via URL (encoded state in query params)
Animated fielder movement when field changes
---
❌ Out of Scope
Real player names or live match data
Mobile native app
Backend / database
User authentication
Multiple overs / match simulation
