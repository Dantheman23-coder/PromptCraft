from __future__ import annotations

from collections.abc import Callable
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

    _FORWARDED_ATTRS = {
        "api_key",
        "base_url",
        "organization",
        "timeout",
        "max_retries",
        "default_headers",
    }

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
        openai_module = object.__getattribute__(self, "_openai_module")
        return getattr(openai_module, name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self._FORWARDED_ATTRS:
            client_kwargs = object.__getattribute__(self, "_client_kwargs")
            if value is None or (name in {"api_key", "base_url", "organization"} and value == ""):
                client_kwargs.pop(name, None)
            else:
                client_kwargs[name] = value
            object.__setattr__(self, "_client", None)
        else:
            openai_module = object.__getattribute__(self, "_openai_module")
            setattr(openai_module, name, value)


def _default_import_openai() -> Any:
    import openai as _openai  # type: ignore[import-not-found]

    return _openai


def _load_openai(importer: Callable[[], Any] | None = None) -> _OpenAIProtocol:
    """Return the OpenAI ChatCompletion client or a helpful stub."""

    importer = importer or _default_import_openai

    try:  # pragma: no cover - exercised indirectly via tests
        _openai = importer()
    except ModuleNotFoundError as exc:  # pragma: no cover - behaviour asserted in tests
        missing_exc = exc

        class _MissingChatCompletion:
            @staticmethod
            def create(*args: Any, **kwargs: Any) -> Any:
                raise RuntimeError(
                    "The 'openai' package is required for API interactions. "
                    "Install it with `pip install openai` or configure a mock."
                ) from missing_exc

        return SimpleNamespace(
            ChatCompletion=_MissingChatCompletion,
            api_key=None,
            base_url=None,
            organization=None,
            timeout=None,
            max_retries=None,
            default_headers=None,
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
        if self.settings.openai_api_key and hasattr(openai, "api_key"):
            setattr(openai, "api_key", self.settings.openai_api_key)
        if self.settings.openai_base_url:
            if hasattr(openai, "base_url"):
                setattr(openai, "base_url", self.settings.openai_base_url)
            elif hasattr(openai, "api_base"):
                setattr(openai, "api_base", self.settings.openai_base_url)
        if self.settings.openai_organization and hasattr(openai, "organization"):
            setattr(openai, "organization", self.settings.openai_organization)

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
