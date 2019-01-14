class Node:
    def __init__(self, val, _next=None):
        """Initialize the class with value
        """
        self.val = val
        self._next = _next

    def __str__(self):
        """Return a string
        """
        return f'{self.val}'

    def __repr__(self):
        """Return a more highly formatted string
        """
        return f' <Node | Val: {self.val} | Next: {self._next}>'


class Stack(object):
    """Create a stack class with methods below
    """
    def __init__(self, potential_iterable=None):
        """Initialize the function, define datatype as always a node
        """
        self.top: Node = None
        self._length: int = 0
        if potential_iterable is iter:
            try:
                for i in potential_iterable:
                    self.pop(i)
            except TypeError:
                self.pop()

    def __str__(self):
            """Return a string of the top and the length
            """
            return f'{self.top} | Length: {self._length}'

    def __repr__(self):
        """Return a formatted string of the top and the length of the stack
        """
        return f'<Stack | Top: {self.top} | Length : {self._length}>'

    def __len__(self):
        """Return the length
        """
        return self._length

    def push(self, val):
        """Create a new node and add to the top of the stack
        """
        self.top = Node(val, self.top)
        self._length += 1
        return self.top

    def pop(self):
        """Pop the value from the top of the stack
        """
        temporary = self.top
        self.top = temporary._next
        temporary._next = None
        self._length -= 1
        return temporary.val

    def peek(self):
        """Return the value from the top of the stack without changing it.
        """
        return self.top


class Graph:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return(f'Graph: {self.graph}')

    def __str__(self):
        return f'{self.graph}'

    def __len__(self):
        return len(self.graph)

    def add_vert(self, val):
        """ add vertex to the graph and check to see if value already exists
        """
        if self.has_vert(val):
            raise LookupError
        self.graph[val] = {}

    def has_vert(self, val):
        """Check for the key in the graph (if exists)
        """
        if val in self.graph:
            return True
        else:
            return False

    def add_edge(self, v1, v2, weight):
        """Add the vertex value
        """
        if self.has_vert(v1) and self.has_vert(v2):
            try:
                if self.graph[v1][v2]:
                    raise LookupError
            except KeyError:
                self.graph[v1][v2] = weight

    def get_neighbors(self, val):
        """Return if empty otherwise get the neighbors
        """
        if self.has_vert(val):
            return self.graph[val].keys()
        else:
            return([])

    def depth_first_graph(self, start, x=lambda x: print(x)):
        """Graph traversal - left then right
        """
        explored = []
        output = []
        explored.append(start)
        stack = Stack()
        stack.push(start)
        while stack._length:
            output.append(stack.pop())
            for neighbor in self.graph[output[-1]].keys():
                if neighbor not in explored:
                    stack.push(neighbor)
                    explored.append(neighbor)
        return output
