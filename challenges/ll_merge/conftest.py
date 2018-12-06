import pytest
from .ll_merge import LinkedList as LL


@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def small_ll():
    return LL([4, 3, 2, 1])


@pytest.fixture
def short_ll():
    return LL([8, 7, 6, 5])


@pytest.fixture
def long_ll():
    return LL([16, 15, 14, 13, 12, 11])
