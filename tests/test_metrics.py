from promptcraft.metrics import score_prompt


def test_score_prompt():
    score = score_prompt("short prompt")
    assert 0 <= score.overall <= 100
