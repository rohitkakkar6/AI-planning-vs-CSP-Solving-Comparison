import unittest
from pathfinding import h

class TestHeuristic(unittest.TestCase):
    def test_manhattendistance(self):
        self.assertEqual(h((0, 0), (0, 5)), 5)
        
    def test_incorrectinput(self):
        with self.assertRaises(TypeError):
            h(("a", "b"), (0, 1))
    
if __name__ == '__main__':
    unittest.main()