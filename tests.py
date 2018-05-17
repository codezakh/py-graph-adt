import unittest

from graph import Vertex, Edge

class VertexTestCase(unittest.TestCase):
    def test_creating_vertex(self):
        v = Vertex("foo")
        self.assertEqual(v.data, "foo")


class EdgeTestCase(unittest.TestCase):
    def test_creating_edge(self):
        u, v = Vertex("foo"), Vertex("bar")
        e = Edge(u, v)
        self.assertIs(e.start, u)
        self.assertIs(e.end, v)



if __name__ == "__main__":
    unittest.main()