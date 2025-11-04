"""Backward-compatible alias for :mod:`promptcraft.ai_client`."""

from __future__ import annotations

import warnings

from promptcraft.ai_client import AIClient as _AIClient
from promptcraft.ai_client import _OpenAIShim as _OpenAIShim
from promptcraft.ai_client import _load_openai as _load_openai
from promptcraft.ai_client import openai as _openai

warnings.warn(
    "Importing 'ai_client' from the project root is deprecated; "
    "use 'promptcraft.ai_client' instead.",
    DeprecationWarning,
    stacklevel=2,
)

AIClient = _AIClient
_OpenAIShim = _OpenAIShim
_load_openai = _load_openai
openai = _openai

__all__ = ["AIClient", "_OpenAIShim", "_load_openai", "openai"]
