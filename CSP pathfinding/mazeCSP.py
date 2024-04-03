from pyamaze import maze, agent

grid_size = 5
m = maze(grid_size, grid_size)
m.CreateMaze(loopPercent=100)
# Set the agent's start position (e.g., top-left corner)
a = agent(m, 1, 1)

# Set the maze's goal (end point) explicitly
m.goal = (grid_size, grid_size)  # Bottom-right corner

start_pos = (0, 0)
goal_pos = (4,4)

grid_positions = [(x, y) for x in range(grid_size) for y in range(grid_size)]

