
import os
import sys

import pygame as pg

import Configuration.config as config

import Controller.gameController as gameController

from Model import maze

config.load('./configuration/initialisation.yml')

class App:
        
    """Create a single-window app with multiple scenes."""
    
    def __init__(self, controller):
        """Initialize pygame and the application."""
        pg.init()
        pg.display.set_mode((400, 400))
        pg.time.Clock().tick(30)
        
        self.controller = controller         
        self.running = True        
    
    def run(self):
        """Run the main event loop."""
        controller = self.controller
        controller.on_init()
                
        model = controller.get_model         
       
           
        while self.running:
            controller.keyboard_game_control(self)    
       
       
        if model.get_character.alive:
            print('YOU WIN')

 
if __name__ == '__main__':
    
    c = gameController.Controller()
    game = App(c)
    game.run()
    
    