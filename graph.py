import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

laberinto = [
"#####################",
"# #       #       # #",
"# # ### # # ##### # #",
"# # #   #   #       #",
"# ### ##### ####### #",
"#   # # #   #   #   #",
"### # # # ### # ### #",
"#   # #   #   #   # #",
"# ### ##### ##### # #",
"#   #       #   # # #",
"### # ######### # ###",
"# # #     #     #   #",
"# # ##### # ### ### #",
"# #   # #   # # #   #",
"# ### # ##### # # # #",
"# #   #     #   # # #",
"# # ####### # ### ###",
"# #       #     #   #",
"# ####### ######### #",
"#                   #",
"#####################",
]

# Convierte el laberinto en una matriz de 1 y 0
laberinto_array = np.array([[1 if c == ' ' else 0 for c in row] for row in laberinto])
print(laberinto_array)

# Crea un grafo vacío
G = nx.Graph()

# Dimensiones del laberinto
filas, columnas = laberinto_array.shape

# Diccionario para mapear coordenadas (fila, columna) a nodos
coord_to_node = {}

# Escanea la matriz de 1 y 0 y crea nodos para celdas válidas
for fila in range(filas):
    for columna in range(columnas):
        if laberinto_array[fila, columna] == 1:
            nodo = (fila, columna)
            G.add_node(nodo)
            coord_to_node[(fila, columna)] = nodo

# Conecta nodos adyacentes (arriba, abajo, izquierda, derecha)
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
                    G.add_edge(actual, nodo_adyacente)

# Dibuja el grafo del laberinto
pos = dict((nodo, nodo) for nodo in G.nodes())
nx.draw(G, pos, with_labels=False, font_weight='bold', node_size=5)
print(G)

plt.show()
