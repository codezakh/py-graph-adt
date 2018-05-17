import unittest
from graph import Vertex

class VertexTestCase(unittest.TestCase):
    def test_creating_vertex(self):
        v = Vertex("foo")
        self.assertEqual(v.data, "foo")







if __name__ == "__main__":
    unittest.main()