from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from base64 import b64encode
from util.dto import Request
from maze.graph import MazeSolver
import maze.generator as generator

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-maze")
def generate_maze(request: Request):
    type_maze = request.type_maze
    type_algorithm = request.type_algorithm
    maze_list = request.maze_structure

    if len(maze_list) == 0:
        maze = generator.generate_maze(type_maze)
        maze_list = generator.maze_to_list(maze)
    
    maze_solver = MazeSolver(maze_list)
    
    inicio = list(maze_solver.G.nodes())[0]
    fin = list(maze_solver.G.nodes())[-1]
    
    camino_corto, time = maze_solver.solve_maze(inicio, fin, type_algorithm)
    image_data = maze_solver.plot_solution(camino_corto)
    encoded_image = b64encode(image_data).decode('utf-8')

    return {
        "image": encoded_image, 
        "time": time, 
        "maze_structure": maze_list
    }