from .array_binary_search import binary_search
import pytest


def test_assert_binary_search():
    assert binary_search


def test_finds_indexed_odd_num():
    expected = 4
    actual = binary_search([1, 2, 3, 4, 5, 6], 5)
    assert expected == actual

def test_finds_indexed_even_num_():
    expected = 4
    actual = binary_search([1, 2, 4, 5, 6, 7], 6)
    assert expected == actual


def test_works_if_blank_arr():
    expected = -1
    actual = binary_search([], 2)
    assert expected == actual
