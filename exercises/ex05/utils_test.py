"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat


__author__ = "730466575"


def test_only_evens_zeros() -> None:
    """Test only evens: zero values."""
    numbs: list[int] = [0, 0, 0]
    assert only_evens(numbs) == [0, 0, 0]


def test_only_evens_one_number() -> None:
    """Test only evens: one integer number."""
    numbs: list[int] = [2, 2, 2]
    assert only_evens(numbs) == [2, 2, 2]


def test_only_evens_some_even() -> None:
    """Test only evens: some even values."""
    numbs: list[int] = [2, 5, 8]
    assert only_evens(numbs) == [2, 8]


def test_sub_empty_list() -> None:
    """Test sub: empty list."""
    b: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(b, start, end) == []


def test_sub_negative_start() -> None:
    """Test sub: negative start index."""
    b: list[int] = [2, 3, 4, 5]
    start: int = -3
    end: int = 2
    assert sub(b, start, end) == [2, 3]


def test_sub_normal_list() -> None:
    """Test sub: normal list."""
    b: list[int] = [2, 3, 4, 5]
    start: int = 1
    end: int = 2
    assert sub(b, start, end) == [3]


def test_sub_negative_end() -> None:
    """Test sub: negative end index."""
    b: list[int] = [2, 3, 4, 5]
    start: int = 1
    end: int = -2
    assert sub(b, start, end) == []


def test_sub_same_large_end() -> None:
    """Test sub: end value out of string length."""
    b: list[int] = [2, 3, 4, 5]
    start: int = 1
    end: int = 8
    assert sub(b, start, end) == [3, 4, 5]


def test_concat_random_numbers() -> None:
    """Test concat: normal values."""
    a: list[int] = [1, 3, 5]
    b: list[int] = [8, 9, 2]
    assert concat(a, b) == [1, 3, 5, 8, 9, 2]


def test_concat_empty_lists() -> None:
    """Test concat: empty list."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


def test_concat_patterened_numbers() -> None:
    """Test concat: patterend numbers."""
    a: list[int] = [1, 5, 1]
    b: list[int] = [5, 1, 5]
    assert concat(a, b) == [1, 5, 1, 5, 1, 5]


def test_concat_zeros() -> None:
    """Test concat: lists of zeros."""
    a: list[int] = [0, 0, 0]
    b: list[int] = [0, 0, 0]
    assert concat(a, b) == [0, 0, 0, 0, 0, 0]
