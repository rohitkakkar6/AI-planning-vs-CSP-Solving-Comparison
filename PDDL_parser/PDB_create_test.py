import unittest
import unittest
from PDB_create import cell_to_chunk, initialize_chunks, adjacent_cell_and_chunk

class Tests(unittest.TestCase):
    def test_cell_to_chunk(self):
        self.assertEqual(cell_to_chunk(4, 4), (1, 1))
        self.assertEqual(cell_to_chunk(5, 5), (1, 1))
        self.assertEqual(cell_to_chunk(6, 6), (2, 2))

    def test_initialize_chunks(self):
        chunk_map = initialize_chunks(2, 2)
        self.assertEqual(len(chunk_map), 1)
        self.assertTrue((0, 0) in chunk_map)

    def test_adjacent_cell_and_chunk(self):
        cell, chunk = adjacent_cell_and_chunk(["cellx1y1"], "up", (1, 1))
        self.assertEqual(cell, "cellx1y0")
        self.assertEqual(chunk, (1, 0))

        # Test moving right from a cell within a chunk
        cell, chunk = adjacent_cell_and_chunk(["cellx1y1"], "right", (1, 1))
        self.assertEqual(cell, "cellx2y1")
        self.assertEqual(chunk, (2, 1))

        # Test moving down from a cell within a chunk
        cell, chunk = adjacent_cell_and_chunk(["cellx1y1"], "down", (1, 1))
        self.assertEqual(cell, "cellx1y2")
        self.assertEqual(chunk, (1, 2))

        # Test moving left from a cell within a chunk
        cell, chunk = adjacent_cell_and_chunk(["cellx1y1"], "left", (1, 1))
        self.assertEqual(cell, "cellx0y1")
        self.assertEqual(chunk, (0, 1))

if __name__ == '__main__':
    unittest.main()