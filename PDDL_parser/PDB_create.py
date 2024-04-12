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
    """
    Converts cell coordinates to chunk coordinates.

    Args:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        chunk_size (int, optional): The size of each chunk. Defaults to 3.

    Return:
        tuple: The chunk coordinates corresponding to the given cell coordinates.
    """
    return (x // chunk_size, y // chunk_size)

def initialize_chunks(max_x, max_y, chunk_size=3):
    """
    Initializes chunks for a grid map.

    Args:
        max_x (int): The maximum x-coordinate of the grid map.
        max_y (int): The maximum y-coordinate of the grid map.
        chunk_size (int, optional): The size of each chunk. Set to 3.

    Return:
        dict: A dictionary mapping chunk coordinates to Chunk objects.
    """
    chunk_map = {}
    for x in range(0, max_x + 1, chunk_size):
        for y in range(0, max_y + 1, chunk_size):
            chunk_coord = cell_to_chunk(x, y, chunk_size)
            chunk_map[chunk_coord] = Chunk()
    return chunk_map

def identify_and_store_entry_exit_points(chunk_map, right_of, left_of, is_above, is_underneath, chunk_size=3):
    """
    Identifies and stores entry and exit points for each chunk based on adjacency relationships from pddl file.

    Args:
        chunk_map (dict): A dictionary mapping chunk coordinates to Chunk objects.
        right_of (dict): A dictionary representing right-of relationships between cells.
        left_of (dict): A dictionary representing left-of relationships between cells.
        is_above (dict): A dictionary representing is-above relationships between cells.
        is_underneath (dict): A dictionary representing is-underneath relationships between cells.
        chunk_size (int, optional): The size of each chunk. Set to 3.
    """
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
    """
    Filters adjacent cell relationships to include only those within the given chunk.

    Args:
        chunk (Chunk): The Chunk object representing the chunk.
        right_of (dict): A dictionary representing right-of relationships between cells.
        left_of (dict): A dictionary representing left-of relationships between cells.
        is_above (dict): A dictionary representing is-above relationships between cells.
        is_underneath (dict): A dictionary representing is-underneath relationships between cells.

    Returns:
        dict: A dictionary containing filtered adjacent cell relationships within the chunk.
    """
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
    """
    Localises the cell coordinates by applying the given offsets.

    Args:
        cell (str): The coordinate of the cell in the format 'cellx{x}y{y}'.
        offset_x (int): The offset to be applied to the x-coordinate.
        offset_y (int): The offset to be applied to the y-coordinate.

    Returns:
        str: The localized coordinate of the cell in the format 'cellx{x}y{y}'.
    """
    parts = cell.split('x')[1].split('y')
    cell_x, cell_y = int(parts[0]), int(parts[1])
        
    local_x = cell_x - offset_x
    local_y = cell_y - offset_y
        
    return f"cellx{local_x}y{local_y}"

def localise(chunk, entry, exit, right_adj, left_adj, above_adj, under_adj):
    """
    Localises chunk coordinates, entry and exit points, and adjacency dictionaries based on chunk offsets.

    Args:
        chunk (tuple): The coordinates of the chunk.
        entry (tuple): The coordinates of the entry point.
        exit (tuple): The coordinates of the exit point.
        right_adj (dict): A dictionary representing right-of relationships between cells.
        left_adj (dict): A dictionary representing left-of relationships between cells.
        above_adj (dict): A dictionary representing is-above relationships between cells.
        under_adj (dict): A dictionary representing is-underneath relationships between cells.

    Returns:
        tuple: A tuple containing localised adjacency dictionaries, localised entry and exit points.
    """
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
    """
    Processes adjacency relationships for a given direction.

    Args:
        direction (str): The direction of adjacency relationships (e.g., 'right', 'left', 'above', 'under').
        cells (dict): A dictionary representing adjacency relationships between cells.

    Return:
        list: A list containing formatted adjacency relationships for the given direction.
    """
    sorted_cells = sorted(cells.items(), key=lambda item: item[0])
    return [f"{direction}-{key}-{value}" for key, value in sorted_cells]

def generate_lookup_key(right_of, left_of, is_above, is_underneath, entry_points, exit_points):
    """
    Generates a lookup key based on adjacency relationships, entry points, and exit points.

    Args:
        right_of (dict): A dictionary representing right-of relationships between cells.
        left_of (dict): A dictionary representing left-of relationships between cells.
        is_above (dict): A dictionary representing is-above relationships between cells.
        is_underneath (dict): A dictionary representing is-underneath relationships between cells.
        entry_points (list): A list of entry points.
        exit_points (list): A list of exit points.

    Returns:
        str: A lookup key string.
    """
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
    """
    Globalises a path by applying the chunk's offsets.

    Args:
        chunk_coord (tuple): The coordinates of the chunk.
        path (list): The path to be globalized.

    Returns:
        list: A list containing globalised cells representing the path.
    """
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
    """
    Localises a path by applying the chunk's offsets.

    Args:
        chunk_coord (tuple): The coordinates of the chunk.
        path (list): The path to be localised.

    Returns:
        list: A list containing localised cells representing the path.
    """
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
    """
    Calculates paths for the given chunk based on its adjacency relationships and entry/exit points.

    Args:
        chunk (Chunk): The chunk for which paths are to be calculated.
        chunk_coord (tuple): The coordinates of the chunk.
        right_of (dict): A dictionary representing right-of relationships between cells.
        left_of (dict): A dictionary representing left-of relationships between cells.
        is_above (dict): A dictionary representing is-above relationships between cells.
        is_underneath (dict): A dictionary representing is-underneath relationships between cells.
    """
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
    """
    Creates a graph representing the connections between chunks and their paths.

    Args:
        chunk_map (dict): A dictionary mapping chunk coordinates to Chunk objects.

    Returns:
        dict: A dictionary representing the chunk graph, with chunk coordinates as keys, and dictionaries representing
        paths from entry to exit points as values.
    """
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
    """
    Determines the adjacent cell and chunk coordinates based on the current path, direction, and chunk coordinates.

    Args:
        path (list): A list representing the current path, where the first element is the current cell.
        direction (str): A string representing the direction of adjacency ('up', 'down', 'left', 'right').
        chunk (tuple): A tuple representing the coordinates of the current chunk.

    Returns:
        tuple: A tuple containing the adjacent cell and the coordinates of the chunk it belongs to.
               The adjacent cell is represented as a string in the format "cellx{cell_x}y{cell_y}".
               The chunk coordinates are represented as a tuple (chunk_x, chunk_y).
               Returns (None, None) if the direction is invalid.
    """
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
    """
    Determines the adjacent cell and its corresponding chunk coordinates based on the given path, direction, and chunk.

    Args:
        path (list): The path from entry to exit points.
        direction (str): The direction of movement ('up', 'down', 'left', 'right').
        chunk (tuple): The coordinates of the chunk.

    Return:
        tuple: A tuple containing the adjacent cell and its corresponding chunk coordinates.
    """
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
    """
    Performs a breadth first search to find all possible paths from the bottom right chunk to the top left chunk in the given graph.

    Args:
        graph (dict): The graph representing the chunks and their connections.

    Return:
        list: A list of complete paths from the starting chunk to the goal chunk.
    """
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
max_chunk_coord = max(chunk_map.keys())
max_chunk_x, max_chunk_y = max_chunk_coord
max_inside_chunk_x = (max_chunk_x * 3) + (3 - 1)
max_inside_chunk_y = (max_chunk_y * 3) + (3 - 1)
chunk_map[max_chunk_coord].add_exit_point((max_inside_chunk_x, max_inside_chunk_y), 'manual')
# Calculate paths for each chunk
for chunk_coord, chunk in chunk_map.items():
    calculate_paths_for_chunk(chunk, chunk_coord, right_of, left_of, is_above, is_underneath)
graph = create_chunk_graph(chunk_map)


filename = 'PDDL_parser/paths.pkl'

# Open the file and dump the paths into it
all_paths = backtrack(graph)
with open(filename, 'wb') as file:
    pickle.dump(all_paths, file)
