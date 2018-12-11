from ...data_structures.stack.stack import Stack


class KindaQueue(object):
    """Kinda looks like a queue, but is actually two stacks working in tandem."""

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self):
        return f'<Queue Length: {len(self)}>'

    def __repr__(self):
        return f'<Queue Length: {len(self)}>'

    def __len__(self):
        return self.stack1._size

    def enqueue(self, value):
        """Add a new value to the Queue"""
        self.stack1.push(value)
        return self

    def dequeue(self):
        """Remove the values in a Queue"""
        if len(self) == 0:
            raise ValueError('The queue is already empty')
        while self.stack1.peek() is not None:
            self.stack2.push(self.stack1.pop().value)

        output = self.stack2.pop()

        while self.stack2.peek() is not None:
            self.stack1.push(self.stack2.pop().value)

        return output.value

