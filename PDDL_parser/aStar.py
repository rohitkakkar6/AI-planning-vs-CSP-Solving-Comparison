from queue import PriorityQueue
from pddl_parser import *
import re

right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/problem.pddl')

def h(cell1, cell2):
    """
    Calculates the Manhattan distance heuristic between two cells in a grid.

    Args:
        cell1 (str): The coordinate of the first cell in the format 'cellx{x_coord}y{y_coord}'.
        cell2 (str): The coordinate of the second cell in the format 'cellx{x_coord}y{y_coord}'.

    Return:
        int: The Manhattan distance between the two cells.
    """
    x1, y1 = map(int, re.findall(r'(\d+)', cell1))
    x2, y2 = map(int, re.findall(r'(\d+)', cell2))
    return abs(x1 - x2) + abs(y1 - y2)

def validifyRight(cell1, cell2, right_of):
    """
    Checks if `cell2` is validly right of `cell1` according to the provided `right_of` dictionary.

    Args:
        cell1 (str): The coordinate of the first cell.
        cell2 (str): The coordinate of the second cell.
        right_of (dict): A dictionary representing right-of relationships between cells.

    Return:
        bool: True if `cell2` is validly right of `cell1`, False otherwise.
    """
    return right_of.get(cell1) == cell2

def validifyLeft(cell1, cell2, left_of):
    """
    Checks if `cell2` is validly left of `cell1` according to the provided `left_of` dictionary.

    Args:
        cell1 (str): The coordinate of the first cell.
        cell2 (str): The coordinate of the second cell.
        left_of (dict): A dictionary representing left-of relationships between cells.

    Return:
        bool: True if `cell2` is validly left of `cell1`, False otherwise.
    """
    return left_of.get(cell1) == cell2

def validifyUp(cell1, cell2, is_above):
    """
    Checks if `cell2` is validly above `cell1` according to the provided `is_above` dictionary.

    Args:
        cell1 (str): The coordinate of the first cell.
        cell2 (str): The coordinate of the second cell.
        is_above (dict): A dictionary representing is-above relationships between cells.

    Return:
        bool: True if `cell2` is validly above `cell1`, False otherwise.
    """
    return is_above.get(cell1) == cell2

def validifyDown(cell1, cell2, is_underneath):
    """
    Checks if `cell2` is validly underneath `cell1` according to the provided `is_underneath` dictionary.

    Args:
        cell1 (str): The coordinate of the first cell.
        cell2 (str): The coordinate of the second cell.
        is_underneath (dict): A dictionary representing is-underneath relationships between cells.

    Return:
        bool: True if `cell2` is validly underneath `cell1`, False otherwise.
    """
    return is_underneath.get(cell1) == cell2

def moveRight(cell):
    """
    Gets the cell that is right of the given cell.

    Args:
        cell (str): The coordinate of the cell.

    Return:
        str: The coordinate of the cell right of the given cell, or None if not found.
    """
    return right_of.get(cell)

def moveLeft(cell):
    """
    Gets the cell that is left of the given cell.

    Args:
        cell (str): The coordinate of the cell.

    Return:
        str: The coordinate of the cell left of the given cell, or None if not found.
    """
    return left_of.get(cell)

def moveUp(cell):
    """
    Gets the cell that is above the given cell.

    Args:
        cell (str): The coordinate of the cell.

    Return:
        str: The coordinate of the cell above the given cell, or None if not found.
    """
    return is_above.get(cell)

def moveDown(cell):
    """
    Gets the cell that is underneath the given cell.

    Args:
        cell (str): The coordinate of the cell.

    Return:
        str: The coordinate of the cell underneath the given cell, or None if not found.
    """
    return is_underneath.get(cell)

def generate_successors(current_cell, right_of, left_of, is_above, is_underneath):
    """
    Generates the successor cells of the given current cell based on the provided relationships.

    Args:
        current_cell (str): The coordinate of the current cell.
        right_of (dict): A dictionary representing right-of relationships between cells.
        left_of (dict): A dictionary representing left-of relationships between cells.
        is_above (dict): A dictionary representing is-above relationships between cells.
        is_underneath (dict): A dictionary representing is-underneath relationships between cells.

    Return:
        list: A list of successor cells of the given current cell.
    """
    successors = []
    
    right_cell = moveRight(current_cell)
    if right_cell and validifyRight(current_cell, right_cell, right_of):
        successors.append(right_cell)

    left_cell = moveLeft(current_cell)
    if left_cell and validifyLeft(current_cell, left_cell, left_of):
        successors.append(left_cell)

    up_cell = moveUp(current_cell)
    if up_cell and validifyUp(current_cell, up_cell, is_above):
        successors.append(up_cell)

    down_cell = moveDown(current_cell)
    if down_cell and validifyDown(current_cell, down_cell, is_underneath):
        successors.append(down_cell)

    return successors

def aStar(right_of, left_of, is_above, is_underneath, start, goal, grid_size, top_corner):
    """
    Finds the shortest path from the start cell to the goal cell using the A* algorithm.

    Args:
        right_of (dict): A dictionary representing right-of relationships between cells.
        left_of (dict): A dictionary representing left-of relationships between cells.
        is_above (dict): A dictionary representing is-above relationships between cells.
        is_underneath (dict): A dictionary representing is-underneath relationships between cells.
        start (str): The coordinate of the start cell.
        goal (str): The coordinate of the goal cell.
        grid_size (int): The size of the grid.
        top_corner (tuple): The coordinates of the top-left corner of the grid.

    Return:
        list or None: The shortest path from the start cell to the goal cell as a list of coordinates,
        or None if no path is found.
    """
    x_min, y_min = top_corner
    g_score = {f"cellx{x}y{y}": float('inf') for x in range(x_min, x_min + grid_size) for y in range(y_min, y_min + grid_size)}
    f_score = {f"cellx{x}y{y}": float('inf') for x in range(x_min, x_min + grid_size) for y in range(y_min, y_min + grid_size)}

    # Set the start cell's g_score to 0 and its f_score to the heuristic estimate to the goal
    g_score[start] = 0
    f_score[start] = h(start, goal)
    
    open_set = PriorityQueue()
    open_set.put((h(start, goal), h(start, goal), start))  # Priority, G-score, Node

    # Track the path taken to reach each node
    came_from = {}
    
    while not open_set.empty():
        current_cell = open_set.get()[2]
        if current_cell == goal:
            break
        
        for child_cell in generate_successors(current_cell, right_of, left_of, is_above, is_underneath):
            temp_g_score = g_score[current_cell] + 1
            temp_f_score = temp_g_score + h(child_cell, goal)

            if temp_f_score < f_score[child_cell]:
                g_score[child_cell] = temp_g_score
                f_score[child_cell] = temp_f_score
                open_set.put((temp_f_score, temp_g_score, child_cell))
                came_from[child_cell] = current_cell
    
    if current_cell == goal:
        return reconstruct_path(came_from, goal)
    else:
        return None

def reconstruct_path(came_from, goal):
    """
    Reconstructs the path from the start cell to the goal cell using the 'came_from' dictionary.

    Args:
        came_from (dict): A dictionary containing the path information.
        goal (str): The coordinate of the goal cell.

    Return:
        list: The reconstructed path from the start cell to the goal cell as a list of coordinates.
    """
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()
    return path
