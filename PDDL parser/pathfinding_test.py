import unittest
from pathfinding import aStar, generate_successors, h, moveDown, moveLeft, moveRight, moveUp, reconstruct_path, validifyDown, validifyLeft, validifyRight, validifyUp

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
        
class TestCellMoves(unittest.TestCase):
    def test_moveRight(self):
        self.assertEqual(moveRight("cell00"), "cell01")
        self.assertIsNone(moveRight("cell04"))

    def test_moveLeft(self):
        self.assertEqual(moveLeft("cell01"), "cell00")
        self.assertIsNone(moveLeft("cell00"))

    def test_moveUp(self):
        self.assertEqual(moveUp("cell10"), "cell00")
        self.assertIsNone(moveUp("cell00")) 

    def test_moveDown(self):
        self.assertEqual(moveDown("cell00"), "cell10")
        self.assertIsNone(moveDown("cell40"))

    def test_validifyRight(self):
        self.assertTrue(validifyRight("cell00", "cell01"))
        self.assertFalse(validifyRight("cell00", "cell02"))

    def test_validifyLeft(self):
        self.assertTrue(validifyLeft("cell01", "cell00"))
        self.assertFalse(validifyLeft("cell00", "cell01"))

    def test_validifyUp(self):
        self.assertTrue(validifyUp("cell10", "cell00"))
        self.assertFalse(validifyUp("cell00", "cell10"))

    def test_validifyDown(self):
        self.assertTrue(validifyDown("cell00", "cell10"))
        self.assertFalse(validifyDown("cell10", "cell00"))  
        
class TestGenerateSuccessors(unittest.TestCase):
    def test_center_cell(self):
        self.assertEqual(set(generate_successors("cell22")), {"cell12", "cell32", "cell21", "cell23"})

    def test_edge_cell(self):
        self.assertEqual(set(generate_successors("cell00")), {"cell01", "cell10"})

    def test_corner_cell(self):
        self.assertEqual(set(generate_successors("cell44")), {"cell34", "cell43"})
        
class TestReconstruct(unittest.TestCase):
    def test_reconstruct_path(self):
        came_from = {'cell01': 'cell00', 'cell02': 'cell01', 'cell12': 'cell02'}
        goal = 'cell12'
        expected_path = ['cell00', 'cell01', 'cell02', 'cell12']
        self.assertEqual(reconstruct_path(came_from, goal), expected_path)

class TestaStar(unittest.TestCase):
    def test_aStar_path_found(self):
        expected_path = ['cell43', 'cell33', 'cell23', 'cell13', 'cell03', 'cell02', 'cell01', 'cell00']
        self.assertEqual(aStar(), expected_path)

    
if __name__ == '__main__':
    unittest.main()