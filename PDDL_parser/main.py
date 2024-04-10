from pddl_parser import *
from aStar import aStar

# Parse the PDDL file to get the maze structure
right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/problem.pddl')

all_cells = set(right_of.keys()) | set(left_of.keys()) | set(is_above.keys()) | set(is_underneath.keys())

max_row = max_col = 0

# Iterate over the combined set of cell identifiers
for cell in all_cells:
    col = int(re.search(r'x(\d+)', cell).group(1))
    row = int(re.search(r'y(\d+)', cell).group(1))
    max_row = max(max_row, row)
    max_col = max(max_col, col)

# Adjust grid_size based on the maximum row and column values found
grid_size = max(max_row, max_col) + 1

# Call the A* algorithm with the start and goal points
path = aStar(right_of, left_of, is_above, is_underneath, start, goal, grid_size, (0, 0))

if path:
    print("Path found:", path)
else:
    print("No path found.")
