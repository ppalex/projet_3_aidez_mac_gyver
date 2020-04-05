class Player(Cell):
    
    SPEED = 30
    INIT_X = 0
    INIT_Y = 0
    
    def __init__(self):      
        
        
        self.pos_x = self.INIT_X
        self.pos_y = self.INIT_Y
              
        self.change_x = 0
        self.change_y = 0      
        
        self.alive = True       
        
        self.bag_of_items = {}
        self.all_items = False    
    
    
    # MOVE RIGHT
    def move_right(self)):
        pass
        
    # MOVE LEFT  
    def _move_left(self):
        pass
    
    # MOVE DOWN  
    def _move_down(self):
        pass
    
    # MOVE UP   
    def move_up(self):
        pass    
    
    def check_collision(self):
        pass
    
    def get_current_pos(self):
        return (self.pos_x, self.pos_y)
        
        