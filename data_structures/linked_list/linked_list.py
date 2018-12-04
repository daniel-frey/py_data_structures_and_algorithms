from node import Node


class LinkedList(object):
    """Instantiate a LinkedList."""

    def __init__(self, iterable=None):
        self.head = None
        self.size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be a type of list')

        for val in iterable:
            self.insert(val)

    def __str__(self):
        output = f'Linked List Head val - { self.head }'
        return output

    def __repr__(self):
        output = f'<LinkedList: head - {self.head} size - {self.size}>'
        return output

    def __len__(self):
        return self.size

    def insert(self, value):
        """Insert values into a linked list."""
        node = Node(value)
        node._next = self.head
        self.head = node
        # this line is the same as the three above it.
        # self.head - Node(value, self.head)
        self.size += 1

    def includes(self, value):
        """Find method for linked list.

        Takes in a value as an argument and attempts to find that value in a ll
        """
        current_node = self.head
        while current_node and current_node._next is not None:
            if current_node.val == value:
                return True
            current_node = current_node._next
        return False

    def insertBefore(self, value, newVal):
        """Insert before a given value in a linked list."""
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.val == value:
                if previous_node is None:
                    self.insert(newVal)
                else:
                    new_node = Node(newVal)
                    new_node._next = current_node
                    previous_node._next = new_node
                    self.size += 1
                break
            previous_node = current_node
            current_node = current_node._next

    def insertAfter(self, value, newVal):
        """Insert after a given value in a linked list."""
        current_node = self.head
        while current_node:
            if current_node.val == value:
                position = current_node._next
                current_node._next = Node(newVal)
                current_node._next._next = position
                self.size += 1
                break
            current_node = current_node._next

    def append(self, value):
        """Insert a value to the end of a linked list."""
        if self.head is None:
            self.insert(value)
        else:
            current_node = self.head
            while current_node is not None:
                if current_node._next is None:
                    current_node._next = Node(value)
                    self.size += 1
                    break
                current_node = current_node._next
