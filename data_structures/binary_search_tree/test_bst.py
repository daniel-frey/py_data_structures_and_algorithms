from .bst import BST
from .bst import Node
import pytest


def test_create_node():
    node = Node(5)
    assert node.left is None
    assert node.right is None


def test_binary_tree_insert_after_root():
    binarytree = BST([4])
    binarytree.insert(6)
    assert binarytree.root.val == 4
    assert binarytree.root.right.val == 6


def test_binary_tree_right_and_left_access():
    binarytree = BST([4])
    binarytree.insert(6)
    binarytree.insert(2)
    assert binarytree.root.val == 4
    assert binarytree.root.right.val == 6
    assert binarytree.root.left.val == 2


def test_bst_access_right_child_has_left():
    binarytree = BST([1, 3])
    binarytree.insert(2)
    assert binarytree.root.val == 1
    assert binarytree.root.right.val == 3
    assert binarytree.root.right.left.val == 2


def test_bst_created_with_iterable():
    binarytree = BST([1, 2, 3])
    assert binarytree.root.val == 1
    assert binarytree.root.right.val == 2
    assert binarytree.root.right.right.val == 3


def test_bst_invalid_iterable():
    with pytest.raises(TypeError):
        BST(1)


def test_make_empty_bst():
    empty_bst = BST()
    assert empty_bst.root is None


def test_walk_none_node_post_order():
    empty_bst = BST()
    assert empty_bst.post_order(lambda n: print(n)) is None


def test_bst_created_with_iterable_four():
    binarytree = BST([1, 3, 2, 4])
    assert binarytree.root.val == 1
    assert binarytree.root.right.left.val == 2
    assert binarytree.root.right.right.val == 4


def test_insert_single_is_root():
    empty_bst = BST()
    empty_bst.insert(3)
    assert empty_bst.root.val == 3


def test_bst_insert():
    binarytree = BST([1, 2, 5])
    binarytree.insert(3)
    assert binarytree.root.val == 1
    assert binarytree.root.right.val == 2
    assert binarytree.root.right.right.left.val == 3
    assert binarytree.root.right.right.val == 5


def test_insert_balance(balanced_bst):
    balanced_bst.insert(9)
    assert balanced_bst.root.left.right.right.val == 9


def test_fixture_left(left_weighted):
    assert left_weighted.root.val == 10
    assert left_weighted.root.left.val == 8
    assert left_weighted.root.left.left.val == 6
    assert left_weighted.root.left.left.left.val == 4


def test_fixture_right(right_weighted):
    assert right_weighted.root.val == 1
    assert right_weighted.root.right.val == 3
    assert right_weighted.root.right.right.val == 5
    assert right_weighted.root.right.right.right.val == 7
    assert right_weighted.root.right.right.right.right.val == 9


def test_fixture_balanced(balanced_bst):
    assert balanced_bst.root.val == 10
    assert balanced_bst.root.left.val == 7
    assert balanced_bst.root.left.left.val == 3
    assert balanced_bst.root.left.right.val == 8
    assert balanced_bst.root.right.val == 16
    assert balanced_bst.root.right.left.val == 12
    assert balanced_bst.root.right.right.val == 20


def test_in_order_operation():
    b = BST([1, 3, 2])
    order = []
    b.in_order(lambda n: order.append(n.val))
    assert order == [1, 2, 3]


def test_in_order_operation_balance_in_order(balanced_bst):
    order = []
    balanced_bst.in_order(lambda n: order.append(n.val))
    assert order == [3, 7, 8, 10, 12, 16, 20]


def test_pre_order_operation_balance_pre_order(balanced_bst):
    order = []
    balanced_bst.pre_order(lambda n: order.append(n.val))
    assert order == [10, 7, 3, 8, 16, 12, 20]


def test_post_order_operation_balance_post_order(balanced_bst):
    order = []
    balanced_bst.post_order(lambda n: order.append(n.val))
    assert order == [3, 8, 7, 12, 20, 16, 10]


def test_in_order_operation_right_in_order(right_weighted):
    order = []
    right_weighted.in_order(lambda n: order.append(n.val))
    assert order == [1, 3, 5, 7, 9]


def test_pre_order_operation_right_heavy(right_weighted):
    order = []
    right_weighted.pre_order(lambda n: order.append(n.val))
    assert order == [1, 3, 5, 7, 9]


def test_post_order_operation_right_heavy(right_weighted):
    order = []
    right_weighted.post_order(lambda n: order.append(n.val))
    assert order == [9, 7, 5, 3, 1]


def test_in_order_operation_left_heavy(left_weighted):
    order = []
    left_weighted.in_order(lambda n: order.append(n.val))
    assert order == [4, 6, 8, 10]


def test_pre_order_operation_left_heavy(left_weighted):
    order = []
    left_weighted.pre_order(lambda n: order.append(n.val))
    assert order == [10, 8, 6, 4]


def test_post_order_operation_left_heavy(left_weighted):
    order = []
    left_weighted.post_order(lambda n: order.append(n.val))
    assert order == [4, 6, 8, 10]


def test_walk_none_node_in_order():
    empty_bst = BST()
    assert empty_bst.in_order(lambda n: print(n)) is None


def test_walk_none_node_pre_order():
    empty_bst = BST()
    assert empty_bst.pre_order(lambda n: print(n)) is None
