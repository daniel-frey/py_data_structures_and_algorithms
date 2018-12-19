from breadth_first_traversal import BST
from breadth_first_traversal import breadth_first_traversal


def test_breadth_first_traversal():
    """Test the breadth first traversal"""
    tree = BST([2, 1, 3])
    assert breadth_first_traversal(tree) == [2, 1, 3]


def test_breadth_first_traversal_only_root():
    """Test with only a root node"""
    tree = BST([1])
    assert breadth_first_traversal(tree) == [1]


def test_breadth_first_traversal_not_a_number():
    """Test with a value not a number"""
    tree = BST(['demi', 'scott'])
    assert breadth_first_traversal(tree) == ['demi', 'scott']


def test_breadth_first_traversal_empty_tree():
    """Test an empty tree"""
    tree = BST([])
    assert breadth_first_traversal(tree) == []


def test_breadth_first_traversal_balanced():
    """Test a balanced tree"""
    tree = BST([10, 7, 3, 16, 12, 8, 20])
    assert breadth_first_traversal(tree) == [10, 7, 16, 3, 8, 12, 20]


def test_breadth_first_traversal_right():
    """Test traversing the right side"""
    tree = BST([1, 3, 5, 7, 9])
    assert breadth_first_traversal(tree) == [1, 3, 5, 7, 9]
