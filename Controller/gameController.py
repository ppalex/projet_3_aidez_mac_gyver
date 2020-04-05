import sys
import pygame as pg

import Model.gameModel as gameModel


class Controller:
    def __init__(self):
        self.model = gameModel.Model()        
         
    @property
    def get_model(self):
        return self.model
    
    def keyboard_control(self, app):
        
        for event in pg.event.get():
            keys = pg.key.get_pressed()  
            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)                                     
            
            elif keys[pg.K_RIGHT]:
                print('RIGHT')
                self.get_model.get_character.move_right(self.get_model.get_maze)
                print(self.get_model.get_maze)
                
            elif keys[pg.K_LEFT]:
                print('LEFT')
                self.get_model.get_character.move_left(self.get_model.get_maze)
                print(self.get_model.get_maze)
                
            elif keys[pg.K_DOWN]:
                print('DOWN')
                self.get_model.get_character.move_down(self.get_model.get_maze)
                print(self.get_model.get_maze)
                
            elif keys[pg.K_UP]:
                print('UP')
                self.get_model.get_character.move_up(self.get_model.get_maze)
                print(self.get_model.get_maze)
    
            
           
                                   
                    
              