import unittest
from aStar import aStar, generate_successors, h, moveDown, moveLeft, moveRight, moveUp, reconstruct_path, validifyDown, validifyLeft, validifyRight, validifyUp

class TestHeuristic(unittest.TestCase):
    def test_adjacent_horizontal(self):
        self.assertEqual(h("cellx0y0", "cellx0y1"), 1)

    def test_adjacent_vertical(self):
        self.assertEqual(h("cellx0y0", "cellx1y0"), 1)

    def test_diagonally_adjacent(self):
        self.assertEqual(h("cellx0y0", "cellx1y1"), 2)

    def test_non_adjacent(self):
        self.assertEqual(h("cellx0y0", "cellx3y3"), 6)

    def test_same_cell(self):
        self.assertEqual(h("cellx2y2", "cellx2y2"), 0)

    def test_non_zero_cells(self):
        self.assertEqual(h("cellx2y3", "cellx4y5"), 4)
        
class TestCellMoves(unittest.TestCase):
    def test_moveRight(self):
        self.assertEqual(moveRight("cellx0y0"), "cellx0y1")
        self.assertIsNone(moveRight("cellx0y4"))

    def test_moveLeft(self):
        self.assertEqual(moveLeft("cellx0y1"), "cellx0y0")
        self.assertIsNone(moveLeft("cellx0y0"))

    def test_moveUp(self):
        self.assertEqual(moveUp("cellx1y0"), "cellx0y0")
        self.assertIsNone(moveUp("cellx0y0")) 

    def test_moveDown(self):
        self.assertEqual(moveDown("cellx0y0"), "cellx1y0")
        self.assertIsNone(moveDown("cellx4y0"))

    def test_validifyRight(self):
        self.assertTrue(validifyRight("cellx0y0", "cellx0y1"))
        self.assertFalse(validifyRight("cellx0y0", "cellx0y2"))

    def test_validifyLeft(self):
        self.assertTrue(validifyLeft("cellx0y1", "cellx0y0"))
        self.assertFalse(validifyLeft("cellx0y0", "cellx0y1"))

    def test_validifyUp(self):
        self.assertTrue(validifyUp("cellx1y0", "cellx0y0"))
        self.assertFalse(validifyUp("cellx0y0", "cellx1y0"))

    def test_validifyDown(self):
        self.assertTrue(validifyDown("cellx0y0", "cellx1y0"))
        self.assertFalse(validifyDown("cellx1y0", "cellx0y0"))  
        
class TestGenerateSuccessors(unittest.TestCase):
    def test_center_cell(self):
        self.assertEqual(set(generate_successors("cellx2y2")), {"cellx1y2", "cellx3y2", "cellx2y1", "cellx2y3"})

    def test_edge_cell(self):
        self.assertEqual(set(generate_successors("cellx0y0")), {"cellx0y1", "cellx1y0"})

    def test_corner_cell(self):
        self.assertEqual(set(generate_successors("cellx4y4")), {"cellx3y4", "cellx4y3"})
        
class TestReconstruct(unittest.TestCase):
    def test_reconstruct_path(self):
        came_from = {'cellx0y1': 'cellx0y0', 'cellx0y2': 'cellx0y1', 'cellx1y2': 'cellx0y2'}
        goal = 'cellx1y2'
        expected_path = ['cellx0y0', 'cellx0y1', 'cellx0y2', 'cellx1y2']
        self.assertEqual(reconstruct_path(came_from, goal), expected_path)

class TestaStar(unittest.TestCase):
    def test_aStar_path_found(self):
        expected_path = ['cellx0y2', 'cellx0y3', 'cellx0y4', 'cellx1y4', 'cellx2y4', 'cellx3y4', 'cellx4y4']
        self.assertEqual(aStar(), expected_path)

    
if __name__ == '__main__':
    unittest.main()