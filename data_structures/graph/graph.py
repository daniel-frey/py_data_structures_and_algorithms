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
        """Add an individual vertex to a graph"""
        if self.has_vert(val):
            raise LookupError
        self.graph[val] = {}

    def has_vert(self, val):
        """Check to find a specific value in a graph"""
        if val in self.graph:
            return True
        else:
            return False

    def add_edge(self, v1, v2, weight):
        """ Add an endge between vertex in a graph"""
        if self.has_vert(v1) and self.has_vert(v2):
            try:
                if self.graph[v1][v2]:
                    raise LookupError
            except KeyError:
                self.graph[v1][v2] = weight

    def get_neighbors(self, val):
        """Find the neighbors for a given value in a graph"""
        if self.has_vert(val):
            return self.graph[val].keys()
        else:
            return([])

