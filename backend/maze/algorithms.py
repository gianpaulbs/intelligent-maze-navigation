from collections import deque
from heapq import heappop, heappush
from time import time
from scipy.spatial.distance import euclidean

def reconstruct_path(came_from, start, end):
    path = [end]
    current = end
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def bfs(graph, start, end):
    start_time = time()
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == end:
            total = time() - start_time
            return path, total

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                queue.append((neighbor, path + [neighbor]))

    return None, 0

def dijkstra(grafo, inicio, fin):
    start_time = time()
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]
    camino = {}

    while cola:
        distancia_actual, nodo_actual = heappop(cola)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heappush(cola, (distancia, vecino))
                camino[vecino] = nodo_actual

    camino_corto = reconstruct_path(camino, inicio, fin)
    total = time() - start_time
    return camino_corto, total

def a_star(graph, start, end):
    def heuristic(node, goal):
        return euclidean(node, goal)
    
    start_time = time()
    open_set = set([start])
    came_from, g_score, f_score = {}, {node: float('inf') for node in graph}, {node: float('inf') for node in graph}
    g_score[start], f_score[start] = 0, heuristic(start, end)

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])

        if current == end:
            total = time() - start_time
            path = reconstruct_path(came_from, start, end)
            return path, total

        open_set.remove(current)

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]['weight']

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                open_set.add(neighbor)

    return None, 0
