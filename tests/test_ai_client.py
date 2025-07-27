from promptcraft.ai_client import AIClient


def test_ai_client(monkeypatch):
    client = AIClient()
    monkeypatch.setattr("promptcraft.ai_client.openai.ChatCompletion.create", lambda **kwargs: type('x',(object,),{'choices':[type('x',(object,),{'message':type('x',(object,),{"content":"ok"})()})()]})())
    assert client.chat("hi") == "ok"
