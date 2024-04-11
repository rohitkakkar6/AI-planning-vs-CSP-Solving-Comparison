from pyamaze import maze, agent

def generate_pddl(maze):
    """
    Generates PDDL representation of a maze problem.

    Args:
        maze (dict): A dictionary representing the maze map.

    Return:
        str: A string representing the PDDL domain definition for the maze problem.
    """
    pddl_str = "(define (problem maze-problem)\n    (:domain maze)\n"

    # Objects
    pddl_str += "    (:objects\n        "
    objects = [f"cellx{x-1}y{y-1}" for (y, x) in maze.keys()]  # Adjust for (y, x) format
    pddl_str += " ".join(objects) + " - cell)\n"

    # Init with the start position
    pddl_str += "    (:init\n        (at cellx0y0)\n"

    # Sets for valid connections
    valid_right_of = set()
    valid_left_of = set()
    valid_is_above = set()
    valid_is_underneath = set()

    for (y, x), dirs in maze.items():
        x_adj, y_adj = x-1, y-1
        current_cell = f"cellx{x_adj}y{y_adj}"

        # East (right-of) connections
        if dirs.get('E'):
            target_cell = f"cellx{x_adj+1}y{y_adj}"
            if (y, x+1) in maze:  # Ensure the target cell exists in maze
                valid_right_of.add((current_cell, target_cell))

        # South (is-underneath) connections
        if dirs.get('S'):
            target_cell = f"cellx{x_adj}y{y_adj+1}"
            if (y+1, x) in maze:  # Ensure the target cell exists in maze
                valid_is_underneath.add((current_cell, target_cell))

        # West (left-of) connections
        if dirs.get('W'):
            target_cell = f"cellx{x_adj-1}y{y_adj}"
            if (y, x-1) in maze:  # Ensure the target cell exists in maze
                valid_left_of.add((current_cell, target_cell))

        # North (is-above) connections
        if dirs.get('N'):
            target_cell = f"cellx{x_adj}y{y_adj-1}"
            if (y-1, x) in maze:  # Ensure the target cell exists in maze
                valid_is_above.add((current_cell, target_cell))

    # Add the valid connections to PDDL
    for right, left in valid_right_of:
        pddl_str += f"        (right-of {left} {right})\n"
        pddl_str += f"        (left-of {right} {left})\n"
    for above, underneath in valid_is_above:
        pddl_str += f"        (is-above {underneath} {above})\n"
        pddl_str += f"        (is-underneath {above} {underneath})\n"
    for underneath, above in valid_is_underneath:
        pddl_str += f"        (is-underneath {above} {underneath})\n"
        pddl_str += f"        (is-above {underneath} {above})\n"
    for left, right in valid_left_of:
        pddl_str += f"        (left-of {right} {left})\n"
        pddl_str += f"        (right-of {left} {right})\n"

    pddl_str += "    )\n"
    
    max_y, max_x = max(maze.keys())
    goal_cell = f"cellx{max_x-1}y{max_y-1}"
    pddl_str += f"    (:goal (\n        (at {goal_cell})\n    )\n)"
    
    pddl_str += ")\n"
    return pddl_str


def main():
    grid_size = 30
    m = maze(grid_size, grid_size)
    m.CreateMaze(loopPercent=21)
    # Set the agent's start position (e.g., top-left corner)
    a = agent(m, 1, 1)

    # Set the maze's goal (end point) explicitly
    m.goal = (grid_size, grid_size)  # Bottom-right corner

    # print(m.maze_map)

    # new_maze = {(1, 1): {'E': 0, 'W': 0, 'N': 0, 'S': 1}, (2, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (3, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (1, 2): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, (2, 2): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (3, 2): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (1, 3): {'E': 0, 'W': 1, 'N': 0, 'S': 0}, (2, 3): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (3, 3): {'E': 0, 'W': 1, 'N': 1, 'S': 0}}

    pddl_content = generate_pddl(m.maze_map)
    
    pddl_file_path = 'PDDL pathfinding/problem.pddl'
    
    # Write the generated PDDL to a file
    with open(pddl_file_path, 'w') as file:
        file.write(pddl_content)

    m.run() # Used to visualise maze

if __name__ == "__main__":
    main()
