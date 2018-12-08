from .node import Node

class Queue:
    """Create a queue (yes, Scott it is spelled correctly)"""
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Invalid iterable')
        for item in iterable:
            self.enqueue(item)

    def __repr__(self):
        return f'Front of the queue is { self.front.val }'

    def __str__(self):
        return f'Front of the queue is { self.front.val }'

    def __len__(self):
        return self._size

    def enqueue(self, val):
        """Method to add a node to the queue"""
        try:
            node = Node(val)
        except TypeError:
            return self.back
        self._size += 1
        if self.front is None:
            self.front = node
            self.back = node
        self.back._next = node
        self.back = node
        return self.front

    def dequeue(self):
        """Method to remove a node from the queue"""
        if self._size == 0:
            raise IndexError('Queue is empty')
        dequeued_node = self.front
        self.front = self.front._next
        self._size -= 1
        return dequeued_node.val
