from collections import deque
from pddl_parser import *
from aStar import *
import re
import pickle

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

def localise_cell(cell, offset_x, offset_y):
        parts = cell.split('x')[1].split('y')
        cell_x, cell_y = int(parts[0]), int(parts[1])
        
        local_x = cell_x - offset_x
        local_y = cell_y - offset_y
        
        return f"cellx{local_x}y{local_y}"

def localise(chunk, entry, exit, right_adj, left_adj, above_adj, under_adj):
    
    x, y = chunk
    offset_x = x * 3
    offset_y = y * 3

    entry_x, entry_y = entry
    exit_x, exit_y = exit
    
    entry_x = entry_x - offset_x
    entry_y = entry_y - offset_y
    local_entry = (entry_x, entry_y)

    exit_x = exit_x - offset_x
    exit_y = exit_y - offset_y
    local_exit = (exit_x, exit_y)

    localized_right_adjacency = {localise_cell(key, offset_x, offset_y): localise_cell(value, offset_x, offset_y) for key, value in right_adj.items()}
    localized_left_adjacency = {localise_cell(key, offset_x, offset_y): localise_cell(value, offset_x, offset_y) for key, value in left_adj.items()}
    localized_above_adjacency = {localise_cell(key, offset_x, offset_y): localise_cell(value, offset_x, offset_y) for key, value in above_adj.items()}
    localized_under_adjacency = {localise_cell(key, offset_x, offset_y): localise_cell(value, offset_x, offset_y) for key, value in under_adj.items()}
    
    return localized_right_adjacency, localized_left_adjacency, localized_above_adjacency, localized_under_adjacency, local_exit, local_entry

def process_adjacency(direction, cells):
        sorted_cells = sorted(cells.items(), key=lambda item: item[0])
        return [f"{direction}-{key}-{value}" for key, value in sorted_cells]

def generate_lookup_key(right_of, left_of, is_above, is_underneath, entry_points, exit_points):
    adjacencies_str_parts = []
    adjacencies_str_parts.extend(process_adjacency("right_of", right_of))
    adjacencies_str_parts.extend(process_adjacency("left_of", left_of))
    adjacencies_str_parts.extend(process_adjacency("above", is_above))
    adjacencies_str_parts.extend(process_adjacency("underneath", is_underneath))

    adjacencies_str = ",".join(adjacencies_str_parts)

    entry_points_str = ",".join(sorted([f"entry-{pt[0]}-{pt[1]}" for pt in entry_points]))
    exit_points_str = ",".join(sorted([f"exit-{pt[0]}-{pt[1]}" for pt in exit_points]))

    lookup_key = f"{adjacencies_str}|{entry_points_str}|{exit_points_str}"
    return lookup_key

def globalise_path(chunk_coord, path):
    globalised_path = []
    x, y = chunk_coord
    offset_x = x * 3
    offset_y = y * 3
    for cell in path:
        parts = cell.split('x')[1].split('y')
        cell_x, cell_y = int(parts[0]), int(parts[1])
        
        global_x = cell_x + offset_x
        global_y = cell_y + offset_y
        
        globalised_cell = f"cellx{global_x}y{global_y}"
        globalised_path.append(globalised_cell)
    
    return globalised_path

def localise_path(chunk_coord, path):
    localised_path = []
    x, y = chunk_coord
    offset_x = x * 3
    offset_y = y * 3
    for cell in path:
        parts = cell.split('x')[1].split('y')
        cell_x, cell_y = int(parts[0]), int(parts[1])
        
        global_x = cell_x - offset_x
        global_y = cell_y - offset_y
        
        localised_cell = f"cellx{global_x}y{global_y}"
        localised_path.append(localised_cell)
    
    return localised_path


def calculate_paths_for_chunk(chunk, chunk_coord, right_of, left_of, is_above, is_underneath):
    filtered_adjacencies = filter_adjacencies_for_chunk(chunk, right_of, left_of, is_above, is_underneath)
    entry_points = chunk.get_entry_points()
    exit_points = chunk.get_exit_points()
    path_db = {}

    new_x, new_y = chunk_coord
    top_left_x_new = new_x * 3
    top_left_y_new = new_y * 3
    for entry in entry_points:
        for exit in exit_points:
            lright_adj, lleft_adj, labove_adj, lunder_adj, lexit, lentry = localise(chunk_coord, entry, exit, filtered_adjacencies["right_of"], filtered_adjacencies["left_of"], filtered_adjacencies["is_above"], filtered_adjacencies["is_underneath"])
            lookup_key = generate_lookup_key(lright_adj, lleft_adj, labove_adj, lunder_adj, [lentry], [lexit])
            existing_path = path_db.get(lookup_key, None)
            if existing_path is not None:
                new_path = globalise_path(chunk_coord, existing_path)
                cost = len(new_path)
                chunk.add_path(entry, exit, new_path, cost)
            else:
                start_cell = f"cellx{entry[0]}y{entry[1]}"
                goal_cell = f"cellx{exit[0]}y{exit[1]}"
                path = aStar(filtered_adjacencies["right_of"], filtered_adjacencies["left_of"], filtered_adjacencies["is_above"], filtered_adjacencies["is_underneath"], start_cell, goal_cell, 3, (top_left_x_new, top_left_y_new))
                if path is not None:
                    new_path = localise_path(chunk_coord, path)
                    path_db[lookup_key] = new_path
                    cost = len(new_path)
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
    chunk_data = graph.get(adj_chunk, {})
    
    for entry, exits in chunk_data.items():
        for exit, details in exits.items():
            if exit == cell:
                adj_info = adjacent_cell_and_chunk(details['path'], details['direction'], adj_chunk)
                paths.append((details['path'], adj_info, details['direction']))
    
    return paths


def backtrack(graph):
    max_chunk_coord = max(graph.keys(), key=lambda x: (x[0], x[1]))
    x, y = max_chunk_coord
    x = x // 2 + 1 
    y = y // 2 + 1
    start = (x, y)

    start_paths = []
    queue = deque(start_paths)
    all_paths = []
    complete_paths = []

    for entry, exits in graph[start].items():
        for exit, details in exits.items():
            current_path_info = []
            direction = details['direction']
            path = details['path']
            reversed_path = path[::-1]
            direction = details['direction']
            start_paths.append((start, reversed_path, direction))
            queue = deque(start_paths)

    while queue:
        chunk, path, direction = queue.popleft()
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
        if chunk == (start):
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
                queue.append((new_adj_chunk, new_path, adj_direction))
    for path in all_paths:
        if path:
            complete_paths.append(path)
    
    return complete_paths

def target_path(paths, target):
    # Search for complete paths that contain the target anywhere within them
    target_paths = [path for path in paths if target in path and path[-1] == "cellx0y0"]
    
    if target_paths:
        # extract the part of the path from the target onwards
        shortest_path_containing_target = min(target_paths, key=len)
        target_index = shortest_path_containing_target.index(target)
        
        # return the part of the path from the target onwards
        path_from_target = shortest_path_containing_target[target_index:]
        return path_from_target
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


filename = 'paths.pkl'

# Open the file and dump the paths into it
all_paths = backtrack(graph)
with open(filename, 'wb') as file:
    pickle.dump(all_paths, file)
