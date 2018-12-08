class Node:
    """This is the node object"""
    def __init__(self, val, next=None):
        self.val = val
        self._next = next
        if val is None:
            raise TypeError('Enter a value')

    def __repr__(self):
        return '{ val }'.format(val=self.val)

    def __str__(self):
        return '{ val }'.format(val=self.val)
