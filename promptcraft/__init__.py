"""PromptCraft package."""

from ._version import __version__ as __version__
from .prompt import rewrite as rewrite

__all__ = ["__version__", "rewrite"]
