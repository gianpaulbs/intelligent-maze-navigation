import random

def generate_maze(width, height):
    maze = [[0] * width for _ in range(height)]

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height

    def generate(x, y):
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and maze[ny][nx] == 0:
                maze[y + dy // 2][x + dx // 2] = 1
                maze[ny][nx] = 1
                generate(nx, ny)

    generate(1, 1)
    maze[0][1] = maze[height - 1][width - 2] = 1

    num_additional_paths = (width * height) // 10
    for _ in range(num_additional_paths):
        x, y = random.randrange(1, width - 1, 2), random.randrange(1, height - 1, 2)
        maze[y][x] = 1

    return maze

def display_maze(maze):
    for row in maze:
        print(''.join(['#' if cell == 0 else ' ' for cell in row]))

def maze_to_list(maze):
    maze_list = []
    for row in maze:
        row_str = ''.join(['#' if cell == 1 else ' ' for cell in row])
        maze_list.append(row_str)
    return maze_list

width, height = 21, 21

maze = generate_maze(width, height)
maze_list = maze_to_list(maze)

print(maze_list)
