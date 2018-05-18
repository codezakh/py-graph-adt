class Vertex:
    def __init__(self, data):
        self.data = data
        self.incident_edges = {} 

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return 'Vertex("{}")'.format(self.data)

class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start = start_vertex
        self.end = end_vertex
        self.end.incident_edges[self.start] = self

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return "Edge({src}, {end})".format(src=self.start, end=self.end)

class GraphADT:

    def __init__(self):
        self.vertices = set() 
        self.edges = set() 

    @property
    def vertex_count(self):
        return len(self.vertices)

    @property
    def edge_count(self):
        return len(self.edges)

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

    def remove_edge(self, source, endpoint):
        try:
            edge = endpoint.incident_edges.pop(source)
        except KeyError:
            raise ValueError("Edge {}->{} does not exist".format(
                source, 
                endpoint))
        else:
            self.edges.remove(edge)

