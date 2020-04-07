import os
import pygame as pg

import Configuration.config as config

from Model.board import Cell

config.load('./configuration/initialisation.yml')

class Character(Cell):
    
    SPEED = 1
    INIT_X = 0
    INIT_Y = 0
    
    def __init__(self, x=INIT_X, y=INIT_Y):
        super().__init__(x, y)
        self.image = pg.image.load(os.path.join(config.value['src']['images'],'player.png'))                
        self.change_x = 0
        self.change_y = 0 
              
        self.alive = True            
        
        self.bag_of_items = {}
        self.all_items = False    
    
    
    def get_current_pos(self):
        return (self.x, self.y)
    
    def set_current_pos(self, x, y):
        self.x = x
        self.y = y
        
    # MOVE RIGHT    
    def move_right(self, current_x, current_y, maze):
        self.change_x += self.SPEED
        width, _ = maze.get_map_size()
        
        if current_x < (width - 1) and \
            (not self.check_collision(current_x+self.change_x, current_y, maze)):
                
            self.set_current_pos(current_x+self.change_x, current_y)           
                     
        self.change_x -= self.SPEED
        
        
    # MOVE LEFT  
    def move_left(self, current_x, current_y, maze):
        
        self.change_x -= self.SPEED        
        width, _ = maze.get_map_size()
        
        if current_x > (0) and \
            (not self.check_collision(current_x+self.change_x, current_y, maze)):                
            self.set_current_pos(current_x+self.change_x, current_y)                                
        self.change_x += self.SPEED
    
    # MOVE DOWN  
    def move_down(self, current_x, current_y, maze):
        
        self.change_y += self.SPEED        
        _, heigth = maze.get_map_size()
        
        if current_y < (heigth - 1) and \
            (not self.check_collision(current_x, current_y+self.change_y, maze)):                
            self.set_current_pos(current_x, current_y+self.change_y)
                      
        self.change_y -= self.SPEED
    
    # MOVE UP   
    def move_up(self, current_x, current_y, maze):
        
        self.change_y -= self.SPEED       
        _, heigth = maze.get_map_size()
        
        if current_y > 0 and \
            (not self.check_collision(current_x, current_y+self.change_y, maze)):
             
            self.set_current_pos(current_x, current_y+self.change_y)
           
        self.change_y += self.SPEED     
          
    
    def check_collision(self, next_x, next_y, maze):
        collision = False        
        if maze.map[next_y][next_x] == maze.symbol['wall']:
            print('COLLISION')
            collision = True        
        return collision
    

    def check_cell(self, current_x, current_y, maze):
        
        element_on_cell = maze.map[current_y][current_x]        
        
        if  element_on_cell != maze.symbol['path'] and \
            element_on_cell != maze.symbol['gate'] and \
            element_on_cell != maze.symbol['gardian'] and \
            element_on_cell != maze.symbol['character']:
                self.pick_up_item(element_on_cell, maze)
                
        elif element_on_cell == maze.symbol['gardian']:
            self.hit_guardian(maze)
        
        elif element_on_cell == maze.symbol['gate']:
            self.open_gate(maze)
    
    
    def pick_up_item(self, element_on_cell, maze):
        
        element_name = [k for k,v in maze.symbol.items() if v == element_on_cell][0]
            
        if element_name not in self.bag_of_items:
            self.bag_of_items[element_name] = 1
        else:
            self.bag_of_items[element_name] += 1
            
        maze.remove_item_from_list(self.x, self.y)
        print(self.all_items)
        print(self.bag_of_items)
                

    def check_items_picked_up(self, maze):        
        return len(self.bag_of_items) == maze.get_number_of_items()
 
    def open_gate(self, maze):
        print('GATE')                
        asleep_guardians = [guardian.is_sleeping() for guardian in maze.guardians]         
            
        if set(asleep_guardians).pop() == True:
            for gate in maze.gates:
                gate.open = True 
    
    
    def hit_guardian(self, maze):
        
        guardian = maze.guardians[0]
        
        if self.all_items:
            print('GUARDIAN SLEEP')
            guardian.sleep = True
        else:
            print('YOU DIE')
            self.alive = False