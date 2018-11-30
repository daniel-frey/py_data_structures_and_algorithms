from linked_list import LinkedList
import pytest


@pytest.fixture
def empty_ll():
    return LinkedList()


@pytest.fixture
def small_ll():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


@pytest.fixture
def random_ll():
    from random import randint
    ll = LinkedList()
    for num in range(100):
        ll.insert(randint(0, 100))
    return ll


def test_LL_module_exists():
    assert LinkedList


def test_LL_instance_has_none_value_head(empty_ll):
    assert empty_ll.head is None


def test_ll_str_method(empty_ll):
    assert str(empty_ll) == f'Linked List Head val - { empty_ll.head }'


def test_size_of_empty_list(empty_ll):
    assert len(empty_ll) == 0


def test_small_fixture_has_size(small_ll):
    assert len(small_ll) == 4


def test_new_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(1)
    assert empty_ll.head.val == 1


def test_random_ll(random_ll):
    assert len(random_ll) == 100


def test_iterable_as_argument(empty_ll):
    ll = LinkedList([1, 2, 3, 4])
    assert ll.head.val == 4
    assert len(ll) == 4


def test_ll_includes_value(small_ll):
    assert small_ll.includes(3) is True


def test_empty_ll_does_not_include(empty_ll):
    assert empty_ll.includes(4) is False


def test_insert_ll_insert():
    ll = LinkedList()
    assert ll.head is None
    ll.insert('apples')
    assert ll.head.val is 'apples'
    ll.insert('banana')
    assert ll.head.val is 'banana'
    assert ll.head._next.val is 'apples'
