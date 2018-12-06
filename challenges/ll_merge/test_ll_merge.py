import pytest
from .ll_merge import LinkedList as LL
from .ll_merge_lists import merge_lists as merge


def test_merge_list(short_ll, long_ll):
    assert merge(short_ll, long_ll) == 5
    assert len(long_ll) == 10


def test_merge_list_one_first(short_ll, long_ll):
    merge(short_ll, long_ll)
    assert long_ll.head.val == 5
    assert long_ll.head._next.val == 11


def test_merge_list_two_first(long_ll, short_ll):
    assert merge(long_ll, short_ll) == 11
    assert len(long_ll) == 10


def test_merge_list_same(short_ll, small_ll):
    assert merge(short_ll, small_ll) == 5
    assert len(small_ll) == 8


def test_merge_list_same_values(short_ll, small_ll):
    merge(short_ll, small_ll)
    assert small_ll.head.val == 5
    assert small_ll.head._next.val == 1
    assert small_ll.head._next._next._next._next._next._next._next.val == 4


def test_merge_list_two_values(long_ll, short_ll):
    merge(long_ll, short_ll)
    assert long_ll.head.val == 11
    assert long_ll.head._next.val == 5


def test_merge_list_empty(short_ll, empty_ll):
    assert merge(short_ll, empty_ll) == 5
    assert len(short_ll) == 4


def test_merge_empty_list_values(short_ll, empty_ll):
    merge(short_ll, empty_ll)
    assert short_ll.head.val == 5
    assert short_ll.head._next.val == 6


def test_merge_empty_list_first(empty_ll, short_ll):
    assert merge(empty_ll, short_ll) == 5
    assert len(short_ll) == 4


def test_merge_empty_list_values(empty_ll, short_ll):
    merge(empty_ll, short_ll)
    assert short_ll.head.val == 5
    assert short_ll.head._next.val == 6
