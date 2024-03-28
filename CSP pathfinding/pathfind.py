path_length = 4

#variables
steps = [f"step_{i}" for i in range(1, path_length + 1)]

grid_positions = [(x, y) for x in range(5) for y in range(5)]
domains = {step: grid_positions for step in steps}

print(steps)
print(domains)

# Constraints
def is_adjacent(pos1, pos2):
    row_diff = abs(pos1[0] - pos2[0])
    col_diff = abs(pos1[1] - pos2[1])
    return (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1)

def not_visited(pos, visited):
    return pos not in visited

