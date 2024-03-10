import unittest
from pddl_parser import parse_pddl_file

class TestPDDLParser(unittest.TestCase):
    def test_parse_pddl_file_right_of(self):
        # Defined the expected right adjacency rules
        expected_right_of = {'cell00': 'cell01', 'cell01': 'cell02', 
                             'cell02': 'cell03', 'cell03': 'cell04', 
                             'cell10': 'cell11', 'cell11': 'cell12', 
                             'cell12': 'cell13', 'cell13': 'cell14', 
                             'cell20': 'cell21', 'cell21': 'cell22', 
                             'cell22': 'cell23', 'cell23': 'cell24', 
                             'cell30': 'cell31', 'cell31': 'cell32', 
                             'cell32': 'cell33', 'cell33': 'cell34', 
                             'cell40': 'cell41', 'cell41': 'cell42', 
                             'cell42': 'cell43', 'cell43': 'cell44'
                             }

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed right adjacency rules match the expected rules
        self.assertEqual(right_of, expected_right_of)
    
    def test_parse_pddl_file_left_of(self):
        # Defined the expected left adjacency rules
        expected_left_of = {'cell01': 'cell00', 'cell02': 'cell01', 
                            'cell03': 'cell02', 'cell04': 'cell03', 
                            'cell11': 'cell10', 'cell12': 'cell11', 
                            'cell13': 'cell12', 'cell14': 'cell13', 
                            'cell21': 'cell20', 'cell22': 'cell21', 
                            'cell23': 'cell22', 'cell24': 'cell23', 
                            'cell31': 'cell30', 'cell32': 'cell31', 
                            'cell33': 'cell32', 'cell34': 'cell33', 
                            'cell41': 'cell40', 'cell42': 'cell41', 
                            'cell43': 'cell42', 'cell44': 'cell43'}

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed left adjacency rules match the expected rules
        self.assertEqual(left_of, expected_left_of)
        
    def test_parse_pddl_file_is_above(self):
        # Defined the expected above adjacency rules
        expected_is_above = {'cell10': 'cell00', 'cell20': 'cell10',
                             'cell30': 'cell20', 'cell40': 'cell30',
                             'cell11': 'cell01', 'cell21': 'cell11',
                             'cell31': 'cell21', 'cell41': 'cell31',
                             'cell12': 'cell02', 'cell22': 'cell12',
                             'cell32': 'cell22', 'cell42': 'cell32',
                             'cell13': 'cell03', 'cell23': 'cell13',
                             'cell33': 'cell23', 'cell43': 'cell33',
                             'cell14': 'cell04', 'cell24': 'cell14',
                             'cell34': 'cell24', 'cell44': 'cell34'}

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed above adjacency rules match the expected rules
        self.assertEqual(is_above, expected_is_above)
        
    def test_parse_pddl_file_is_underneath(self):
        # Defined the expected underneath adjacency rules
        expected_is_underneath = {'cell00': 'cell10', 'cell10': 'cell20', 
                                  'cell20': 'cell30', 'cell30': 'cell40', 
                                  'cell01': 'cell11', 'cell11': 'cell21', 
                                  'cell21': 'cell31', 'cell31': 'cell41', 
                                  'cell02': 'cell12', 'cell12': 'cell22', 
                                  'cell22': 'cell32', 'cell32': 'cell42', 
                                  'cell03': 'cell13', 'cell13': 'cell23', 
                                  'cell23': 'cell33', 'cell33': 'cell43', 
                                  'cell04': 'cell14', 'cell14': 'cell24', 
                                  'cell24': 'cell34', 'cell34': 'cell44'}

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed underneath adjacency rules match the expected rules
        self.assertEqual(is_underneath, expected_is_underneath)
        
    def test_parse_pddl_file_start(self):
        # Defined the expected start cell
        expected_start = 'cell02'

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed start matches the expected start
        self.assertEqual(start, expected_start)
    
    def test_parse_pddl_file_goal(self):
        # Defined the expected goal cell
        expected_goal = 'cell44'

        # Parse the PDDL file
        right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed goal matches the expected goal
        self.assertEqual(goal, expected_goal)

if __name__ == '__main__':
    unittest.main()