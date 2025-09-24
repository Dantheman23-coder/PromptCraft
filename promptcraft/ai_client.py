from __future__ import annotations

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


def _load_openai() -> _OpenAIProtocol:
    """Return the OpenAI ChatCompletion client or a helpful stub.

    Importing ``openai`` at module load time makes tests fail when the optional
    dependency is not installed.  Instead we lazily import the module and fall
    back to a stub that raises a descriptive error when actually invoked.  Test
    suites can still monkeypatch ``promptcraft.ai_client.openai`` thanks to the
    attribute assignment below.
    """

    try:  # pragma: no cover - exercised indirectly via tests
        import openai as _openai
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
