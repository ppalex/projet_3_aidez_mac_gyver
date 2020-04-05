
import Configuration.config as config
from Model.board import Cell

config.load('./configuration/initialisation.yml')

class Character(Cell):
    
    SPEED = 1
    INIT_X = 0
    INIT_Y = 0
    
    def __init__(self, x=INIT_X, y=INIT_Y):
        super().__init__(x, y)                 
        self.change_x = 0
        self.change_y = 0       
        self.alive = True     
        
        self.bag_of_items = {}
        self.all_items = False    
    
    
    # MOVE RIGHT
    
    def move_right(self, maze):
        self.change_x += self.SPEED
        x, y = self.get_current_pos()
        width, _ = maze.get_maze_size()
        
        if x < width:
            self.set_current_pos(x+self.change_x, y)
            maze.update_maze_position(self.x, self.y)
            
        
    # MOVE LEFT  
    def move_left(self):
        pass
    
    # MOVE DOWN  
    def move_down(self):
        pass
    
    # MOVE UP   
    def move_up(self):
        pass    
    
    def check_collision(self):
        pass
    
    def get_current_pos(self):
        return (self.x, self.y)
    
    def set_current_pos(self, x, y):
        self.x = x
        self.y = y
        
        