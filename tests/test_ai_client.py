import pytest

from ai_client import build_prompt, call_ollama, call_openai_compatible, onboard_ai_note


def test_build_prompt_includes_matchup_and_fielders():
    prompt = build_prompt(
        "English",
        "Right-Handed",
        "Opener",
        "Weak Outside Off Stump",
        "Right-arm Fast",
        "Swing (Outswing)",
        {"preset_name": "Off-Stump Channel Trap", "preset_desc": "Attacking cordon"},
        [{"name": "First Slip", "zone": "Catching", "reason": "Outside edge"}],
    )

    assert "Right-Handed, Opener" in prompt
    assert "Off-Stump Channel Trap - Attacking cordon" in prompt
    assert "- First Slip (Catching): Outside edge" in prompt


def test_onboard_ai_note_uses_selected_terms():
    note = onboard_ai_note(
        "en",
        {"preset_name": "Short Ball Trap"},
        "Weak vs Short Ball",
        "Right-arm Fast",
        "Bouncer Specialist",
    )

    assert "Short Ball Trap" in note
    assert "Weak vs Short Ball" in note
    assert "Right-arm Fast / Bouncer Specialist" in note


def test_call_ollama_returns_trimmed_response(monkeypatch):
    class Response:
        def raise_for_status(self):
            return None

        def json(self):
            return {"response": "  hold the ring  "}

    def fake_post(url, json, timeout):
        assert url == "http://localhost:11434/api/generate"
        assert json["stream"] is False
        assert timeout == 45
        return Response()

    monkeypatch.setattr("requests.post", fake_post)

    assert call_ollama("http://localhost:11434/", "llama3.1", "prompt") == "hold the ring"


def test_call_openai_compatible_returns_message(monkeypatch):
    class Response:
        def raise_for_status(self):
            return None

        def json(self):
            return {"choices": [{"message": {"content": "  attack off stump  "}}]}

    def fake_post(url, headers, json, timeout):
        assert url == "https://example.test/v1/chat/completions"
        assert headers["Authorization"] == "Bearer token"
        assert json["model"] == "model"
        assert timeout == 45
        return Response()

    monkeypatch.setattr("requests.post", fake_post)

    assert call_openai_compatible("https://example.test/v1/", "token", "model", "prompt") == "attack off stump"


def test_call_openai_compatible_raises_for_malformed_response(monkeypatch):
    class Response:
        def raise_for_status(self):
            return None

        def json(self):
            return {"choices": []}

    monkeypatch.setattr("requests.post", lambda *args, **kwargs: Response())

    with pytest.raises(IndexError):
        call_openai_compatible("https://example.test/v1", "token", "model", "prompt")
