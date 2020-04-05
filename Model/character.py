
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
        current_x, current_y = self.get_current_pos()
        width, _ = maze.get_map_size()
        
        if current_x < (width - 1):
            self.set_current_pos(current_x+self.change_x, current_y)
            maze.update_character_position(self.x, self.y, current_x, current_y)            
        self.change_x -= self.SPEED
        
        
    # MOVE LEFT  
    def move_left(self, maze):
        self.change_x -= self.SPEED
        current_x, current_y = self.get_current_pos()
        width, _ = maze.get_map_size()
        
        if current_x > (0):
            self.set_current_pos(current_x+self.change_x, current_y)
            maze.update_character_position(self.x, self.y, current_x, current_y)            
        self.change_x += self.SPEED
    
    # MOVE DOWN  
    def move_down(self, maze):
        
        self.change_y += self.SPEED
        current_x, current_y = self.get_current_pos()
        _, heigth = maze.get_map_size()
        
        if current_y < (heigth - 1):
            self.set_current_pos(current_x, current_y+self.change_y)
            maze.update_character_position(self.x, self.y, current_x, current_y)            
        self.change_y -= self.SPEED
    
    # MOVE UP   
    def move_up(self, maze):
        
        self.change_y -= self.SPEED
        current_x, current_y = self.get_current_pos()
        _, heigth = maze.get_map_size()
        
        if current_y > 0:
            self.set_current_pos(current_x, current_y+self.change_y)
            maze.update_character_position(self.x, self.y, current_x, current_y)            
        self.change_y += self.SPEED       
          
    
    def check_collision(self):
        pass
    
    def get_current_pos(self):
        return (self.x, self.y)
    
    def set_current_pos(self, x, y):
        self.x = x
        self.y = y
        
        