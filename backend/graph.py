import mazes
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

# Obtener el laberinto y crear la matriz y el grafo
laberinto = mazes.maze_list
laberinto_array = np.array([[0 if c == ' ' else 1 for c in row] for row in laberinto])

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
                    peso = 1  # Asignar peso aleatorio entre 1 y 20
                    G.add_edge(actual, nodo_adyacente, weight=peso)

# Algoritmo de Dijkstra para encontrar el camino más corto desde el primer nodo al último nodo
inicio = list(G.nodes())[0]  # Primer nodo creado
fin = list(G.nodes())[-1]  # Último nodo creado

camino_corto = nx.dijkstra_path(G, inicio, fin, weight='weight')

# Dibujar el grafo
pos = dict((nodo, nodo) for nodo in G.nodes())
labels = {edge: G.get_edge_data(*edge)['weight'] for edge in G.edges()}
nx.draw(G, pos, with_labels=False, font_weight='bold', node_size=5)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Resaltar el camino más corto encontrado por Dijkstra
edges_camino_corto = list(zip(camino_corto, camino_corto[1:]))
nx.draw_networkx_edges(G, pos, edgelist=edges_camino_corto, edge_color='red', width=3)

# Resaltar el nodo de inicio y el nodo final
nx.draw_networkx_nodes(G, pos, nodelist=[inicio], node_color='green', node_size=100) # PUNTO DE INICIO ES COLOR VERDE
nx.draw_networkx_nodes(G, pos, nodelist=[fin], node_color='blue', node_size=100) # PUNTO DE FIN ES COLOR AZUL

plt.show()
