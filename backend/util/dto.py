from pydantic import BaseModel

class Request(BaseModel):
    type_maze: int
    type_algorithm: int
    maze_structure: list