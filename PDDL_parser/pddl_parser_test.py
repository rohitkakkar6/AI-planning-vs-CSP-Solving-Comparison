import unittest
from pddl_parser import parse_pddl_file

class TestPDDLParser(unittest.TestCase):
    def test_parse_pddl_file_right_of(self):
        # Defined the expected right adjacency rules
        expected_right_of = {'cellx0y0': 'cellx0y1', 'cellx0y1': 'cellx0y2', 
                             'cellx0y2': 'cellx0y3', 'cellx0y3': 'cellx0y4', 
                             'cellx1y0': 'cellx1y1', 'cellx1y1': 'cellx1y2', 
                             'cellx1y2': 'cellx1y3', 'cellx1y3': 'cellx1y4', 
                             'cellx2y0': 'cellx2y1', 'cellx2y1': 'cellx2y2', 
                             'cellx2y2': 'cellx2y3', 'cellx2y3': 'cellx2y4', 
                             'cellx3y0': 'cellx3y1', 'cellx3y1': 'cellx3y2', 
                             'cellx3y2': 'cellx3y3', 'cellx3y3': 'cellx3y4', 
                             'cellx4y0': 'cellx4y1', 'cellx4y1': 'cellx4y2', 
                             'cellx4y2': 'cellx4y3', 'cellx4y3': 'cellx4y4'
                             }

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed right adjacency rules match the expected rules
        self.assertEqual(right_of, expected_right_of)
    
    def test_parse_pddl_file_left_of(self):
        # Defined the expected left adjacency rules
        expected_left_of = {'cellx0y1': 'cellx0y0', 'cellx0y2': 'cellx0y1', 
                            'cellx0y3': 'cellx0y2', 'cellx0y4': 'cellx0y3', 
                            'cellx1y1': 'cellx1y0', 'cellx1y2': 'cellx1y1', 
                            'cellx1y3': 'cellx1y2', 'cellx1y4': 'cellx1y3', 
                            'cellx2y1': 'cellx2y0', 'cellx2y2': 'cellx2y1', 
                            'cellx2y3': 'cellx2y2', 'cellx2y4': 'cellx2y3', 
                            'cellx3y1': 'cellx3y0', 'cellx3y2': 'cellx3y1', 
                            'cellx3y3': 'cellx3y2', 'cellx3y4': 'cellx3y3', 
                            'cellx4y1': 'cellx4y0', 'cellx4y2': 'cellx4y1', 
                            'cellx4y3': 'cellx4y2', 'cellx4y4': 'cellx4y3'}

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed left adjacency rules match the expected rules
        self.assertEqual(left_of, expected_left_of)
        
    def test_parse_pddl_file_is_above(self):
        # Defined the expected above adjacency rules
        expected_is_above = {'cellx1y0': 'cellx0y0', 'cellx2y0': 'cellx1y0',
                             'cellx3y0': 'cellx2y0', 'cellx4y0': 'cellx3y0',
                             'cellx1y1': 'cellx0y1', 'cellx2y1': 'cellx1y1',
                             'cellx3y1': 'cellx2y1', 'cellx4y1': 'cellx3y1',
                             'cellx1y2': 'cellx0y2', 'cellx2y2': 'cellx1y2',
                             'cellx3y2': 'cellx2y2', 'cellx4y2': 'cellx3y2',
                             'cellx1y3': 'cellx0y3', 'cellx2y3': 'cellx1y3',
                             'cellx3y3': 'cellx2y3', 'cellx4y3': 'cellx3y3',
                             'cellx1y4': 'cellx0y4', 'cellx2y4': 'cellx1y4',
                             'cellx3y4': 'cellx2y4', 'cellx4y4': 'cellx3y4'}

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed above adjacency rules match the expected rules
        self.assertEqual(is_above, expected_is_above)
        
    def test_parse_pddl_file_is_underneath(self):
        # Defined the expected underneath adjacency rules
        expected_is_underneath = {'cellx0y0': 'cellx1y0', 'cellx1y0': 'cellx2y0', 
                                  'cellx2y0': 'cellx3y0', 'cellx3y0': 'cellx4y0', 
                                  'cellx0y1': 'cellx1y1', 'cellx1y1': 'cellx2y1', 
                                  'cellx2y1': 'cellx3y1', 'cellx3y1': 'cellx4y1', 
                                  'cellx0y2': 'cellx1y2', 'cellx1y2': 'cellx2y2', 
                                  'cellx2y2': 'cellx3y2', 'cellx3y2': 'cellx4y2', 
                                  'cellx0y3': 'cellx1y3', 'cellx1y3': 'cellx2y3', 
                                  'cellx2y3': 'cellx3y3', 'cellx3y3': 'cellx4y3', 
                                  'cellx0y4': 'cellx1y4', 'cellx1y4': 'cellx2y4', 
                                  'cellx2y4': 'cellx3y4', 'cellx3y4': 'cellx4y4'}

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed underneath adjacency rules match the expected rules
        self.assertEqual(is_underneath, expected_is_underneath)
        
    def test_parse_pddl_file_start(self):
        # Defined the expected start cell
        expected_start = 'cellx0y2'

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed start matches the expected start
        self.assertEqual(start, expected_start)
    
    def test_parse_pddl_file_goal(self):
        # Defined the expected goal cell
        expected_goal = 'cellx4y4'

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed goal matches the expected goal
        self.assertEqual(goal, expected_goal)

if __name__ == '__main__':
    unittest.main()