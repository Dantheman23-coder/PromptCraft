from promptcraft.cache import set, get


def test_cache_roundtrip(tmp_path):
    key = "foo"
    value = "bar"
    set(key, value)
    assert get(key) == value
