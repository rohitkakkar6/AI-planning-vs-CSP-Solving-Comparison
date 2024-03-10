import unittest
from pddl_parser import parse_pddl_file

class TestPDDLParser(unittest.TestCase):
    def test_parse_pddl_file_right_of(self):
        # Define the expected right adjacency rules
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
        right_of, left_of = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed right adjacency rules match the expected rules
        self.assertEqual(right_of, expected_right_of)
    
    def test_parse_pddl_file_left_of(self):
        # Define the expected right adjacency rules
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
        right_of, left_of = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

        # Check if the parsed right adjacency rules match the expected rules
        self.assertEqual(left_of, expected_left_of)

if __name__ == '__main__':
    unittest.main()