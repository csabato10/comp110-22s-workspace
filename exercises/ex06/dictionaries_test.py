"""Unit tests for dictionary functions."""
 

from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest

__author__ = "730466575"


def test_same_key_in_invert() -> None:
    """Test for the same key in invert."""
    with pytest.raises(KeyError):
        a = {"string": "bean", "pinto": "bean"}
        invert(a)


def test_phrase_invert() -> None:
    """Invert a phrase."""
    a = {"hello": "there", "my": "friend"}
    assert invert(a) == {"there": "hello", "friend": "my"}  


def test_normal_invert() -> None:
    """Invert random dicitonary."""
    a = {"string": "bean", "blue": "bird"}
    assert invert(a) == {"bean": "string", "bird": "blue"}  


def test_all_different_colors() -> None:
    """Test of all the same colors."""
    colors = {"Karl": "orange", "Daniel": "red", "James": "purple"}
    assert favorite_color(colors) == "orange"


def test_tie_colors() -> None:
    """Test for a tie in colors."""
    colors = {"Karl": "purple", "Daniel": "orange", "James": "purple", "Blake": "orange"}
    assert favorite_color(colors) == "purple"


def test_singal_popular_colors():
    """Test for a single popular color."""
    colors = {"Karl": "red", "Daniel": "red", "James": "purple"}
    assert favorite_color(colors) == "red"


def test_all_different_count():
    """Test of list different values."""
    classes = ["math", "science", "english"]
    assert count(classes) == {"math": 1, "science": 1, "english": 1}


def test_repeated_classes_count():
    """Test for repeated values in list."""
    classes = ["math", "science", "english", "science"]
    assert count(classes) == {"math": 1, "science": 2, "english": 1}


def test_no_classes_count():
    """Test for empty list."""
    classes = []
    assert count(classes) == {}