"""Backward-compatible alias for prompt utilities and models."""

from __future__ import annotations

import warnings

from promptcraft.models.prompt import Prompt as _Prompt
from promptcraft.prompt import rewrite as _rewrite

warnings.warn(
    "Importing 'prompt' from the project root is deprecated; "
    "use 'promptcraft.prompt' or 'promptcraft.models.prompt' instead.",
    DeprecationWarning,
    stacklevel=2,
)

Prompt = _Prompt
rewrite = _rewrite

__all__ = ["Prompt", "rewrite"]
