import pytest
from .fifo_animal_shelter import AnimalShelter

@pytest.fixture
def empty_queue():
    return AnimalShelter()


@pytest.fixture
def small_queue():
    return AnimalShelter(['dog', 'cat', 'dog', 'cat'])


@pytest.fixture
def dog_queue():
    return AnimalShelter(['dog', 'dog', 'cat'])
