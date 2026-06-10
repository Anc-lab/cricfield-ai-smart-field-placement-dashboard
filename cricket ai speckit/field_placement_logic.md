Field Placement Logic & Data Spec
Coordinate System
SVG ViewBox: `0 0 500 500`
Centre of pitch: `(250, 250)`
All coordinates are absolute SVG units
Ground radius: ~200 units
---
Standard Fielding Positions (Reference)
Position	Approx SVG (x, y)	Zone
Wicket Keeper	250, 270	Catching
First Slip	285, 255	Catching
Second Slip	305, 248	Catching
Gully	330, 230	Catching
Point	370, 265	Saving
Cover Point	355, 310	Saving
Extra Cover	320, 340	Saving
Mid Off	290, 170	Saving
Mid On	210, 170	Saving
Mid Wicket	175, 270	Saving
Square Leg	175, 300	Saving
Fine Leg	220, 420	Saving
Third Man	320, 410	Saving
Long On	195, 120	Saving
Long Off	310, 120	Saving
Deep Mid Wicket	145, 330	Saving
Deep Square Leg	155, 370	Saving
---
Preset Field Configurations
1. Short Ball Trap (vs Left-Handed Opener, Weak vs Short Ball, Right-Arm Fast Bouncer)
Intent: Force the pull/hook shot into placed fielders
#	Position	Reason
1	Fine Leg	Catches/saves the top-edge pull
2	Square Leg	Cuts off leg-side flick
3	Mid Wicket	Stops the controlled pull
4	Mid On	Straight drive coverage
5	Mid Off	Off-side straight drive
6	Cover	Front-foot drive
7	Point	Cut shot off short ball
8	Gully	Top edge flying to off side
9	Third Man	Edge past keeper
---
2. Off-Stump Channel (vs Right-Handed Batsman, Weak Outside Off, Right-Arm Swing)
Intent: Invite the drive, protect the edges
#	Position	Reason
1	First Slip	Thick outside edge
2	Second Slip	Thin outside edge
3	Gully	Drive in the air
4	Point	Square cut
5	Cover	Driven into gap
6	Extra Cover	Over-drive
7	Mid Off	Straight drive
8	Mid On	Defensive push
9	Fine Leg	Leg glance / swing through leg
---
3. Spin Trap (vs Right-Handed Middle Order, Weak vs Turning Ball, Leg Spin)
Intent: Invite the big shot into the leg side
#	Position	Reason
1	Slip	Edge off turn
2	Silly Point	Bat-pad catch
3	Mid On	Driven down the ground
4	Long On	Slog over mid on
5	Long Off	Slog over mid off
6	Mid Wicket	Swept to leg
7	Deep Mid Wicket	Slog to mid wicket
8	Fine Leg	Sweep fine
9	Cover	Driven through covers
---
4. Attacking Pace (vs Any Batsman, Right-Arm Fast, New Ball)
Intent: Maximise catching opportunities with pace
#	Position	Reason
1	First Slip	Classic edge catcher
2	Second Slip	Wide edge
3	Gully	Fend off short ball
4	Third Man	Edge running fine
5	Point	Cut shot
6	Cover	Drive
7	Mid Off	Straight drive
8	Mid On	Push back
9	Fine Leg	Leg side
---
Selector → Preset Mapping
```
batsman.hand + batsman.weakness + bowler.type + bowler.special
→ presetKey
```
Batsman Hand	Weakness	Bowler Type	Special	Preset
Left	short_ball	right_arm_fast	bouncer	short_ball_trap
Right	outside_off	right_arm_fast	swing_out	off_stump_channel
Right	spin_turning	leg_spin	—	spin_trap
Any	—	right_arm_fast	new_ball	attacking_pace
Left	across_the_line	left_arm_fast	in_swing	leg_stump_attack
> If no exact match: fall back to `attacking_pace` as default.