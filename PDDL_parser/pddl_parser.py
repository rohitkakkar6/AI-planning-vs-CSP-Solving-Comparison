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
            right_of_matches = re.findall(r'\s*\(right-of (\S+) (\S+)\)', line)
            if right_of_matches:
                for match in right_of_matches:
                    right_of[match[1]] = match[0]
            
            # Left adjacency rules
            left_of_matches = re.findall(rf'\s*\(left-of (\S+) (\S+)\)', line)
            if left_of_matches:
                for match in left_of_matches:
                    left_of[match[1]] = match[0]
                    
            # Above adjacency rules
            is_above_matches = re.findall(rf'\s*\(is-above (\S+) (\S+)\)', line)
            if is_above_matches:
                for match in is_above_matches:
                    is_above[match[1]] = match[0]
            
            # Underneath adjacency rules
            is_underneath_matches = re.findall(rf'\s*\(is-underneath (\S+) (\S+)\)', line)
            if is_underneath_matches:
                for match in is_underneath_matches:
                    is_underneath[match[1]] = match[0]

            # (at X) matches
            is_at_matches = re.findall(rf'\s*\(at cellx(\d+)y(\d+)\)', line)
            if is_at_matches:
                for match in is_at_matches:
                    x, y = match
                    cell_name = 'cellx' + x + 'y' + y
                    is_at.append(cell_name)
        
        start = is_at[0]
        goal = is_at[1]

    return right_of, left_of, is_above, is_underneath, start, goal


right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

print(start)
print(goal)
