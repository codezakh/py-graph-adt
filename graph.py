class Vertex:
    def __init__(self, data):
        self.data = data
        self.incident_edges = {} 

    def __hash__(self):
        return id(self)

class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start = start_vertex
        self.end = end_vertex
        self.end.incident_edges[self.start] = self

    def __hash__(self):
        return id(self)

class GraphADT:
    vertices = set() 
    edges = set() 

    @property
    def vertex_count(self):
        return len(self.vertices)

    def add_vertex(self, data):
        vertex = Vertex(data)
        self.vertices.add(vertex)
        return vertex

    def add_edge(self, source, endpoint):
        edge = Edge(source, endpoint)
        self.edges.add(edge)
        return edge

    def get_adjacent(self, vertex):
        for edge in self.edges:
            if edge.start is vertex:
                yield edge.end