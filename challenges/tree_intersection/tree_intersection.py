class Node(object):
    def __init__(self, value, data=None, left=None, right=None, _next=None):
        """Instantiate the first node of the object."""
        self.value = value
        self.data = data
        self.left = left
        self.right = right
        self._next = _next

    def __str__(self):
        """Return the string of the value."""
        return f'{self.value}'

    def __repr__(self):
        """Return a much prettier formatted string containing the node value, data, left, right, and next.
        """
        return f' <Node | Value: {self.value} | Data: {self.data} | Left: {self.left} | Right: {self.right} | Next: {self._next} >'


class Queue(object):
    """Create the queue class, mush the same as before."""
    def __init__(self, potential_iterable=None):
        """Instantiate the class."""
        self.front = None
        self.back = None
        self._length = 0

        if isinstance(potential_iterable, (list, tuple)):
            for x in potential_iterable:
                self.enqueue(x)

    def __str__(self):
            """Return a string of the top and length of the queue."""
            return f'{self.front} | {self.back}| {self._length}'

    def __repr__(self):
        """Return a formatted string containing the top and length of the queue."""
        return f'<Queue | Front: {self.front} | Back: {self.back}| Length : {self._length}>'

    def __len__(self):
        """Return the length of the queue."""
        return self._length

    def enqueue(self, input):
        """Take in the iterable and return new nodes."""
        new_node = Node(input)
        if not self.front:
            self._length += 1
            self.front = new_node
            self.back = new_node
        else:
            self._length += 1
            temp = self.back
            self.back = new_node
            temp._next = self.back

    def dequeue(self):
        if self.front:
            self._length -= 1
            temp = self.front
            self.front = temp._next
            temp._next = None
            return temp.value
        return('The queue is empty.')


class BinaryTree:
    def __init__(self, iterable=None):
        """Instantiate the binary tree class."""
        self.root = None
        if iterable:
            for i in iterable:
                self.insert(i)

    def __str__(self):
        """String value of the binary tree."""
        return f'{self.value}'

    def __repr__(self):
        """Representation of the binary tree."""
        return f' <Node | Value: {self.root.value} | Root : {self.root}>'

    def insert(self, val):
        """This is the insert method on the class."""
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if val == current.value:
                raise ValueError('This value exists in the tree already.')
            if val > current.value:
                if current.right is None:
                    current.right = new_node
                    return False
                else:
                    current = current.right
            if val < current.value:
                if current.left is None:
                    current.left = new_node
                    return False
                else:
                    current = current.left

    def in_order(self, callable=lambda node: print(node)):
        """Left, root, right order of traversal."""
        def _walk(node=None):
            if node is None:
                return
            if node.left is not None:
                _walk(node.left)
            callable(node)
            if node.right is not None:
                _walk(node.right)
        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """Root, left, right order of traversal."""
        def _walk(node=None):
            if node is None:
                return
            callable(node)
            if node.left is not None:
                _walk(node.left)
            if node.right is not None:
                _walk(node.right)
        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
            """Left, right, root order of traversal."""
            def _walk(node=None):
                if node is None:
                    return
                if node.left is not None:
                    _walk(node.left)
                if node.right is not None:
                    _walk(node.right)
                callable(node)
            _walk(self.root)

    def traverse_breadth_first(self):
        """Return the values of each node in the binary tree."""
        queue = Queue()
        output = []
        queue.enqueue(self.root)
        if queue.front is None:
            return('The binary tree is empty.')
        while len(queue) > 0:
            if queue.front.value.left is not None:
                queue.enqueue(queue.front.value.left)
            if queue.front.value.right is not None:
                queue.enqueue(queue.front.value.right)
            output.append(queue.dequeue().value)
        return output


def tree_intersection(bt1, bt2):
    common = []
    bt_one_list = bt1.traverse_breadth_first()
    bt_two_list = bt2.traverse_breadth_first()
    for item in bt_one_list:
        if item in bt_two_list:
            common.append(item)
        else:
            pass
    return common
