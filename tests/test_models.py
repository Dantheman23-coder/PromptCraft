from promptcraft.models import Prompt, Score, Session, User


def test_models():
    Prompt(text="hi")
    Score(clarity=1, context=1, constraints=1, intent=1, overall=1)
    Session(user_id="u")
    User(id="u", name="test")
