🏏 CricField AI — Smart Cricket Field Placement Dashboard
---
One-Line Pitch
> Select a batsman type and bowler style — get an AI-optimized 2D cricket field placement instantly.
---
The Problem
Cricket captains and coaches spend significant mental energy deciding field placements based on batsman weaknesses, bowler type, match situations, and pitch conditions. There's no visual, interactive tool that makes this decision fast, explainable, and data-informed.
---
The Solution
CricField AI is a web-based visual dashboard where:
The user picks a batsman profile (handedness, position, known weaknesses)
The user picks a bowler style (pace, spin, swing, angle)
The app instantly renders an interactive 2D cricket field with 9 optimally placed fielders
Each fielder placement comes with a reason tooltip (e.g., "Cover point: covers the drive gap for off-side heavy batsmen")
---
Key Features
🎯 Interactive 2D oval field with draggable fielder markers
🧠 AI/rule-based field logic per batsman-bowler combination
💬 Tooltip explanations for each fielder placement
📋 Export field as image or share link
🔁 Compare two field setups side by side
---
Tech Stack
Layer	Technology
Frontend	React + Tailwind CSS
Field Rendering	SVG / Canvas
Logic Engine	Rule-based JSON map + optional Claude API
State Management	React useState/useReducer
Export	html2canvas
Hosting	Vercel / GitHub Pages
---
Team
Solo Developer — 1 member
---

