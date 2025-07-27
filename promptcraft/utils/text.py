"""Text utilities."""

def shorten(text: str, length: int) -> str:
    return text if len(text) <= length else text[:length].rstrip() + "..."
