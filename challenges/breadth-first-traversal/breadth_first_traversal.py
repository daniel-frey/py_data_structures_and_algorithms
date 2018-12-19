from queue import Queue


class Node:
    """create a Node"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node Val: {}'.format(self.val)

    def __str__(self):
        return str(self.val)


class BST:
    """Create a BST"""
    def __init__(self, iterable=[]):
        self.root = None
        if type(iterable) is not list:
            raise TypeError
        for item in iterable:
            self.insert(item)

    def __repr__(self):
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        return self.root.val

    def insert(self, val):
        """Insert a node into the BST"""
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break
            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node


def breadth_first_traversal(tree):
    """Perform the BST traversal. This is in-order"""
    queue = Queue()
    traverse = []

    queue.enqueue(tree.root)
    while len(queue) > 0:
        current = queue.dequeue()
        traverse.append(current.val)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return traverse
