import mazes
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from constants import LITTLE_MAZE, MEDIUM_MAZE, BIG_MAZE

laberinto = mazes.maze_list
laberinto_array = np.array([[0 if c == ' ' else 1 for c in row] for row in laberinto])

print(laberinto_array)

G = nx.Graph()

filas, columnas = laberinto_array.shape
coord_to_node = {}

for fila in range(filas):
    for columna in range(columnas):
        if laberinto_array[fila, columna] == 1:
            nodo = (fila, columna)
            G.add_node(nodo)
            coord_to_node[(fila, columna)] = nodo

direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for fila in range(filas):
    for columna in range(columnas):
        if laberinto_array[fila, columna] == 1:
            actual = (fila, columna)
            for dx, dy in direcciones:
                nueva_fila = fila + dx
                nueva_columna = columna + dy
                if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and laberinto_array[nueva_fila, nueva_columna] == 1:
                    nodo_adyacente = (nueva_fila, nueva_columna)
                    peso = 1
                    G.add_edge(actual, nodo_adyacente, weight=peso)

inicio = list(G.nodes())[0]
fin = list(G.nodes())[-1]

camino_corto = nx.dijkstra_path(G, inicio, fin, weight='weight')

# Gráfica con grafos
# pos = dict((nodo, nodo) for nodo in G.nodes())
# labels = {edge: G.get_edge_data(*edge)['weight'] for edge in G.edges()}

# nx.draw(G, pos, with_labels=False, font_weight='bold', node_size=5)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# edges_camino_corto = list(zip(camino_corto, camino_corto[1:]))
# nx.draw_networkx_edges(G, pos, edgelist=edges_camino_corto, edge_color='red', width=3)

# nx.draw_networkx_nodes(G, pos, nodelist=[inicio], node_color='green', node_size=100) # PUNTO DE INICIO ES COLOR VERDE
# nx.draw_networkx_nodes(G, pos, nodelist=[fin], node_color='blue', node_size=100) # PUNTO DE FIN ES COLOR AZUL

# plt.show()

width = BIG_MAZE
height = BIG_MAZE

# Gráfica para mostrar en servidor
plt.figure(figsize=(8, 8))
plt.imshow(laberinto_array, cmap='binary_r', origin='upper')

for i in range(height):
    plt.plot([-0.5, width - 0.5], [i - 0.5, i - 0.5], 'w-', linewidth=2)

for j in range(width):
    plt.plot([j - 0.5, j - 0.5], [-0.5, height - 0.5], 'w-', linewidth=2)

for k in range(len(camino_corto) - 1):
    y1, x1 = camino_corto[k]
    y2, x2 = camino_corto[k + 1]
    plt.plot([x1, x2], [y1, y2], color='red', linewidth=3)

# plt.scatter([0], [0], color='green', s=100, marker='o')  # Punto de inicio
# plt.scatter([width - 1], [height - 1], color='blue', s=100, marker='o')  # Punto de fin

print(G)
plt.axis('equal')
plt.axis('off')
plt.show()
