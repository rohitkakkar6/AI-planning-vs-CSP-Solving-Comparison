from PDB_create import adjacent_cell_and_chunk, adjacent_path, graph
import pickle
from collections import deque

def bfs(graph, all_paths):
    """
    Performs a breadth-first search (BFS) on a graph to find a path from the start to the goal cell.

    Parameters:
    - "graph" (dict): A dictionary representing the graph where keys are chunk coordinates and values are dictionaries representing paths from entry to exit cells within chunks.
    - "all_paths" (list): A list of all paths found in the pattern database.

    Returns:
    - list or str: If a path from the start to the goal cell is found, returns the complete path. If no path is found, returns "Path not found".
    """
    max_chunk_coord = max(graph.keys(), key=lambda x: (x[0], x[1]))
    start = max_chunk_coord

    start_paths = []
    queue = deque(start_paths)
    all_paths = []

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

        target = target_path(all_paths, current_step)
        if target is not None:
            return path + target

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

    return "Path not found"

def target_path(paths, target):
    """
    Searches for complete paths that contain the target cell anywhere within them.

    Parameters:
        paths (list): A list of paths.
        target (str): The target cell to search for in the paths.

    Returns:
        list or None: If paths containing the target and reaching the goal cell are found, returns the part of the path from the target cell onwards. Otherwise, returns None.
    """
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

filename = 'PDDL_parser/paths.pkl'

with open(filename, 'rb') as file:
    all_paths = pickle.load(file)

solution = bfs(graph, all_paths)

print(solution)