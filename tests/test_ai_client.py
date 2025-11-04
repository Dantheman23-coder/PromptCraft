import importlib
import sys
from types import SimpleNamespace

import pytest

from promptcraft.ai_client import AIClient, _OpenAIShim, _load_openai


def test_ai_client(monkeypatch):
    client = AIClient()
    monkeypatch.setattr("promptcraft.ai_client.openai.ChatCompletion.create", lambda **kwargs: type('x',(object,),{'choices':[type('x',(object,),{'message':type('x',(object,),{"content":"ok"})()})()]})())
    assert client.chat("hi") == "ok"


class _StubOpenAIModule:
    def __init__(self):
        self.created_with: list[dict[str, object]] = []
        self.requests: list[dict[str, object]] = []

    class _Client:
        def __init__(self, module: "_StubOpenAIModule", **kwargs):
            module.created_with.append(kwargs)
            self._module = module
            self.chat = SimpleNamespace(
                completions=SimpleNamespace(create=module._record_request)
            )

    def OpenAI(self, **kwargs):  # noqa: N802 - replicates OpenAI module API
        return self._Client(self, **kwargs)

    def _record_request(self, **kwargs):
        self.requests.append(kwargs)
        return SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="stub-response"),
                )
            ]
        )


def test_openai_shim_uses_api_key_and_reinitialises():
    stub_module = _StubOpenAIModule()
    shim = _OpenAIShim(stub_module)

    shim.api_key = "abc"
    shim.ChatCompletion.create(model="gpt", messages=[{"role": "user", "content": "hi"}])
    assert stub_module.created_with == [{"api_key": "abc"}]
    assert stub_module.requests == [
        {"model": "gpt", "messages": [{"role": "user", "content": "hi"}]}
    ]

    shim.api_key = None
    shim.ChatCompletion.create(model="gpt", messages=[{"role": "user", "content": "hi"}])
    assert stub_module.created_with[-1] == {}
    assert len(stub_module.created_with) == 2


def test_load_openai_missing_dependency(monkeypatch):
    monkeypatch.delitem(sys.modules, "openai", raising=False)
    original_import = importlib.import_module

    def _missing(name: str, package: str | None = None):
        if name == "openai":
            raise ModuleNotFoundError("openai not installed")
        return original_import(name, package)

    monkeypatch.setattr(importlib, "import_module", _missing)

    loaded = _load_openai()
    with pytest.raises(RuntimeError):
        loaded.ChatCompletion.create()


def test_load_openai_prefers_legacy_chat_completion(monkeypatch):
    stub_module = SimpleNamespace(ChatCompletion=object(), api_key=None)
    monkeypatch.setitem(sys.modules, "openai", stub_module)

    loaded = _load_openai()
    assert loaded is stub_module
