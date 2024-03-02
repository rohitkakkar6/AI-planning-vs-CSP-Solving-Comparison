path_length = 4

#variables
steps = [f"step_{i}" for i in range(1, path_length + 1)]

grid_positions = [(x, y) for x in range(5) for y in range(5)]
domains = {step: grid_positions for step in steps}

print(steps)
print(domains)
