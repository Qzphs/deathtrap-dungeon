import pytest

from game.pages import PAGES


def test_text():
    assert PAGES[0].top.startswith("Down in the dark")
    assert PAGES[0].bottom.startswith("Despite its name")
    assert PAGES[400].top.startswith("As soon as you appear")
    assert PAGES[400].bottom == ""


def test_newlines():
    assert "\n" in PAGES[0].top
