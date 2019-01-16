from .tree_intersection import tree_intersection, BinaryTree, Queue
import pytest


@pytest.fixture
def small_tree():
    tree = BinaryTree()
    tree.insert(3)
    tree.insert(11)
    tree.insert(27)
    return tree


@pytest.fixture
def large_tree():
    tree = BinaryTree()
    tree.insert(11)
    tree.insert(2)
    tree.insert(3)
    tree.insert(12)
    tree.insert(44)
    tree.insert(27)
    tree.insert(1)
    return tree


@pytest.fixture
def tiny_tree():
    tree = BinaryTree()
    tree.insert(0)
    return tree


@pytest.fixture
def same_tree():
    tree = BinaryTree()
    tree.insert(0)
    return tree


def test_bts_have_same_values(small_tree, large_tree):
    assert tree_intersection(small_tree, large_tree) == [3, 11, 27]


def test_binary_trees_do_not_have_the_same_values(small_tree, tiny_tree):
    assert tree_intersection(small_tree, tiny_tree) == []


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    return queue


def test_queue():
    assert small_queue


def test_create_queue_instance():
    queue = Queue()
    assert isinstance(queue, Queue)


def test_property_front(empty_queue):
    assert empty_queue.front is None


def test_root_value(small_tree):
    """Test that the small tree contains a root value."""
    assert small_tree.root.value == 3


def test_small_tree_has_no_root(small_tree):
    """Test that there is no left child of the small tree."""
    assert small_tree.root.left is None


def test_small_tree_has_root_value(small_tree):
    """Test that there is a value of the right child in the small tree."""
    assert small_tree.root.right.value == 11


def test_small_tree_has_right_child_child(small_tree):
    """Test that there is a right child of the small tree."""
    assert small_tree.root.right.right.value == 27


def test_root_large_tree_value(large_tree):
    """Test the root value of the larger of the two trees."""
    assert large_tree.root.value == 11
