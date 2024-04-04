from pyamaze import maze, agent

# Constraints
def is_adjacent(pos1, pos2):
    row_diff = abs(pos1[0] - pos2[0])
    col_diff = abs(pos1[1] - pos2[1])
    return (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1)

def not_visited(pos, visited):
    return pos not in visited

def is_move_allowed(maze_map, current, next):
    # (y,x to x,y and 1,1 to 0,0)
    maze_current = (current[1] + 1, current[0] + 1)
    maze_next = (next[1] + 1, next[0] + 1)

    direction = (maze_next[0] - maze_current[0], maze_next[1] - maze_current[1])
    
    if direction == (1, 0):
        return 'S' in maze_map[maze_current] and maze_map[maze_current]['S'] == 1
    elif direction == (-1, 0):
        return 'N' in maze_map[maze_current] and maze_map[maze_current]['N'] == 1
    elif direction == (0, 1):
        return 'E' in maze_map[maze_current] and maze_map[maze_current]['E'] == 1
    elif direction == (0, -1):
        return 'W' in maze_map[maze_current] and maze_map[maze_current]['W'] == 1
    
    return False

def select_unassigned_variable(assignment, steps):
    for step in steps:
        if step not in assignment:
            return step
    return None

# Consistency checker
def is_consistent(step, pos, assignment, visited, mazeGrid):
    if not not_visited(pos, visited):
        return False
    
    if assignment:
        previous_step_number = int(step.split('_')[1]) - 1
        if previous_step_number > 0:
            previous_step = f"step_{previous_step_number}"
            if previous_step in assignment:
                last_step_pos = assignment[previous_step]
                # Check if the move is adjacent and not blocked by a wall
                if not is_adjacent(last_step_pos, pos) or not is_move_allowed(mazeGrid, last_step_pos, pos):
                    return False
    return True

def assign(step, pos, assignment, visited):
    assignment[step] = pos
    visited.append(pos)

def unassign(step, assignment, visited):
    if step in assignment:
        pos = assignment.pop(step)
        visited.remove(pos)

def goal_test(assignment, steps, goal_pos):
    if len(assignment) != len(steps) or assignment[steps[-1]] != goal_pos:
        return False
    
    visited = set()
    for i, step in enumerate(steps):
        if i == 0 and assignment[step] != start_pos:
            return False
        
        if i > 0:
            prev_step = steps[i - 1]
            if not is_adjacent(assignment[prev_step], assignment[step]) or assignment[step] in visited:
                return False
        
        visited.add(assignment[step])
    return True

def backtrack(assignment, steps, domains, visited, goal_pos, mazeGrid):
    if len(assignment) == len(steps) and goal_test(assignment, steps, goal_pos):
        return assignment
    
    step = select_unassigned_variable(assignment, steps)
    if step is None:
        return None
    
    for pos in domains[step]:
        if is_consistent(step, pos, assignment, visited, mazeGrid):
            assign(step, pos, assignment, visited)
            result = backtrack(assignment, steps, domains, visited, goal_pos, mazeGrid)
            if result is not None:
                return result
            unassign(step, assignment, visited)
    return None

def iterative_deepening(start_pos, goal_pos, grid_size, mazeGrid, max_depth=30):
    for path_length in range(1, max_depth + 1):
        steps = [f"step_{i}" for i in range(1, path_length + 1)]
        grid_positions = [(x, y) for x in range(grid_size) for y in range(grid_size)]
        domains = {step: grid_positions for step in steps}
        visited = [start_pos]
        assignment = {steps[0]: start_pos}
        
        solution = backtrack(assignment, steps, domains, visited, goal_pos, mazeGrid)
        if solution:
            print(f"Solution found with path length {path_length}:", solution)
            return solution
    print("No solution found within the maximum path length.")
    return None


start_pos = (0, 0)
goal_pos = (4,4)

grid_size = 5
m = maze(grid_size, grid_size)
m.CreateMaze()
# Set the agent's start position (e.g., top-left corner)
a = agent(m, 1, 1)

# Set the maze's goal (end point) explicitly
m.goal = (grid_size, grid_size)  # Bottom-right corner

mazeGrid = m.maze_map

solution = iterative_deepening(start_pos, goal_pos, grid_size, mazeGrid)

# m.run() # Used to visualise grid