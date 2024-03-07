import unittest
from pathfinding import h

class TestHeuristic(unittest.TestCase):
    def test_adjacent_horizontal(self):
        self.assertEqual(h("cell00", "cell01"), 1)

    def test_adjacent_vertical(self):
        self.assertEqual(h("cell00", "cell10"), 1)

    def test_diagonally_adjacent(self):
        self.assertEqual(h("cell00", "cell11"), 2)

    def test_non_adjacent(self):
        self.assertEqual(h("cell00", "cell33"), 6)

    def test_same_cell(self):
        self.assertEqual(h("cell22", "cell22"), 0)

    def test_non_zero_cells(self):
        self.assertEqual(h("cell23", "cell45"), 4)
    
if __name__ == '__main__':
    unittest.main()