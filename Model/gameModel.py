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
    
    def get_all_sprites(self):
        
        all_sprites = self.maze.walls + self.maze.gates + self.maze.items + self.maze.guardians
        all_sprites.append(self.character)
                        
        return all_sprites