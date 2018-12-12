from .fifo_animal_shelter import AnimalShelter
import pytest


def test_empty_shelter(empty_queue):
    """Test the empty queue"""
    assert empty_queue.front is None
    assert empty_queue.back is None
    assert empty_queue._size == 0


def test_make_invalid_queue():
    """Test an invalid argument"""
    with pytest.raises(TypeError) as err:
        AnimalShelter(1)
    assert str(err.value) == 'Invalid'


def test_enqueue_invalid(small_queue):
    """Test an invalid argument on the small queue"""
    with pytest.raises(ValueError):
        small_queue.enqueue(None)


def test_dequeue_invalid(empty_queue):
    """Test the empty queue dequeue method"""
    with pytest.raises(IndexError) as err:
        empty_queue.dequeue()
    assert str(err.value) == 'the shelter is empty!'


def test_enqueue_invalid(small_queue):
    """Test the enqueue invalid method"""
    with pytest.raises(ValueError):
        small_queue.enqueue('hyena')


def test_instantiate_with_iterable():
    """Test the correct iterable"""
    animals = AnimalShelter(['dog', 'dog', 'cat'])
    assert animals._size == 3
    assert animals.front.val == 'dog'
    assert animals.back.val == 'cat'


def test_enqueue_a_dog(empty_queue):
    """add a dog to the shelter"""
    empty_queue.enqueue('dog')
    assert empty_queue.front.val == 'dog'
    assert empty_queue._size == 1


def test_enqueue_a_cat(empty_queue):
    """Add cat to the shelter"""
    empty_queue.enqueue('cat')
    assert empty_queue.front.val == 'cat'
    assert empty_queue._size == 1


def test_enqueue_twice(empty_queue):
    """Enqueue both a dog and a cat"""
    empty_queue.enqueue('dog')
    empty_queue.enqueue('cat')
    assert empty_queue._size == 2
    assert empty_queue.front.val == 'dog'


def test_dequeue_none(small_queue):
    """Adopt a dog"""
    assert small_queue.dequeue() == 'dog'
    assert small_queue.front.val == 'cat'


def test_dequeue_dog(small_queue):
    """Fill the shelter"""
    assert small_queue.dequeue('dog') == 'dog'
    assert small_queue.front.val == 'cat'
    assert small_queue._size == 3


def test_dequeue_cat(small_queue):
    """Adobt a cat"""
    assert small_queue.dequeue('cat') == 'cat'
    assert small_queue._size == 3
    assert small_queue.front.val == 'dog'


def test_dequeue_cat_values(small_queue):
    """Adopt a cat"""
    small_queue.dequeue('cat')
    assert small_queue.front._next.val == 'dog'
    assert small_queue.front._next._next.val == 'cat'


def test_dequeue_cat_dog_queue(dog_queue):
    """Adopt a cat from the dog queue"""
    assert dog_queue.dequeue('cat') == 'cat'
    assert dog_queue._size == 2


def test_dequeue_cat_dog_vals(dog_queue):
    """Adopt a car from the dog queue"""
    dog_queue.dequeue('cat')
    assert dog_queue.front.val == 'dog'
    assert dog_queue.front._next.val == 'dog'


def test_dequeue_dog_queue(dog_queue):
    """Adopt a dog from the dog queue"""
    assert dog_queue.dequeue('dog') == 'dog'
    assert dog_queue.front.val == 'dog'
    assert dog_queue._size == 2


def test_dequeue_not_dog_or_cat(dog_queue):
    """Adopt an animal that doesn't exist"""
    with pytest.raises(ValueError):
        dog_queue.dequeue('hound')
