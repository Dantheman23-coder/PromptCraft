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


    _FORWARDED_ATTRS = {"api_key", "base_url"}

        object.__setattr__(self, "_client_kwargs", {})
    def _create_chat_completion(
        self,
        *,
        model: str,
        messages: list[dict[str, str]],
        **kwargs: Any,
    ) -> Any:
            client_kwargs: dict[str, Any] = dict(
                object.__getattribute__(self, "_client_kwargs")
            )
        if name in self._FORWARDED_ATTRS:
            client_kwargs = object.__getattribute__(self, "_client_kwargs")
            return client_kwargs.get(name)
        if name in self._FORWARDED_ATTRS:
            client_kwargs = object.__getattribute__(self, "_client_kwargs")
            if value in (None, ""):
                client_kwargs.pop(name, None)
            else:
                client_kwargs[name] = value
    try:  # pragma: no cover - exercised indirectly via tests
            base_url: str | None = None
        return SimpleNamespace(
            ChatCompletion=_MissingOpenAI.ChatCompletion,
            api_key=None,
            base_url=None,
        )
        if hasattr(openai, "base_url") and self.settings.openai_base_url:
            setattr(openai, "base_url", self.settings.openai_base_url)
    except ModuleNotFoundError as exc:  # pragma: no cover - behaviour asserted in tests
        class _MissingOpenAI:
            class ChatCompletion:
                @staticmethod
                def create(*args: Any, **kwargs: Any) -> Any:
                    raise RuntimeError(
                        "The 'openai' package is required for API interactions. "
                        "Install it with `pip install openai` or configure a mock."
                    ) from exc

        return SimpleNamespace(ChatCompletion=_MissingOpenAI.ChatCompletion)

        _openai = importlib.import_module("openai")
        missing_exc = exc


                    ) from missing_exc
# expose a module-level attribute so tests can monkeypatch it easily
openai: _OpenAIProtocol = _load_openai()


class AIClient:
    def __init__(self, model: str = "gpt-4o"):
        self.model = model
        self.settings = get_settings()
        # Configure API key if the real client is available
        if hasattr(openai, "api_key") and self.settings.openai_api_key:
            setattr(openai, "api_key", self.settings.openai_api_key)

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
