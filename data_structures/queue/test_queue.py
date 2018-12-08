import pytest
from .queue import Queue


def test_create_empty_queue(empty_queue):
    assert empty_queue.front is None
    assert empty_queue.back is None
    assert len(empty_queue) == 0


def test_create_queue():
    que = Queue([1, 2, 3])
    assert que.front.val == 1
    assert que.back.val == 3


def test_create_invalid_queue():
    with pytest.raises(TypeError) as err:
        Queue(1)
    assert str(err.value) == 'Invalid iterable'


def test_enqueue_single(empty_queue):
    empty_queue.enqueue(3)
    assert empty_queue.front.val == 3
    assert empty_queue.back.val == 3
    assert len(empty_queue) == 1


def test_enqueue(small_queue):
    small_queue.enqueue(6)
    assert small_queue.front.val == 1
    assert small_queue.back.val == 6
    assert len(small_queue) == 6


def test_enqueue_long(large_queue):
    large_queue.enqueue(11)
    assert large_queue.front.val == 1
    assert large_queue.back.val == 11
    assert len(large_queue) == 11


def test_dequeue(small_queue):
    assert small_queue.dequeue() == 1
    assert len(small_queue) == 4


def test_dequeue_small_values(small_queue):
    small_queue.dequeue()
    assert small_queue.front.val == 2
    assert small_queue.back.val == 5


def test_dequeue_large(large_queue):
    assert large_queue.dequeue() == 1
    assert len(large_queue) == 9


def test_dequeue_large_values(large_queue):
    large_queue.dequeue()
    assert large_queue.front.val == 2
    assert large_queue.back.val == 10


def test_dequeue_error_handling(empty_queue):
    with pytest.raises(IndexError) as err:
        empty_queue.dequeue()
    assert str(err.value) == 'Queue is empty'
