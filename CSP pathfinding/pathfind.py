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

def select_unassigned_variable(assignment, steps):
    for step in steps:
        if step not in assignment:
            return step
    return None

# Consistency checker
def is_consistent(step, pos, assignment, is_adjacent, visited):
    if not not_visited(pos, visited):
        return False
    
    if assignment:
        previous_step_number = int(step.split('_')[1]) - 1
        if previous_step_number > 0:
            previous_step = f"step_{previous_step_number}"
            if previous_step in assignment:
                last_step_pos = assignment[previous_step]
                if not is_adjacent(last_step_pos, pos):
                    return False
    return True