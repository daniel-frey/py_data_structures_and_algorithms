class Node(object):
    """
    """
    def __init__(self, val, next=None):
        self.val = val
        self._next = next

    def __str__(self):
        output = f' { self.val }'
        return output
