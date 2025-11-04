"""Backward-compatible alias for :mod:`promptcraft.models.score`."""

from __future__ import annotations

import warnings

from promptcraft.models.score import Score as _Score

warnings.warn(
    "Importing 'score' from the project root is deprecated; "
    "use 'promptcraft.models.score' instead.",
    DeprecationWarning,
    stacklevel=2,
)

Score = _Score

__all__ = ["Score"]
