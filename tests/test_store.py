import pytest
from session_memory.store import MEMORY, remember


def test_requires_session():
    MEMORY.clear()
    with pytest.raises(ValueError):
        remember("hello")


def test_binds_session():
    MEMORY.clear()
    remember("hello", session_id="a")
    remember("world", session_id="b")
    assert [row["text"] for row in MEMORY["a"]] == ["hello"]
    assert [row["text"] for row in MEMORY["b"]] == ["world"]
