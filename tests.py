import unittest

from graph import Vertex, Edge, GraphADT

class VertexTestCase(unittest.TestCase):
    def test_creating_vertex(self):
        v = Vertex("foo")
        self.assertEqual(v.data, "foo")

    def test_vtx_contains_incident_edges(self):
        u, v = Vertex("foo"), Vertex("bar")
        e = Edge(u, v)
        self.assertCountEqual(v.incident_edges, {u: e})


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
        vtx1 = g.add_vertex("first")
        vtx2 = g.add_vertex("second")
        g.add_edge(vtx1, vtx2)
        self.assertEqual(list(g.get_adjacent(vtx1)), [vtx2])

    def test_removing_edge(self):
        g = GraphADT()
        vtx1 = g.add_vertex("first")
        vtx2 = g.add_vertex("second")
        edg1 = g.add_edge(vtx1, vtx2)
        self.assertEqual(g.edge_count, 1)
        g.remove_edge(vtx1, vtx2)
        self.assertEqual(g.edge_count, 0)
        self.assertDictEqual(vtx2.incident_edges, {})

if __name__ == "__main__":
    unittest.main()