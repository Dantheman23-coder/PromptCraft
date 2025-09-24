"""TinyDB-backed cache with a graceful in-memory fallback."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

DB_PATH = Path(".cache.json")

try:  # pragma: no cover - behaviour exercised via tests
    from tinydb import Query, TinyDB
except ModuleNotFoundError:  # pragma: no cover
    TinyDB = None  # type: ignore[assignment]
    Query = None  # type: ignore[assignment]
else:
    _db = TinyDB(DB_PATH)


if TinyDB is not None:
    def get(key: str) -> Any | None:
        """Retrieve ``key`` from the persistent TinyDB cache."""

        result = _db.search(Query().key == key)
        return result[0]["value"] if result else None


    def set(key: str, value: Any) -> None:
        """Store ``value`` under ``key`` in the persistent TinyDB cache."""

        _db.upsert({"key": key, "value": value}, Query().key == key)
else:
    _CACHE: Dict[str, Any] = {}

    def get(key: str) -> Any | None:
        """Retrieve ``key`` from the in-memory cache."""

        return _CACHE.get(key)


    def set(key: str, value: Any) -> None:
        """Store ``value`` under ``key`` in the in-memory cache."""

        _CACHE[key] = value
