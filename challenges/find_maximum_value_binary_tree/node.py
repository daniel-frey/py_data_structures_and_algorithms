class Node:
    """Node class for the binary tree method"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node Val: {}'.format(self.val)

    def __str__(self):
        return str(self.val)
