from io import BytesIO
import matplotlib
import numpy as np
import networkx as nx
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from util.constants import A_STAR, BFS, DIJKSTRA
from maze.algorithms import a_star, bfs, dijkstra

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.maze_array = np.array([[0 if c == ' ' else 1 for c in row] for row in maze])
        self.G = nx.Graph()
        self.rows, self.columns = self.maze_array.shape
        self.coord_to_node = {}
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        self._build_graph()
    
    def _build_graph(self):
        for fila in range(self.rows):
            for columna in range(self.columns):
                if self.maze_array[fila, columna] == 1:
                    nodo = (fila, columna)
                    self.G.add_node(nodo)
                    self.coord_to_node[(fila, columna)] = nodo

        for fila in range(self.rows):
            for columna in range(self.columns):
                if self.maze_array[fila, columna] == 1:
                    actual = (fila, columna)
                    for dx, dy in self.directions:
                        nueva_fila = fila + dx
                        nueva_columna = columna + dy
                        if 0 <= nueva_fila < self.rows and 0 <= nueva_columna < self.columns and self.maze_array[nueva_fila, nueva_columna] == 1:
                            nodo_adyacente = (nueva_fila, nueva_columna)
                            peso = 1
                            self.G.add_edge(actual, nodo_adyacente, weight=peso)
    
    def solve_maze(self, start, end, algorithm):
        path = None
        time = None

        if algorithm == BFS:
            path, time = bfs(self.G, start, end)

        if algorithm == DIJKSTRA:
            grafo_ponderado = {nodo: {vecino: peso['weight'] for vecino, peso in self.G[nodo].items()} for nodo in self.G}
            path, time = dijkstra(grafo_ponderado, start, end)

        if algorithm == A_STAR:
            path, time = a_star(self.G, start, end)
        
        return path, time
    
    def plot_solution(self, path):
        width, height = self.rows, self.columns
        image_buffer = BytesIO()

        plt.figure(figsize=(8, 8))
        plt.imshow(self.maze_array, cmap='binary_r', origin='upper')

        for i in range(height):
            plt.plot([-0.5, width - 0.5], [i - 0.5, i - 0.5], 'w-', linewidth=2)

        for j in range(width):
            plt.plot([j - 0.5, j - 0.5], [-0.5, height - 0.5], 'w-', linewidth=2)

        for k in range(len(path) - 1):
            y1, x1 = path[k]
            y2, x2 = path[k + 1]
            plt.plot([x1, x2], [y1, y2], color='red', linewidth=3)

        plt.axis('equal')
        plt.axis('off')
        plt.savefig(image_buffer, format='png')
        plt.close()

        image_buffer.seek(0)
        return image_buffer.read()