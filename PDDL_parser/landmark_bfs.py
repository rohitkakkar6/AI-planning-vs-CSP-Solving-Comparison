from pddl_parser import *
from aStar import *
import re
from queue import PriorityQueue
from collections import defaultdict

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

def calculate_paths_for_chunk(chunk, chunk_coord, right_of, left_of, is_above, is_underneath):
    filtered_adjacencies = filter_adjacencies_for_chunk(chunk, right_of, left_of, is_above, is_underneath)
    entry_points = chunk.get_entry_points()
    exit_points = chunk.get_exit_points()

    if chunk_coord == (0, 0) and (0, 0) in entry_points:
        start_cell = "cellx0y0"
        for exit in exit_points:
            goal_cell = f"cellx{exit[0]}y{exit[1]}"
            path = aStar(filtered_adjacencies["right_of"], filtered_adjacencies["left_of"], filtered_adjacencies["is_above"], filtered_adjacencies["is_underneath"], start_cell, goal_cell, 3, (0, 0))
            if path is not None:
                cost = len(path)
                chunk.add_path((0, 0), exit, path, cost)

    else:
        x, y = chunk_coord
        top_left_x = x * 3
        top_left_y = y * 3
        for entry in entry_points:
            for exit in exit_points:
                start_cell = f"cellx{entry[0]}y{entry[1]}"
                goal_cell = f"cellx{exit[0]}y{exit[1]}"
                path = aStar(filtered_adjacencies["right_of"], filtered_adjacencies["left_of"], filtered_adjacencies["is_above"], filtered_adjacencies["is_underneath"], start_cell, goal_cell, 3, (top_left_x, top_left_y))
                if path is not None:
                    cost = len(path)
                    chunk.add_path(entry, exit, path, cost)


def create_chunk_graph(chunk_map):
    graph = {}
    for chunk_coord, chunk in chunk_map.items():
        graph[chunk_coord] = {}
        for entry, exits in chunk.paths.items():
            graph[chunk_coord][entry] = {}
            for exit, details in exits.items():
                path = details['path']
                cost = details['cost']
                direction = chunk.entry_points.get(entry)
                graph[chunk_coord][entry][exit] = {'path': path, 'cost': cost, 'direction': direction}
    return graph

def adjacent_cell_and_chunk(path, direction, chunk):
    cell = path[0]
    match = re.match(r'cellx(\d+)y(\d+)', cell)
    
    cell_x, cell_y = map(int, match.groups())
    chunk_x, chunk_y = chunk
    
    if direction == 'up':
        return f"cellx{cell_x}y{cell_y - 1}", (chunk_x, chunk_y - 1)
    elif direction == 'down':
        return f"cellx{cell_x}y{cell_y + 1}", (chunk_x, chunk_y + 1)
    elif direction == 'left':
        return f"cellx{cell_x - 1}y{cell_y}", (chunk_x - 1, chunk_y)
    elif direction == 'right':
        return f"cellx{cell_x + 1}y{cell_y}", (chunk_x + 1, chunk_y)
    else:
        return None, None


def adjacent_path(adj_cell, adj_chunk, graph):
    match = re.match(r'cellx(\d+)y(\d+)', adj_cell)
    paths = []
    x, y = map(int, match.groups())
    cell = (x, y)
    # Retrieve the adjacent chunk's data from the graph; if not found, default to an empty dict
    chunk_data = graph.get(adj_chunk, {})
    
    for entry, exits in chunk_data.items():
        for exit, details in exits.items():
            if exit == cell:
                adj_info = adjacent_cell_and_chunk(details['path'], details['direction'], adj_chunk)
                paths.append((details['path'], adj_info, details['direction']))
    
    # Return the list of paths and costs
    return paths

def is_adjacent(cell1, cell2):
    # Extract coordinates
    x1, y1 = map(int, re.findall(r'(\d+)', cell1))
    x2, y2 = map(int, re.findall(r'(\d+)', cell2))
    
    # Check for adjacency (vertical or horizontal)
    return (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1)

def Identify_Landmarks(graph):
    landmarks = set()
    final_landmarks = set()
    paths_to_landmark = []
    adjacent_paths = []
    path_to_goal = []
    precomputed_paths = []

    for entry, exits in graph[(0, 0)].items():
        for exit, details in exits.items():
            path = details['path']
            reversed_path = path[::-1]
            exit_points = path[-1]
            landmarks.add(exit_points)
            path_to_goal.append(path)
    
    for entry, exits in graph[(0, 1)].items():
        for exit, details in exits.items():
            path = details['path']
            reversed_path = path[::-1]
            exit_points = path[0]
            paths_to_landmark.append(path)

    for entry, exits in graph[(1, 0)].items():
        for exit, details in exits.items():
            path = details['path']
            reversed_path = path[::-1]
            exit_points = path[0]
            paths_to_landmark.append(path)
    
    for path in paths_to_landmark:
        first_cell = path[0]  # Get the first cell of the path
        for cell in landmarks:
            if is_adjacent(first_cell, cell):
                adjacent_paths.append(path)
    
    path_groups = defaultdict(list)
    for path in adjacent_paths:
        start, end = path[0], path[-1]
        path_groups[(start, end)].append(path)

    shortest_paths = []
    for start_end, group_paths in path_groups.items():
        shortest = min(group_paths, key=len)
        shortest_paths.append(shortest)

    for path in shortest_paths:
        for paths in path_to_goal:
            if is_adjacent(path[0], paths[-1]):
                precomputed_paths.append(paths+path)

    for path in precomputed_paths:
        final_landmarks.add(path[-1])

    return final_landmarks, precomputed_paths

