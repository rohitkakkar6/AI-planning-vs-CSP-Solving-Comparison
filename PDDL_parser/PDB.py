from pddl_parser import *
from aStar import *
import re

class Chunk:
    def __init__(self):
        self.cells = []
        self.entry_points = {}
        self.exit_points = {}
        self.paths = {}

    def add_cell(self, cell_name):
        self.cells.append(cell_name)
    
    def add_entry_point(self, point, direction):
        self.entry_points[point] = direction

    def add_exit_point(self, point, direction):
        self.exit_points[point] = direction

    def get_entry_points(self):
        return self.entry_points

    def get_exit_points(self):
        return self.exit_points

    def add_path(self, entry, exit, path, cost):
        if entry not in self.paths:
            self.paths[entry] = {}
        self.paths[entry][exit] = {'path': path, 'cost': cost}

def cell_to_chunk(x, y, chunk_size=3):
    return (x // chunk_size, y // chunk_size)

def initialize_chunks(max_x, max_y, chunk_size=3):
    chunk_map = {}
    for x in range(0, max_x + 1, chunk_size):
        for y in range(0, max_y + 1, chunk_size):
            chunk_coord = cell_to_chunk(x, y, chunk_size)
            chunk_map[chunk_coord] = Chunk()
    return chunk_map

def identify_and_store_entry_exit_points(chunk_map, right_of, left_of, is_above, is_underneath, chunk_size=3):
    for chunk_coord, chunk in chunk_map.items():
        for cell in chunk.cells:
            col, row = map(int, re.findall(r'\d+', cell))
            adjacent_cells = [
                (right_of.get(cell), 'right'),
                (left_of.get(cell), 'left'), 
                (is_above.get(cell), 'up'),
                (is_underneath.get(cell), 'down')
            ]
            
            for adjacent_cell, direction in adjacent_cells:
                if adjacent_cell:
                    adj_col, adj_row = map(int, re.findall(r'\d+', adjacent_cell))
                    if cell_to_chunk(row, col, chunk_size) != cell_to_chunk(adj_row, adj_col, chunk_size):
                        if direction == 'right' or direction == 'down':
                            chunk.add_exit_point((col, row), direction)
                        else:
                            chunk.add_entry_point((col, row), direction)

def filter_adjacencies_for_chunk(chunk, right_of, left_of, is_above, is_underneath):
    filtered = {
        "right_of": {},
        "left_of": {},
        "is_above": {},
        "is_underneath": {}
    }
    for cell in chunk.cells:
        if cell in right_of and right_of[cell] in chunk.cells:
            filtered["right_of"][cell] = right_of[cell]
        if cell in left_of and left_of[cell] in chunk.cells:
            filtered["left_of"][cell] = left_of[cell]
        if cell in is_above and is_above[cell] in chunk.cells:
            filtered["is_above"][cell] = is_above[cell]
        if cell in is_underneath and is_underneath[cell] in chunk.cells:
            filtered["is_underneath"][cell] = is_underneath[cell]
    return filtered


right_of, left_of, is_above, is_underneath, start, goal = parse_pddl_file('PDDL pathfinding/problem.pddl')
all_cells = set(right_of.keys()) | set(left_of.keys()) | set(is_above.keys()) | set(is_underneath.keys())
max_x = max_y = 0
for cell in all_cells:
    x, y = map(int, re.findall(r'\d+', cell))
    max_x, max_y = max(max_x, x), max(max_y, y)
chunk_map = initialize_chunks(max_x, max_y)
for cell in all_cells:
    x, y = map(int, re.findall(r'\d+', cell))
    chunk_coord = cell_to_chunk(x, y)
    chunk_map[chunk_coord].add_cell(cell)
identify_and_store_entry_exit_points(chunk_map, right_of, left_of, is_above, is_underneath)
