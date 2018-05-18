class Vertex:
    def __init__(self, data):
        self.data = data
        self.incident_edges = set() 


class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start = start_vertex
        self.end = end_vertex
        self.end.incident_edges.add(self)

    def __hash__(self):
        return id(self)

class GraphADT:
    vertices = []
    edges = []

    @property
    def vertex_count(self):
        return len(self.vertices)

    def add_vertex(self, data):
        self.vertices.append(Vertex(data))