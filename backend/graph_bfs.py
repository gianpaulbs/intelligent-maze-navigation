import mazes
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from constants import LITTLE_MAZE, MEDIUM_MAZE, BIG_MAZE

# Load maze data
maze_list = mazes.maze_list
maze_array = np.array([[0 if cell == " " else 1 for cell in row] for row in maze_list])

# Create a graph
G = nx.Graph()

rows, cols = maze_array.shape
coord_to_node = {}

for row in range(rows):
    for col in range(cols):
        if maze_array[row, col] == 1:
            node = (row, col)
            G.add_node(node)
            coord_to_node[(row, col)] = node

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for row in range(rows):
    for col in range(cols):
        if maze_array[row, col] == 1:
            current = (row, col)

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and maze_array[new_row, new_col] == 1
                ):
                    adjacent_node = (new_row, new_col)
                    weight = 1
                    G.add_edge(current, adjacent_node, weight=weight)

start = list(G.nodes())[0]
end = list(G.nodes())[-1]


# BFS to find the shortest path
def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                queue.append((neighbor, path + [neighbor]))

    return None


shortest_path = bfs_shortest_path(G, start, end)

# Plotting
width, height = cols, rows

plt.figure(figsize=(8, 8))
plt.imshow(maze_array, cmap="binary_r", origin="upper")

# Plot grid lines
for i in range(height):
    plt.plot([-0.5, width - 0.5], [i - 0.5, i - 0.5], "w-", linewidth=1)

for j in range(width):
    plt.plot([j - 0.5, j - 0.5], [-0.5, height - 0.5], "w-", linewidth=1)

# Plot the shortest path in a thinner red line
for k in range(len(shortest_path) - 1):
    y1, x1 = shortest_path[k]
    y2, x2 = shortest_path[k + 1]
    plt.plot([x1, x2], [y1, y2], color="red", linewidth=2, label="Shortest Path")

# Mark the start and end points
plt.scatter(start[1], start[0], color="green", s=50, label="Start")
plt.scatter(end[1], end[0], color="blue", s=50, label="End")

plt.axis("equal")
plt.axis("off")
plt.show()
