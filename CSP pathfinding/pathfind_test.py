import unittest
from pathfind import is_adjacent

class TestIsAdjacent(unittest.TestCase):
    def test_adjacent_positions(self):
        self.assertTrue(is_adjacent((0, 0), (0, 1))) # Right
        self.assertTrue(is_adjacent((0, 2), (0, 1))) # Left
        self.assertTrue(is_adjacent((0, 0), (1, 0))) # Down
        self.assertTrue(is_adjacent((1, 0), (0, 0))) # Up
    
    def test_non_adjacent_positions(self):
        self.assertFalse(is_adjacent((0, 0), (2, 0))) # Far Down
        self.assertFalse(is_adjacent((0, 0), (0, 2))) # Far Right
        self.assertFalse(is_adjacent((1, 1), (2, 2))) #Diagonal
        
 
if __name__ == '__main__':
    unittest.main()