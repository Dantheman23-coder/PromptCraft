from promptcraft.search import keyword_search, semantic_search


def test_keyword_search():
    corpus = ["hello world", "foo bar"]
    assert keyword_search("hello", corpus) == ["hello world"]


def test_semantic_search():
    corpus = ["hello world", "foo bar"]
    assert semantic_search("hello world", corpus)[0] == "hello world"
