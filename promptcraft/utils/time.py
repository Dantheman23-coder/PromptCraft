"""Time utilities."""

from datetime import datetime


def now() -> str:
    return datetime.utcnow().isoformat()
