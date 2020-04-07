
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
        
        self.controller = None         
        self.game_running = False
        self.menu_view_running = False
        self.end_game_running = False    
        
    def on_init(self):
        self.controller = gameController.Controller()
       
    def run(self):
        print('MENU')
        self.on_init()
        controller = self.controller
        menu_view = controller.get_view.menu_view
        menu_view.blit_background()
        menu_view.draw_menu_view()
        
        self.menu_view_running = True
        
        while self.menu_view_running:
            controller.keyboard_menu_control(self)
            menu_view.update_display()
            
        self.start_game()
           
                    
    def start_game(self):
        """Run the main event loop."""
        controller = self.controller
        controller.on_init()                
        model = controller.get_model        
        game_view = controller.get_view.get_game_view  

        character = model.get_character
        
        self.game_running = True
           
        while self.game_running and character.alive:
            game_view.blit_background()                      
                        
            controller.keyboard_game_control(self)
            game_view.blit_sprites(model.get_all_sprites())
            game_view.draw_inventory(model.get_character.bag_of_items)
            game_view.update_display()       

        self.game_running = False    
        self.end_game(character, game_view, controller)    
    
           
    def end_game(self, character, game_view, controller):
        
        self.end_game_running = True
        
        while self.end_game_running:
            
            game_view.update_display()
            controller.keyboard_end_game_control(self)
          
            if character.alive:
                game_view.game_win()    
            else:
                game_view.game_over()        
         
        self.reset_game()    
        self.run()

    def reset_game(self):
        print('RESET')
        del self.controller        
            
 
if __name__ == '__main__':
    
    game = App()
    game.run()
