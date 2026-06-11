# field_presets.py — CricField AI placement engine

BATSMAN_WEAKNESSES = {
    "Weak vs Short Ball": "short_ball",
    "Weak Outside Off Stump": "outside_off",
    "Weak vs Spin (Turning In)": "spin_turning",
    "Plays Across the Line": "across_line",
    "Strong on Leg Side": "strong_leg",
    "Tends to Drive Early": "early_drive",
}

BOWLER_TYPES = {
    "Right-arm Fast": "raf",
    "Left-arm Fast": "laf",
    "Right-arm Medium": "ram",
    "Left-arm Medium": "lam",
    "Right-arm Off-spin": "raos",
    "Left-arm Orthodox Spin": "laos",
    "Leg Spin / Googly": "leg_spin",
}

BOWLER_SPECIALS = {
    "None": "none",
    "Bouncer Specialist": "bouncer",
    "Swing (Outswing)": "outswing",
    "Swing (Inswing)": "inswing",
    "Yorker Specialist": "yorker",
    "Turning / Spinning": "turning",
}

# ── Preset definitions ───────────────────────────────────────────────────────

PRESETS = {

    "short_ball_trap": {
        "preset_name": "Short Ball Trap",
        "preset_desc": "Packs the leg side and square boundaries to exploit the pull/hook weakness.",
        "fielders": [
            {"name": "Fine Leg",       "x": 250, "y": 430, "zone": "Saving",   "reason": "Catches the top-edge pull going fine"},
            {"name": "Square Leg",     "x": 160, "y": 310, "zone": "Saving",   "reason": "Cuts off the controlled leg glance"},
            {"name": "Mid Wicket",     "x": 155, "y": 255, "zone": "Saving",   "reason": "Stops the flick off the pads"},
            {"name": "Mid On",         "x": 205, "y": 170, "zone": "Saving",   "reason": "Straight drive coverage"},
            {"name": "Mid Off",        "x": 295, "y": 170, "zone": "Saving",   "reason": "Off-drive coverage"},
            {"name": "Cover",          "x": 355, "y": 310, "zone": "Saving",   "reason": "Front-foot drive to cover"},
            {"name": "Point",          "x": 370, "y": 265, "zone": "Saving",   "reason": "Cut shot off a short ball"},
            {"name": "Gully",          "x": 335, "y": 225, "zone": "Catching", "reason": "Top-edge flying to off side"},
            {"name": "Third Man",      "x": 320, "y": 420, "zone": "Saving",   "reason": "Edge past the keeper going fine"},
        ]
    },

    "off_stump_channel": {
        "preset_name": "Off-Stump Channel Trap",
        "preset_desc": "Three slips and a gully to maximise catching, inviting the drive outside off.",
        "fielders": [
            {"name": "First Slip",     "x": 285, "y": 255, "zone": "Catching", "reason": "Thick outside edge off the drive"},
            {"name": "Second Slip",    "x": 305, "y": 248, "zone": "Catching", "reason": "Thin edge carrying to second slip"},
            {"name": "Gully",          "x": 335, "y": 225, "zone": "Catching", "reason": "Drive in the air through gully"},
            {"name": "Point",          "x": 370, "y": 265, "zone": "Saving",   "reason": "Square cut off a full ball"},
            {"name": "Cover",          "x": 355, "y": 310, "zone": "Saving",   "reason": "Driven into the gap"},
            {"name": "Extra Cover",    "x": 325, "y": 340, "zone": "Saving",   "reason": "Over-drive or inside-out shot"},
            {"name": "Mid Off",        "x": 295, "y": 170, "zone": "Saving",   "reason": "Straight drive blocked"},
            {"name": "Mid On",         "x": 205, "y": 170, "zone": "Saving",   "reason": "Defensive push back"},
            {"name": "Fine Leg",       "x": 250, "y": 430, "zone": "Saving",   "reason": "Leg glance / inswing through leg"},
        ]
    },

    "spin_trap": {
        "preset_name": "Spin Trap — Leg Side Loaded",
        "preset_desc": "Invites the big slog sweep, with deep fielders protecting boundaries on the leg side.",
        "fielders": [
            {"name": "Slip",           "x": 285, "y": 255, "zone": "Catching", "reason": "Edge off the turn past the keeper"},
            {"name": "Silly Point",    "x": 290, "y": 230, "zone": "Catching", "reason": "Bat-pad catch from the forward press"},
            {"name": "Mid On",         "x": 205, "y": 170, "zone": "Saving",   "reason": "Driven back down the ground"},
            {"name": "Long On",        "x": 190, "y": 110, "zone": "Saving",   "reason": "Slog over mid on"},
            {"name": "Long Off",       "x": 310, "y": 110, "zone": "Saving",   "reason": "Slog over mid off"},
            {"name": "Mid Wicket",     "x": 155, "y": 255, "zone": "Saving",   "reason": "Swept to mid wicket"},
            {"name": "Deep Mid Wicket","x": 130, "y": 330, "zone": "Saving",   "reason": "Slog to deep mid wicket"},
            {"name": "Fine Leg",       "x": 250, "y": 430, "zone": "Saving",   "reason": "Sweep fine off spin"},
            {"name": "Cover",          "x": 355, "y": 310, "zone": "Saving",   "reason": "Driven through the covers"},
        ]
    },

    "attacking_pace_new_ball": {
        "preset_name": "Attacking Pace — New Ball",
        "preset_desc": "Classic attacking setup maximising catching positions with the new ball.",
        "fielders": [
            {"name": "First Slip",     "x": 285, "y": 255, "zone": "Catching", "reason": "Classic edge catcher with new ball movement"},
            {"name": "Second Slip",    "x": 305, "y": 248, "zone": "Catching", "reason": "Wide edge carrying to slip cordon"},
            {"name": "Gully",          "x": 335, "y": 225, "zone": "Catching", "reason": "Fend off a short delivery to off side"},
            {"name": "Third Man",      "x": 320, "y": 420, "zone": "Saving",   "reason": "Edge running fine past the keeper"},
            {"name": "Point",          "x": 370, "y": 265, "zone": "Saving",   "reason": "Cut shot controlled"},
            {"name": "Cover",          "x": 355, "y": 310, "zone": "Saving",   "reason": "Drive through the covers"},
            {"name": "Mid Off",        "x": 295, "y": 170, "zone": "Saving",   "reason": "Straight drive blocked"},
            {"name": "Mid On",         "x": 205, "y": 170, "zone": "Saving",   "reason": "Push back down the ground"},
            {"name": "Fine Leg",       "x": 250, "y": 430, "zone": "Saving",   "reason": "Leg side protection"},
        ]
    },

    "leg_stump_attack": {
        "preset_name": "Leg-Stump Attack — Inswing",
        "preset_desc": "Traps the batsman on the crease, loading the on side for the inevitable flick.",
        "fielders": [
            {"name": "Fine Leg",       "x": 250, "y": 430, "zone": "Saving",   "reason": "Flicked off the pads going fine"},
            {"name": "Square Leg",     "x": 160, "y": 310, "zone": "Saving",   "reason": "Leg glance controlled"},
            {"name": "Mid Wicket",     "x": 155, "y": 255, "zone": "Saving",   "reason": "On-drive blocked"},
            {"name": "Mid On",         "x": 205, "y": 170, "zone": "Saving",   "reason": "Straight push back"},
            {"name": "Mid Off",        "x": 295, "y": 170, "zone": "Saving",   "reason": "Off-drive coverage"},
            {"name": "Cover",          "x": 355, "y": 310, "zone": "Saving",   "reason": "Drive through covers"},
            {"name": "First Slip",     "x": 285, "y": 255, "zone": "Catching", "reason": "Outside edge on inswing delivery"},
            {"name": "Gully",          "x": 335, "y": 225, "zone": "Catching", "reason": "Top-edge or defensive prod"},
            {"name": "Third Man",      "x": 320, "y": 420, "zone": "Saving",   "reason": "Edge running fine"},
        ]
    },

    "yorker_death": {
        "preset_name": "Death Overs — Yorker Setup",
        "preset_desc": "Protects the boundaries with deep fielders, leaving only straight hitting gaps.",
        "fielders": [
            {"name": "Deep Fine Leg",  "x": 240, "y": 445, "zone": "Saving",   "reason": "Flick off a full toss going fine"},
            {"name": "Deep Sq Leg",    "x": 145, "y": 360, "zone": "Saving",   "reason": "Slog to square leg boundary"},
            {"name": "Deep Mid Wicket","x": 130, "y": 290, "zone": "Saving",   "reason": "Slog over mid wicket"},
            {"name": "Long On",        "x": 190, "y": 110, "zone": "Saving",   "reason": "Straight hit over mid on"},
            {"name": "Long Off",       "x": 310, "y": 110, "zone": "Saving",   "reason": "Straight hit over mid off"},
            {"name": "Deep Cover",     "x": 375, "y": 340, "zone": "Saving",   "reason": "Slog through covers"},
            {"name": "Deep Point",     "x": 390, "y": 275, "zone": "Saving",   "reason": "Cut or inside-out shot"},
            {"name": "Third Man",      "x": 320, "y": 420, "zone": "Saving",   "reason": "Edge or mis-hit going fine"},
            {"name": "Mid Off",        "x": 295, "y": 170, "zone": "Saving",   "reason": "Straight drive blocked close in"},
        ]
    },

}

