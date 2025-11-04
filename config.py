"""Backward-compatible alias for :mod:`promptcraft.config`."""

from __future__ import annotations

import warnings

from promptcraft.config import Settings as _Settings
from promptcraft.config import get_settings as _get_settings

warnings.warn(
    "Importing 'config' from the project root is deprecated; "
    "use 'promptcraft.config' instead.",
    DeprecationWarning,
    stacklevel=2,
)

Settings = _Settings
get_settings = _get_settings

__all__ = ["Settings", "get_settings"]
