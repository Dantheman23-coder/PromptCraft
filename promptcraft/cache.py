from tinydb import TinyDB, Query
from pathlib import Path

DB_PATH = Path(".cache.json")

db = TinyDB(DB_PATH)


def get(key: str):
    result = db.search(Query().key == key)
    return result[0]["value"] if result else None


def set(key: str, value):
    db.upsert({"key": key, "value": value}, Query().key == key)
