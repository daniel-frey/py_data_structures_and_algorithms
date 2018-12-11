import pytest
from .stack import Stack

@pytest.fixture
def empty_stack():
    """Empty Stack for testing purposes"""
    return Stack()

@pytest.fixture
def small_stack():
    """Create a small stack, and push new values into the stack for testing purposes"""
    ss = Stack()
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    return ss

@pytest.fixture
def large_stack():
    """Create a large stack, and push values for testing purposes"""
    ls = Stack()
    for num in range(1,11):
        ls.push(num)
    return ls




