from __future__ import annotations

import importlib
from types import SimpleNamespace
from typing import Any, Protocol

from .cache import get, set
from .config import get_settings
from .logger import logger


class _ChatCompletion(Protocol):
    """Protocol describing the subset of the OpenAI Chat API we rely on."""

    @staticmethod
    def create(*, model: str, messages: list[dict[str, str]], **kwargs: Any) -> Any:
        ...


class _OpenAIProtocol(Protocol):
    ChatCompletion: _ChatCompletion


class _OpenAIShim:
    """Compatibility wrapper for the OpenAI 1.x client.

    The 1.x release removed the ``ChatCompletion`` module-level helper and
    requires instantiating :class:`openai.OpenAI`.  This shim exposes an object
    compatible with the legacy interface used throughout the code base while
    lazily constructing the modern client when needed.
    """

    _FORWARDED_ATTRS = {"api_key", "base_url"}

    def __init__(self, openai_module: Any):
        object.__setattr__(self, "_openai_module", openai_module)
        object.__setattr__(self, "_client", None)
        object.__setattr__(self, "_client_kwargs", {})
        object.__setattr__(
            self,
            "ChatCompletion",
            SimpleNamespace(create=self._create_chat_completion),
        )

    def _create_chat_completion(
        self,
        *,
        model: str,
        messages: list[dict[str, str]],
        **kwargs: Any,
    ) -> Any:
        client = object.__getattribute__(self, "_client")
        if client is None:
            client_kwargs: dict[str, Any] = dict(
                object.__getattribute__(self, "_client_kwargs")
            )
            openai_module = object.__getattribute__(self, "_openai_module")
            client = openai_module.OpenAI(**client_kwargs)
            object.__setattr__(self, "_client", client)
        return client.chat.completions.create(model=model, messages=messages, **kwargs)

    def __getattr__(self, name: str) -> Any:
        if name in self._FORWARDED_ATTRS:
            client_kwargs = object.__getattribute__(self, "_client_kwargs")
            return client_kwargs.get(name)
        raise AttributeError(name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self._FORWARDED_ATTRS:
            client_kwargs = object.__getattribute__(self, "_client_kwargs")
            if value in (None, ""):
                client_kwargs.pop(name, None)
            else:
                client_kwargs[name] = value
            object.__setattr__(self, "_client", None)
        else:
            object.__setattr__(self, name, value)


def _load_openai() -> _OpenAIProtocol:
    """Return the OpenAI ChatCompletion client or a helpful stub."""

    try:  # pragma: no cover - exercised indirectly via tests
        _openai = importlib.import_module("openai")
    except ModuleNotFoundError as exc:  # pragma: no cover - behaviour asserted in tests
        missing_exc = exc

        class _MissingOpenAI:
            api_key: str | None = None
            base_url: str | None = None

            class ChatCompletion:
                @staticmethod
                def create(*args: Any, **kwargs: Any) -> Any:
                    raise RuntimeError(
                        "The 'openai' package is required for API interactions. "
                        "Install it with `pip install openai` or configure a mock."
                    ) from missing_exc

        return SimpleNamespace(
            ChatCompletion=_MissingOpenAI.ChatCompletion,
            api_key=None,
            base_url=None,
        )

    if hasattr(_openai, "ChatCompletion"):
        return _openai  # legacy <1.0 API

    if hasattr(_openai, "OpenAI"):
        return _OpenAIShim(_openai)

    return _openai


# expose a module-level attribute so tests can monkeypatch it easily
openai: _OpenAIProtocol = _load_openai()


class AIClient:
    def __init__(self, model: str = "gpt-4o"):
        self.model = model
        self.settings = get_settings()
        # Configure API key if the real client is available
        if hasattr(openai, "api_key") and self.settings.openai_api_key:
            setattr(openai, "api_key", self.settings.openai_api_key)
        if hasattr(openai, "base_url") and self.settings.openai_base_url:
            setattr(openai, "base_url", self.settings.openai_base_url)

    def chat(self, prompt: str) -> str:
        cache_key = f"{self.model}:{prompt}"
        if cached := get(cache_key):
            return cached
        logger.info("Querying OpenAI API")
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        message = response.choices[0].message.content
        set(cache_key, message)
        return message