def manhattan_distance(cell1, cell2):
    x1, y1 = map(int, re.findall(r'(\d+)', cell1))
    x2, y2 = map(int, re.findall(r'(\d+)', cell2))
    return abs(x1 - x2) + abs(y1 - y2)

def LAMA(current_chunk, current_cell, current_path):
    complete_path = []
    goal_cell = "cellx0y0"
    landmarks, precomputed_paths = Identify_Landmarks(graph)
    cost = 0
    
    nearest_landmark = min(landmarks, key=lambda lm: manhattan_distance(current_cell, lm))

    nearest_path_to_landmark = None
    for path in precomputed_paths:
        if current_path[-1] == nearest_landmark and path[-1] == current_cell:
            nearest_path_to_landmark = current_path
            break
    
    path_from_landmark_to_goal = None
    for path in precomputed_paths:
        if path[-1] == nearest_landmark:
            path_from_landmark_to_goal = path
            break
    
    # If both parts of the path are identified, combine them for a complete path from current to goal
    if nearest_path_to_landmark and path_from_landmark_to_goal:
        print(nearest_path_to_landmark + path_from_landmark_to_goal[::-1])
        cost = len(complete_path)
        exit()
    else:
        for path in precomputed_paths:
            if nearest_landmark == path[-1]:
                path_length = len(path)
        cost = manhattan_distance(current_cell, nearest_landmark) + path_length

    return cost

def backtrack(graph):
    max_chunk_coord = max(graph.keys(), key=lambda x: (x[0], x[1]))
    start = max_chunk_coord

    start_paths = []
    all_paths = []
    open_set = PriorityQueue()

    for entry, exits in graph[start].items():
        for exit, details in exits.items():
            current_path_info = []
            direction = details['direction']
            path = details['path']
            reversed_path = path[::-1]
            direction = details['direction']
            cost = LAMA(start, path[-1], path)  # Initial cost estimate
            open_set.put((cost, (start, reversed_path,  direction)))
            start_paths.append((start, reversed_path, direction))

    while not open_set.empty():
        cost, (chunk, path, direction) = open_set.get()  
        current_step = path[-1]  
        current_chunk = chunk  

        # Check if the current step is the goal
        if current_chunk == (0, 0):
            final_cell, final_chunk = adjacent_cell_and_chunk(path[::-1], direction, chunk)

            if final_cell:
                adjacent = adjacent_path(final_cell, current_chunk, graph)
                if adjacent:
                    for adj_path, (new_adj_cell, new_adj_chunk), adj_direction in adjacent:
                        path = path + adj_path[::-1]

            all_paths.append(path)
            continue
        
        adj_cell, chunknew = adjacent_cell_and_chunk(path[::-1], direction, chunk)
        if chunk == (max_chunk_coord):
            chunk = chunknew
        adj_chunk = chunk
        if adj_cell is None or adj_chunk is None:
            continue

        adjacent = adjacent_path(adj_cell, adj_chunk, graph)

        for adj_path, adj_info, adj_direction in adjacent:
            adj_paths = [adj_path for adj_path, _, _ in adjacent]
            adj_infos = [adj_info for _, adj_info, _ in adjacent]
            adj_direction = [adj_direction for _, _, adj_direction in adjacent]
            new_adj_cell, current_chunk = adj_infos[0]
            for adj_path, (new_adj_cell, new_adj_chunk), adj_direction in adjacent:
                new_path = path + adj_path[::-1]
                new_cost = LAMA(adj_chunk, adj_cell, new_path)  # Re-estimate cost
                # Put the new path back into the queue with its updated cost
                open_set.put((new_cost, (new_adj_chunk, new_path, adj_direction)))

    return all_paths

def shortest_path(paths):
    target="cellx0y0"
    target_paths = [path for path in paths if path[-1] == target]
    
    if target_paths:
        shortest_path =  min(target_paths, key=len)
        cost = len(shortest_path)  # The "cost" is the number of steps in the path
        return shortest_path, cost
    else:
        return None


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
first_chunk_coord = (0, 0)
if first_chunk_coord in chunk_map:
    chunk_map[first_chunk_coord].add_entry_point((0, 0), 'manual')
# Finding the coordinates of the last (bottom-right) chunk
max_chunk_coord = max(chunk_map.keys())
max_chunk_x, max_chunk_y = max_chunk_coord
max_inside_chunk_x = (max_chunk_x * 3) + (3 - 1)
max_inside_chunk_y = (max_chunk_y * 3) + (3 - 1)
chunk_map[max_chunk_coord].add_exit_point((max_inside_chunk_x, max_inside_chunk_y), 'manual')
# Calculate paths for each chunk
for chunk_coord, chunk in chunk_map.items():
    calculate_paths_for_chunk(chunk, chunk_coord, right_of, left_of, is_above, is_underneath)
graph = create_chunk_graph(chunk_map)
path_chunks = backtrack(graph)
shortest_path_and_cost = shortest_path(path_chunks)
print("Shortest path and its cost:", shortest_path_and_cost)