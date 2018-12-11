from .queue_with_stacks import KindaQueue
import pytest

@pytest.fixture
def empty_queue():
    queue = KindaQueue()
    return queue

@pytest.fixture
def small_queue():
    queue = KindaQueue()
    queue.enqueue(1)
    return queue

@pytest.fixture
def larger_queue():
    queue = KindaQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue


def test_the_empty_method(empty_queue):
    """Test that the will return the appropriate output for f string"""
    assert str(empty_queue) == f'<Queue Length: 0>'


def test_the_repr(empty_queue):
    """Test the repr method for correct f string output"""
    assert repr(empty_queue) == f'<Queue Length: 0>'


def test_enqueue_method(empty_queue):
    """Test the enqueue method on the empty queue"""
    assert len(empty_queue) == 0
    empty_queue.enqueue(1)
    assert len(empty_queue) == 1


def test_enqueue_method_two(small_queue):
    """Test the enqueue method a second time"""
    assert len(small_queue) == 3
    small_queue.enqueue(4)
    assert len(small_queue) == 4


def test_dequeue_method(larger_queue):
    """Test the dequeue method on the larger queue"""
    assert len(larger_queue) == 3
    larger_queue.dequeue()
    assert len(larger_queue) == 2


def test_dequeue_of_empty_queue(empty_queue):
    """Test the error handling"""
    with pytest.raises(ValueError) as e:
        empty_queue.dequeue()
    assert 'The queue is already empty' in str(e)


def test_dequeue_of_one_value(small_queue):
    """Test that one item is dequeued"""
    assert small_queue.dequeue() == 1


def test_dequque_on_larger_queue(larger_queue):
    """Tests the dequque method running through an entire queue"""
    assert larger_queue.dequeue() == 1
    assert larger_queue.dequeue() == 2
    assert larger_queue.dequeue() == 3
