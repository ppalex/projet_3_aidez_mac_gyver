
import os
import sys

import pygame as pg

import Configuration.config as config
import Controller.gameController as gameController
from Model import maze

config.load('./configuration/initialisation.yml')

class App:
        
    """Create a single-window app with multiple scenes."""
    
    def __init__(self):
        """Initialize pygame and the application."""       
        
        self.controller = gameController.Controller()         
        self.running = True 
        
    def run(self):
        print('MENU')
        controller = self.controller
        menu_view = controller.get_view.menu_view
        menu_view.blit_background()
                    
                    
    def start_game(self):
        """Run the main event loop."""
        controller = self.controller
        controller.on_init()                
        model = controller.get_model        
        game_view = controller.get_view.get_game_view    
       
           
        while self.running:
            game_view.blit_background()
            game_view.blit_sprites(model.get_all_sprites())
            controller.keyboard_game_control(self)
            game_view.draw_inventory(model.get_character.bag_of_items)
            game_view.update_display()
       

        if model.get_character.alive:
            print('YOU WIN')
 
if __name__ == '__main__':
    
    game = App()
    game.run()
