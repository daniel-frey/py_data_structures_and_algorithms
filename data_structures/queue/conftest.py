import pytest
from .queue import Queue


@pytest.fixture
def empty_queue():
    """Create an empty queue for testing purposes."""
    return Queue()


@pytest.fixture
def small_queue():
    """Create a small queue for testing purposes."""
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    que.enqueue(5)
    return que


@pytest.fixture
def large_queue():
    """Create a large queue for testing purposes."""
    que = Queue()
    for num in range(1, 11):
        que.enqueue(num)
    return que

