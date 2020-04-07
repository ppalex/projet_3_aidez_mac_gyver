import os
import sys

import pygame as pg

import Configuration.config as config
import Model.gameModel as gameModel
import View.gameView as gameView

config.load('./configuration/initialisation.yml')


class Controller:
    def __init__(self):
        self.model = gameModel.Model()   
        self.view = gameView.View()    
         
    @property
    def get_model(self):
        return self.model
    
    @property
    def get_view(self):
        return self.view   
    
    def on_init(self):
        self.model.maze.initialize(os.path.join(config.value['src']['data'], 'maze.csv'))
    
    def keyboard_game_control(self, app):        
        
        character =  self.get_model.get_character
        maze = self.get_model.get_maze
        
        for event in pg.event.get():
            keys = pg.key.get_pressed()  
            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)                                     
            
            elif keys[pg.K_RIGHT]:
                print('RIGHT')
                
                current_x, current_y = character.get_current_pos()
                character.move_right(current_x, current_y, maze)                
                character.check_cell(character.x, character.y, maze)                             
                maze.update_character_position(character.x, character.y, current_x, current_y)            
                
                print(self.get_model.get_maze)
                
            elif keys[pg.K_LEFT]:
                print('LEFT')
                current_x, current_y = character.get_current_pos()
                character.move_left(current_x, current_y, maze)
                character.check_cell(character.x, character.y, maze)                             
                maze.update_character_position(character.x, character.y, current_x, current_y)
                print(self.get_model.get_maze)
                
            elif keys[pg.K_DOWN]:
                print('DOWN')
                current_x, current_y = character.get_current_pos()
                character.move_down(current_x, current_y, maze)
                character.check_cell(character.x, character.y, maze)
                maze.update_character_position(character.x, character.y, current_x, current_y)
                
                print(self.get_model.get_maze)
                
            elif keys[pg.K_UP]:
                print('UP')
                current_x, current_y = character.get_current_pos()
                character.move_up(current_x, current_y, maze)
                character.check_cell(character.x, character.y, maze)                             
                maze.update_character_position(character.x, character.y, current_x, current_y)
                print(self.get_model.get_maze)                
              
        if character.check_items_picked_up(maze):
            character.all_items = True
            
        if maze.gates_opened():
            app.running = False                     


    