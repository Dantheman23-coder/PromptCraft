"""Search utilities."""

from difflib import get_close_matches


def keyword_search(query: str, corpus: list[str]) -> list[str]:
    return [text for text in corpus if query.lower() in text.lower()]


def semantic_search(query: str, corpus: list[str]) -> list[str]:
    return get_close_matches(query, corpus, n=5)
