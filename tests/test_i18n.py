from i18n import (
    LANGUAGES,
    cricket_label,
    localized_reason,
    option_label,
    preset_desc_label,
    t,
)


def test_default_translation_falls_back_to_english():
    assert t("missing-language", "app_title") == "CricField AI"
    assert t("en", "missing-key") == "missing-key"


def test_option_and_cricket_labels_return_localized_or_original_values():
    assert option_label("en", "Right-arm Fast") == "Right-arm Fast"
    assert option_label("hi", "Right-arm Fast") != "Right-arm Fast"
    assert cricket_label("en", "Fine Leg") == "Fine Leg"
    assert cricket_label("te", "Fine Leg") != "Fine Leg"


def test_preset_description_uses_language_specific_mapping():
    desc = "Classic attacking setup maximising catching positions with the new ball."

    assert preset_desc_label("en", desc) == desc
    assert preset_desc_label("hi", desc) != desc


def test_localized_reason_matches_zone_and_language():
    assert localized_reason("en", "Fine Leg", "Saving") is None
    assert "edge" in localized_reason("hi", "First Slip", "Catching")
    assert "scoring gap" in localized_reason("te", "Fine Leg", "Saving")


def test_supported_language_codes_are_available():
    assert set(LANGUAGES) == {"en", "hi", "te"}
