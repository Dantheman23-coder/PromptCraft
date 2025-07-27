from promptcraft.prompt import rewrite


def test_rewrite(monkeypatch):
    def fake_chat(prompt: str) -> str:
        return "rewritten"

    monkeypatch.setattr("promptcraft.ai_client.AIClient.chat", lambda self, p: fake_chat(p))
    assert rewrite("hello") == "rewritten"
