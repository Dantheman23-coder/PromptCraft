"""Backward-compatible alias for :mod:`promptcraft.cache`."""

from __future__ import annotations

import warnings

from promptcraft.cache import get as _get
from promptcraft.cache import set as _set

warnings.warn(
    "Importing 'cache' from the project root is deprecated; "
    "use 'promptcraft.cache' instead.",
    DeprecationWarning,
    stacklevel=2,
)

get = _get
set = _set

__all__ = ["get", "set"]