# ── Selector → Preset mapping ─────────────────────────────────────────────────

def get_fielders(hand, weakness_label, bowler_type_label, special_label):
    weakness = BATSMAN_WEAKNESSES.get(weakness_label, "short_ball")
    bowler   = BOWLER_TYPES.get(bowler_type_label, "raf")
    special  = BOWLER_SPECIALS.get(special_label, "none")

    # Rule-based lookup
    if weakness == "short_ball" and special == "bouncer":
        key = "short_ball_trap"
    elif weakness == "outside_off" and bowler in ("raf", "ram", "laf", "lam") and special in ("outswing", "none"):
        key = "off_stump_channel"
    elif weakness in ("spin_turning", "across_line") and bowler in ("raos", "laos", "leg_spin"):
        key = "spin_trap"
    elif weakness in ("outside_off", "early_drive") and special == "inswing":
        key = "leg_stump_attack"
    elif special == "yorker":
        key = "yorker_death"
    elif bowler in ("raf", "laf") and special in ("none", "outswing"):
        key = "attacking_pace_new_ball"
    else:
        key = "attacking_pace_new_ball"  # default

    preset = PRESETS[key].copy()

    # Mirror field for left-handers (flip x around centre 250)
    if hand == "Left-Handed":
        mirrored = []
        for f in preset["fielders"]:
            mf = f.copy()
            mf["x"] = 500 - f["x"]
            mirrored.append(mf)
        preset = preset.copy()
        preset["fielders"] = mirrored

    return preset
