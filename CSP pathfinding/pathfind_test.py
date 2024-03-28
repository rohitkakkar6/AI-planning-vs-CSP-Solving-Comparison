import unittest
from pathfind import is_adjacent, not_visited

class TestIsAdjacent(unittest.TestCase):
    def test_adjacent_positions(self):
        self.assertTrue(is_adjacent((0, 0), (0, 1))) # Right
        self.assertTrue(is_adjacent((0, 2), (0, 1))) # Left
        self.assertTrue(is_adjacent((0, 0), (1, 0))) # Down
        self.assertTrue(is_adjacent((1, 0), (0, 0))) # Up
    
    def test_non_adjacent_positions(self):
        self.assertFalse(is_adjacent((0, 0), (2, 0))) # Far Down
        self.assertFalse(is_adjacent((0, 0), (0, 2))) # Far Right
        self.assertFalse(is_adjacent((1, 1), (2, 2))) # Diagonal
        
 
class TestVisitedFunction(unittest.TestCase):
    def test_not_visited_basic(self):
        visited = [(0, 1), (1, 1), (2, 1)]
        pos = (3, 1)
        self.assertTrue(not_visited(pos, visited), "Position should be considered not visited.")

    def test_not_visited_already_visited(self):
        visited = [(0, 1), (1, 1), (2, 1)]
        pos = (1, 1)
        self.assertFalse(not_visited(pos, visited), "Position should be considered visited.")

    def test_not_visited_empty_visited(self):
        visited = []
        pos = (0, 0)
        self.assertTrue(not_visited(pos, visited), "With an empty visited list, any position should be considered not visited.")

    def test_not_visited_border_position(self):
        visited = [(0, 0), (0, 1), (0, 2)]
        pos = (0, 3)
        self.assertTrue(not_visited(pos, visited), "Border position should be considered not visited if not in the visited list.")

 
if __name__ == '__main__':
    unittest.main()