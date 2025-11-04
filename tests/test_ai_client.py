import importlib
import sys
from types import SimpleNamespace

import pytest

from promptcraft.ai_client import AIClient, _OpenAIShim, _load_openai
from promptcraft.config import get_settings


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


def test_openai_shim_forwards_settings_and_reinitialises():
    stub_module = _StubOpenAIModule()
    shim = _OpenAIShim(stub_module)

    shim.api_key = "abc"
    shim.base_url = "https://example.test"
    shim.ChatCompletion.create(model="gpt", messages=[{"role": "user", "content": "hi"}])
    assert stub_module.created_with == [
        {"api_key": "abc", "base_url": "https://example.test"}
    ]
    assert stub_module.requests == [
        {"model": "gpt", "messages": [{"role": "user", "content": "hi"}]}
    ]

    shim.api_key = None
    shim.base_url = None
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


def test_ai_client_applies_environment_configuration(monkeypatch):
    monkeypatch.setenv("PROMPTCRAFT_OPENAI_API_KEY", "promptcraft-key")
    monkeypatch.setenv("PROMPTCRAFT_OPENAI_BASE_URL", "https://promptcraft.local")

    stub_client = SimpleNamespace(
        ChatCompletion=SimpleNamespace(
            create=lambda **kwargs: SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))]
            )
        ),
        api_key=None,
        base_url=None,
    )

    monkeypatch.setattr("promptcraft.ai_client.openai", stub_client)

    client = AIClient()

    assert stub_client.api_key == "promptcraft-key"
    assert stub_client.base_url == "https://promptcraft.local"
    assert client.chat("hi") == "ok"


def test_get_settings_prefers_promptcraft_environment(monkeypatch):
    monkeypatch.setenv("PROMPTCRAFT_OPENAI_API_KEY", "promptcraft-key")
    monkeypatch.setenv("OPENAI_API_KEY", "global-key")
    monkeypatch.setenv("PROMPTCRAFT_OPENAI_BASE_URL", "https://promptcraft.local")
    monkeypatch.setenv("OPENAI_BASE_URL", "https://openai.local")

    settings = get_settings()

    assert settings.openai_api_key == "promptcraft-key"
    assert settings.openai_base_url == "https://promptcraft.local"


def test_get_settings_falls_back_to_openai_environment(monkeypatch):
    monkeypatch.delenv("PROMPTCRAFT_OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("PROMPTCRAFT_OPENAI_BASE_URL", raising=False)
    monkeypatch.setenv("OPENAI_API_KEY", "global-key")
    monkeypatch.setenv("OPENAI_BASE_URL", "https://openai.local")

    settings = get_settings()

    assert settings.openai_api_key == "global-key"
    assert settings.openai_base_url == "https://openai.local"
