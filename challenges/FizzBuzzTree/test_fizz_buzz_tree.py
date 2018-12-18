from .fizz_buzz_tree import BST
from .fizz_buzz_tree import fizzbuzztree
from .fizz_buzz_tree import Node
import pytest


def test_create_a_node():
    node = Node(5)
    assert node.left is None
    assert node.right is None


def test_make_empty_bst():
    empty_bst = BST()
    assert empty_bst.root is None


def test_fizzbuzz_is_balanced():
    balanced_bst = BST([10, 7, 3, 16, 15, 8, 20])
    fizzbuzztree(balanced_bst)
    assert balanced_bst.root.val == 'buzz'
    assert balanced_bst.root.right.left.val == 'fizz buzz'
    assert balanced_bst.root.left.left.val == 'fizz'


def test_fizzbuzz_basic():
    basic_bst = BST([1, 2, 3])
    assert basic_bst.root.val == 1
    assert basic_bst.root.right.val == 2
    assert basic_bst.root.right.right.val == 3
    fizzbuzztree(basic_bst)
    assert basic_bst.root.val == 1
    assert basic_bst.root.right.val == 2
    assert basic_bst.root.right.right.val == 'fizz'


def test_fizzbuzz_right():
    right_bst = BST([1, 3, 5, 7, 9, 15, 20, 21, 26])
    fizzbuzztree(right_bst)
    assert right_bst.root.right.val == 'fizz'
    assert right_bst.root.right.right.val == 'buzz'
    assert right_bst.root.right.right.right.right.right.val == 'fizz buzz'
    assert right_bst.root.right.right.right.right.right.right.right.val == 'fizz'


def test_fizzbuzz_left():
    left_bst = BST([30, 10, 8, 6, 3])
    fizzbuzztree(left_bst)
    assert left_bst.root.val == 'fizz buzz'
    assert left_bst.root.left.val == 'buzz'
    assert left_bst.root.left.left.left.left.val == 'fizz'
