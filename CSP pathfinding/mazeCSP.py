from pyamaze import maze, agent

# Constraints
def is_adjacent(pos1, pos2):
    """
    Determines if two positions on a grid are adjacent to each other.

    Args:
        pos1 (tuple): A tuple representing the coordinates of the first position in the format (row, column).
        pos2 (tuple): A tuple representing the coordinates of the second position in the format (row, column).

    Return:
        bool: True if the positions are adjacent, False otherwise.
    """
    row_diff = abs(pos1[0] - pos2[0])
    col_diff = abs(pos1[1] - pos2[1])
    return (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1)

def not_visited(pos, visited):
    """
    Checks if a position has not been visited before.

    Args:
        pos (tuple): A tuple representing the coordinates of the position to check.
        visited (list): A list of tuples representing positions that have already been visited.

    Return:
        bool: True if the position has not been visited, False otherwise.
    """
    return pos not in visited

def is_move_allowed(maze_map, current, next):
    """
    Determines if a move from the current position to the next position is allowed in a maze.

    Args:
        maze_map (dict): A dictionary representing the maze map.
        current (tuple): A tuple representing the current position in the format (x, y).
        next (tuple): A tuple representing the next position in the format (x, y).

    Return:
        bool: True if the move is allowed, False otherwise.
    """
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
    """
    Selects an unassigned variable from a list of steps.

    Args:
        assignment (list): A list of steps representing variables that have already been assigned.
        steps (list): A list of steps representing all possible variables.

    Return:
        Any: An unassigned variable if found, otherwise None.
    """
    for step in steps:
        if step not in assignment:
            return step
    return None

# Consistency checker
def is_consistent(step, pos, assignment, visited, mazeGrid):
    """
    Checks if assigning a position to a step is consistent with the current assignment and maze conditions.

    Args:
        step (str): A string representing the current step.
        pos (tuple): A tuple representing the coordinates of the position to check in the maze.
        assignment (dict): A dictionary representing the current assignment of steps to positions.
        visited (list): A list of tuples representing positions that have already been visited.
        mazeGrid (dict): A dictionary representing the maze map.

    Return:
        bool: True if assigning the position to the step is consistent, False otherwise.
    """
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
    """
    Assigns a position to a step and updates the assignment and visited lists.

    Args:
        step (str): A string representing the step to assign the position to.
        pos (tuple): A tuple representing the coordinates of the position to assign.
        assignment (dict): A dictionary representing the current assignment of steps to positions.
        visited (list): A list of tuples representing positions that have already been visited.

    Return:
        None
    """
    assignment[step] = pos
    visited.append(pos)

def unassign(step, assignment, visited):
    """
    Unassigns a position from a step and updates the assignment and visited lists if the step is assigned.

    Args:
        step (str): A string representing the step to assign the position to.
        pos (tuple): A tuple representing the coordinates of the position to assign.
        assignment (dict): A dictionary representing the current assignment of steps to positions.
        visited (list): A list of tuples representing positions that have already been visited.

    Return:
        None
    """
    if step in assignment:
        pos = assignment.pop(step)
        visited.remove(pos)

def goal_test(assignment, steps, goal_pos):
    """
    Checks if the current assignment satisfies the goal condition.

    Args:
        assignment (dict): A dictionary representing the current assignment of steps to positions.
        steps (list): A list of steps representing the order in which positions are visited.
        goal_pos (tuple): A tuple representing the goal position.

    Return:
        bool: True if the current assignment satisfies the goal condition, False otherwise.
    """
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
    """
    Uses backtracking to find a solution to the maze traversal problem.

    Args:
        assignment (dict): A dictionary representing the current assignment of steps to positions.
        steps (list): A list of steps representing the order in which positions are visited.
        domains (dict): A dictionary representing the domains of each step, i.e., the possible positions they can have.
        visited (list): A list of tuples representing positions that have already been visited.
        goal_pos (tuple): A tuple representing the goal position.
        mazeGrid (dict): A dictionary representing the maze map.

    Return:
        dict or None: A dictionary representing the assignment if a solution is found, otherwise None.
    """
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

def iterative_deepening(start_pos, goal_pos, grid_size, mazeGrid, max_depth=150):
    """
    Performs iterative deepening search to find a solution to the maze traversal problem.

    Args:
        start_pos (tuple): A tuple representing the starting position.
        goal_pos (tuple): A tuple representing the goal position.
        grid_size (int): The size of the grid (assumed to be square).
        mazeGrid (dict): A dictionary representing the maze map.
        max_depth (int, optional): The maximum depth to explore during iterative deepening.

    Return:
        dict or None: A dictionary representing the assignment if a solution is found, otherwise None.
    """
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
goal_pos = (14,14)

grid_size = 15
m = maze(grid_size, grid_size)
m.CreateMaze()
# Set the agent's start position
a = agent(m, 1, 1)

# Set the maze's goal (end point) explicitly
m.goal = (grid_size, grid_size)  # Bottom-right corner

mazeGrid = m.maze_map

solution = iterative_deepening(start_pos, goal_pos, grid_size, mazeGrid)

# m.run() # Used to visualise grid