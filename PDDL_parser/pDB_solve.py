from PDB_create import target_path, adjacent_cell_and_chunk, adjacent_path, graph
import pickle
from collections import deque

def bfs(graph, all_paths):

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


filename = 'PDDL_parser/paths.pkl'

with open(filename, 'rb') as file:
    all_paths = pickle.load(file)

solution = bfs(graph, all_paths)

print(solution)