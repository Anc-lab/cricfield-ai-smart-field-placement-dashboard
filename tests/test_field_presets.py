from field_presets import get_fielders


def test_bouncer_weakness_selects_short_ball_trap():
    preset = get_fielders(
        "Right-Handed",
        "Weak vs Short Ball",
        "Right-arm Fast",
        "Bouncer Specialist",
    )

    assert preset["preset_name"] == "Short Ball Trap"
    assert len(preset["fielders"]) == 9
    assert any(fielder["zone"] == "Catching" for fielder in preset["fielders"])


def test_left_handed_field_is_mirrored_from_right_handed():
    right = get_fielders(
        "Right-Handed",
        "Weak Outside Off Stump",
        "Right-arm Fast",
        "Swing (Outswing)",
    )
    left = get_fielders(
        "Left-Handed",
        "Weak Outside Off Stump",
        "Right-arm Fast",
        "Swing (Outswing)",
    )

    assert left["preset_name"] == right["preset_name"]
    assert left["fielders"][0]["x"] == 500 - right["fielders"][0]["x"]
    assert left["fielders"][0]["y"] == right["fielders"][0]["y"]


def test_spin_matchup_selects_spin_trap():
    preset = get_fielders(
        "Right-Handed",
        "Weak vs Spin (Turning In)",
        "Right-arm Off-spin",
        "Turning / Spinning",
    )

    assert "Spin Trap" in preset["preset_name"]
    assert "Leg Side Loaded" in preset["preset_name"]


def test_inswing_early_drive_selects_leg_stump_attack():
    preset = get_fielders(
        "Right-Handed",
        "Tends to Drive Early",
        "Right-arm Fast",
        "Swing (Inswing)",
    )

    assert "Leg-Stump Attack" in preset["preset_name"]
    assert "Inswing" in preset["preset_name"]


def test_yorker_specialist_selects_death_overs_setup():
    preset = get_fielders(
        "Right-Handed",
        "Strong on Leg Side",
        "Right-arm Medium",
        "Yorker Specialist",
    )

    assert "Death Overs" in preset["preset_name"]
    assert "Yorker Setup" in preset["preset_name"]


def test_unknown_inputs_fall_back_to_attacking_pace():
    preset = get_fielders("Right-Handed", "Unknown", "Unknown", "Unknown")

    assert "Attacking Pace" in preset["preset_name"]
    assert "New Ball" in preset["preset_name"]
