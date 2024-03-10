import re

def parse_pddl_file(file_path):
    right_of = {}
    left_of = {}
    is_above = {}
    is_underneath = {}
    is_at = []

    with open(file_path, 'r') as file:
        for line in file:
            # Right adjacency rules
            right_of_matches = re.findall(rf'\s*\(right-of (\S+) (\S+)\)', line)
            if right_of_matches:
                for match in right_of_matches:
                    right_of[match[1]] = match[0]

            

    return right_of

right_of = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')
