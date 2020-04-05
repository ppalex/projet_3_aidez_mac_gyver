import Model.maze as maze
import Model.character as character

class Model:
    def __init__(self):
        self.character = character.Character()
        self.maze = maze.Maze()
        
    @property
    def get_maze(self):
        return self.maze
    
    @property
    def get_character(self):
        return self.character