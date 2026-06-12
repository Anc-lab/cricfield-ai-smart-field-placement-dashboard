UI/UX Design Spec
Design Philosophy
Cricket-first aesthetics — dark green ground, white markers, stadium feel
Mobile-friendly — works on a tablet at the boundary
Instant feedback — field updates the moment selectors change (no submit button)
Explain everything — no placement without a reason
---
Screen Layout (Desktop)
```
┌─────────────────────────────────────────────────────────────────┐
│  🏏 CricField AI                              [Export PNG]       │
├──────────────────────┬──────────────────────────────────────────┤
│                      │                                          │
│   BATSMAN PROFILE    │                                          │
│   ─────────────────  │         [  CRICKET FIELD SVG  ]         │
│   Handedness         │                                          │
│   ○ Left  ○ Right    │      ___________________________         │
│                      │    /                             \        │
│   Position           │   /     ·Gully  ·Slip             \      │
│   ○ Opener           │  |  ·Point                         |     │
│   ○ Middle Order     │  |          [PITCH]        ·Cover  |     │
│   ○ Lower Order      │  |  ·Mid-on         ·Mid-off       |     │
│                      │   \  ·Fine Leg   ·Third Man       /      │
│   Weakness           │    \___________________________/         │
│   ▼ [Dropdown]       │                                          │
│                      │   Field Preset: "Short Ball Trap"        │
│   BOWLER STYLE       │   [Reset to AI Suggestion]               │
│   ─────────────────  │                                          │
│   Type               │                                          │
│   ▼ [Dropdown]       │                                          │
│                      │                                          │
│   Special            │                                          │
│   ▼ [Dropdown]       │                                          │
│                      │                                          │
└──────────────────────┴──────────────────────────────────────────┘
```
---
Screen Layout (Mobile)
```
┌──────────────────────┐
│  🏏 CricField AI     │
├──────────────────────┤
│  Batsman  [▼ Left   ]│
│  Position [▼ Opener ]│
│  Weakness [▼ Short  ]│
│  Bowler   [▼ RF Fast]│
├──────────────────────┤
│                      │
│   [FIELD MAP SVG]    │
│    (full width)      │
│                      │
├──────────────────────┤
│ Preset: Short Trap   │
│ [Reset]  [Export]    │
└──────────────────────┘
```
---
Fielder Marker Design
Circle marker, 18px diameter
White fill with dark green border
Fielder name as small label below
On hover/tap: tooltip card appears
```
  ┌──────────────────────────┐
  │  Fine Leg                │
  │  ──────────────────────  │
  │  Protects against pull   │
  │  shot — exploits short   │
  │  ball weakness           │
  └──────────────────────────┘
  ```
---
Colour Palette
Element	Colour
Ground	`#2d5a27` (dark green)
Pitch	`#c8a96e` (sandy brown)
Boundary	`#ffffff` (white line)
Fielder marker	`#ffffff` fill, `#1a3a17` border
Catching zone fielders	`#ff6b35` accent dot
Saving zone fielders	`#4fc3f7` accent dot
Background	`#0f1e0d` (very dark green)
Text	`#f0f0f0`
Accent	`#f5c518` (cricket gold)
---
Interactions
Action	Behaviour
Change any selector	Field re-renders instantly
Hover fielder marker	Tooltip appears
Drag fielder marker	Marker moves freely on field
Click Reset	Returns to AI-suggested positions
Click Export	Downloads field as PNG

---
Internationalization and Localization
- Default language: English
- Indian language support: Hindi and Telugu
- All primary navigation, form labels, AI controls, table headers, field zones, and adoption messaging are localized.
- Cricket terms stay stable internally so the placement engine remains reliable across languages.
- Language can be changed from the sidebar without changing the selected cricket scenario.

---
AI and Market Adoption Requirements
- Every project screen keeps an AI-powered feature visible through the AI Coaching Note.
- Users can choose onboard rule-based AI for no-setup demos.
- Users can choose local AI inference through Ollama for privacy-friendly offline coaching.
- Users can choose BYOK with an OpenAI-compatible API base URL, model, and user-provided token.
- The dashboard explicitly supports user-centric adoption goals: local languages, explainable recommendations, low-cost local inference, and provider choice for teams with different budgets.
