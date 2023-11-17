import random

# Dimensiones del laberinto
# Impares -> Nos aseguramos que el laberinto solo tenga una entrada y una salida
width = 21
height = 21

# Creamos la matriz bidimensional que representará al laberinto
# Todo llenados de 1
maze = [[1 for _ in range(width)] for _ in range(height)]

# Función para verificar si una celda es válida
def is_valid(x, y):
    return x >= 0 and x < width and y >= 0 and y < height

# Función para verificar si una celda tiene vecinos no visitados
def has_unvisited_neighbors(x, y):
    neighbors = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
    for nx, ny in neighbors:
        if is_valid(nx, ny) and maze[ny][nx] == 1:
            return True
    return False

# Función para eliminar una pared entre dos celdas
def remove_wall(x1, y1, x2, y2):
    maze[y1][x1] = 0
    maze[y2][x2] = 0
    maze[(y1 + y2) // 2][(x1 + x2) // 2] = 0

# Función para generar el laberinto utilizando Recursive Backtracking
def generate_maze():
    stack = [(1, 1)]
    while stack:
        x, y = stack[-1]
        if has_unvisited_neighbors(x, y):
            neighbors = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
            random.shuffle(neighbors)
            for nx, ny in neighbors:
                if is_valid(nx, ny) and maze[ny][nx] == 1:
                    remove_wall(x, y, nx, ny)
                    stack.append((nx, ny))
                    break
        else:
            stack.pop()

# Función para obtener el laberinto como una lista de cadenas
def maze_to_list(maze):
    maze_list = []
    for row in maze:
        row_str = ''.join(['#' if cell == 1 else ' ' for cell in row])
        maze_list.append(row_str)
    return maze_list

# Llamamos a la función para generar el laberinto
generate_maze()

# Llamamos a la función para obtener el laberinto como una lista de cadenas
maze_list = maze_to_list(maze)

# Ahora puedes usar la variable maze_list que contiene el laberinto como una lista de cadenas
print(maze_list)
