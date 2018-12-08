import pytest
from .node import Node
from .stack import Stack


def test_create_invalid_stack():
    with pytest.raises(TypeError) as err:
        Stack(1)
    assert str(err.value) == 'Invalid iterable'


def test_make_valid_stack(empty_stack):
    assert empty_stack.top is None
    assert len(empty_stack) == 0


def test_push_incorrect(small_stack):
    assert small_stack.push(None).val == 5


def test_push_single_node(empty_stack):
    assert empty_stack.push(1).val == 1
    assert len(empty_stack) == 1


def test_push_a_few_into_stack(empty_stack):
    assert empty_stack.push(2).val == 2
    assert empty_stack.push(3).val == 3
    assert len(empty_stack) == 2


def test_make_correctly_formed_small_stack(small_stack):
    assert small_stack.top.val == 5
    assert small_stack.top._next.val == 4
    assert len(small_stack) == 5


def test_make_correctly_formed_large_stack(large_stack):
    assert large_stack.top.val == 10
    assert large_stack.top._next.val == 9
    assert len(large_stack) == 10


def test_pop(small_stack):
    assert small_stack.pop() == 5
    assert small_stack.top.val == 4
    assert len(small_stack) == 4


def test_single_pop(empty_stack):
    empty_stack.push(1)
    assert empty_stack.pop() == 1
    assert len(empty_stack) == 0


def test_two_pops(large_stack):
    large_stack.pop()
    assert large_stack.pop() == 9
    assert len(large_stack) == 8


def test_peek(small_stack):
    assert small_stack.top.val == 5


def test_peek_large(large_stack):
    assert large_stack.top.val == 10


def test_peek_small_next(small_stack):
    small_stack.push(6)
    assert small_stack.top.val == 6
