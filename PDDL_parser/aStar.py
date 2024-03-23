from queue import PriorityQueue
from pddl_parser import *
import re

right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/5x5_pathfinding.pddl')

def h(cell1, cell2):
    # Extract x and y coordinates using regular expressions
    x1, y1 = map(int, re.findall(r'(\d+)', cell1))
    x2, y2 = map(int, re.findall(r'(\d+)', cell2))
    return abs(x1 - x2) + abs(y1 - y2)

def validifyRight(cell1, cell2):
    return right_of.get(cell1) == cell2

def validifyLeft(cell1, cell2):
    return left_of.get(cell1) == cell2

def validifyUp(cell1, cell2):
    return is_above.get(cell1) == cell2

def validifyDown(cell1, cell2):
    return is_underneath.get(cell1) == cell2

def moveRight(cell):
    return right_of.get(cell)

def moveLeft(cell):
    return left_of.get(cell)

def moveUp(cell):
    return is_above.get(cell)

def moveDown(cell):
    return is_underneath.get(cell)

def generate_successors(current_cell):
    successors = []
    
    right_cell = moveRight(current_cell)
    if right_cell and validifyRight(current_cell, right_cell):
        successors.append(right_cell)

    left_cell = moveLeft(current_cell)
    if left_cell and validifyLeft(current_cell, left_cell):
        successors.append(left_cell)

    up_cell = moveUp(current_cell)
    if up_cell and validifyUp(current_cell, up_cell):
        successors.append(up_cell)

    down_cell = moveDown(current_cell)
    if down_cell and validifyDown(current_cell, down_cell):
        successors.append(down_cell)

    return successors

def aStar():
    max_row = max_col = 0

# Iterate over the adjacency relations to find the maximum row and column indices
    for cell in right_of.keys():
        # Extract row and column indices using regular expressions
        row_match = re.search(r'x(\d+)', cell)
        col_match = re.search(r'y(\d+)', cell)
        
        if row_match and col_match:
            row = int(row_match.group(1))
            col = int(col_match.group(1))
            max_row = max(max_row, row)
            max_col = max(max_col, col)

    grid_size = (max_row + 1)

    # Initialize g_score and f_score dictionaries in file input formatting
    g_score = {f"cellx{row}y{col}": float('inf') for row in range(grid_size) for col in range(grid_size)}
    f_score = {f"cellx{row}y{col}": float('inf') for row in range(5) for col in range(5)}

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
        
        for child_cell in generate_successors(current_cell):
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
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()  # Reverse the path to start from the beginning
    return path
