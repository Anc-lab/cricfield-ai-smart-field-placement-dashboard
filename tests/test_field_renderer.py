from field_renderer import render_field_svg


def test_render_field_svg_contains_markers_and_labels():
    svg = render_field_svg(
        [
            {
                "name": "First Slip",
                "x": 285,
                "y": 255,
                "zone": "Catching",
                "reason": "Outside edge",
            }
        ],
        hand="Right-Handed",
        catching_label="Catching",
        saving_label="Saving",
    )

    assert "<svg" in svg
    assert 'transform="translate(285,255)"' in svg
    assert "First Slip: Outside edge" in svg
    assert "Batting left" in svg
