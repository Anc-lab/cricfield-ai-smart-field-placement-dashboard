Build Plan & Timeline
Hackathon Schedule
Time	Milestone	Deliverable
10:00 AM	Project scaffold	Vite + React + Tailwind running
10:30 AM	SVG field renders	Static oval ground with pitch visible
10:45 AM	Static fielders placed	9 hardcoded markers on field
11:00 AM	Selector UI done	Batsman + Bowler dropdowns wired
11:20 AM	Placement engine wired	Field updates on selector change
11:40 AM	Tooltips working	Hover shows reason for each fielder
12:00 PM	Preset name displays	Field name shown below SVG
12:20 PM	Polish & bug fixes	Colours, spacing, mobile check
12:40 PM	README + GitLab push	Repo live with description
1:00 PM	SpecKit + GitLab URL submitted	✅
---
Build Order (Priority Stack)
P0 — Must Have (Demo blockers)
[ ] React scaffold with Tailwind
[ ] SVG cricket oval (oval + pitch + boundary circle)
[ ] Batsman selector (hand, position, weakness)
[ ] Bowler selector (type, special)
[ ] Placement engine (`selectorsToPreset()`)
[ ] 9 fielder markers rendered from preset data
[ ] Field preset name displayed
P1 — Should Have (Demo quality)
[ ] Tooltip on fielder hover
[ ] Smooth transition when field changes
[ ] Mobile responsive layout
[ ] Reset button
P2 — Nice to Have (Bonus)
[ ] Draggable fielder markers
[ ] Export as PNG
[ ] At least 6 distinct presets in `fieldPresets.json`
---
Commands
```bash
# Bootstrap
npm create vite@latest cricfield-ai -- --template react
cd cricfield-ai
npm install
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Dev
npm run dev

# Build
npm run build

# Deploy to Vercel
npx vercel --prod
```
---
GitLab Repo Setup
```bash
git init
git remote add origin <YOUR_GITLAB_URL>
git add .
git commit -m "feat: initial CricField AI scaffold"
git push -u origin main
```
Suggested Repo Description
> 🏏 CricField AI — Visual cricket field placement dashboard. Select batsman type + bowler style, get optimal 9-fielder placement with reasoning. Built for Hackathon 2.
---
Demo Script (2 minutes)
Open the app — show the dark green field
Set: Left-handed Opener + Weak vs Short Balls + Right-arm Fast Bouncer
Watch the field snap to "Short Ball Trap" — 9 fielders placed
Hover Fine Leg → "Protects against the top-edge pull shot"
Switch to Right-handed batsman + Leg Spin → field completely changes to "Spin Trap"
One sentence: "This can help any captain set their field in under 10 seconds."