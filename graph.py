class Vertex:
    def __init__(self, data):
        self.data = data


class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start = start_vertex
        self.end = end_vertex