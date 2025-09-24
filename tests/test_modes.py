from promptcraft.modes import boss_mode


def test_boss_mode(monkeypatch):
    monkeypatch.setattr("promptcraft.ai_client.AIClient.chat", lambda self, p: p)
    result = boss_mode("hi")
    assert "First draft" in result
