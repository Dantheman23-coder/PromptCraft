from ..prompt import rewrite


def boss_mode(text: str) -> str:
    """Challenging rewrite with critique."""
    first = rewrite(text)
    second = rewrite(first)
    return f"First draft:\n{first}\nImproved:\n{second}"
