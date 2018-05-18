import unittest

from graph import Vertex, Edge, GraphADT

class VertexTestCase(unittest.TestCase):
    def test_creating_vertex(self):
        v = Vertex("foo")
        self.assertEqual(v.data, "foo")

    def test_vtx_contains_incident_edges(self):
        u, v = Vertex("foo"), Vertex("bar")
        e = Edge(u, v)
        self.assertCountEqual(v.incident_edges, [e])

class EdgeTestCase(unittest.TestCase):
    def test_creating_edge(self):
        u, v = Vertex("foo"), Vertex("bar")
        e = Edge(u, v)
        self.assertIs(e.start, u)
        self.assertIs(e.end, v)

class GraphTestCase(unittest.TestCase):
    def test_adding_vertices(self):
        g = GraphADT()
        g.add_vertex("first")
        g.add_vertex("second")
        self.assertEqual(g.vertex_count, 2)

    def test_get_adjacent_vertices(self):
        g = GraphADT()
        vtx_1 = g.add_vertex("first")
        vtx_2 = g.add_vertex("second")
        vtx_3 = g.add_vertex("third")
        edge = g.add_edge(vtx_1, vtx_2)
        self.assertSetEqual(vtx_1.incident_edges, set(edge))


if __name__ == "__main__":
    unittest.main()