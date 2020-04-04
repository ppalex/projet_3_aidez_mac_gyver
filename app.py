
import os
import sys

import pygame as pg

import Configuration.config as config

import Controller.gameController as gameController
import Model.gameModel as gameModel
import View.gameView as gameView

from Model import maze

config.load('./configuration/initialisation.yml')


class App:
        
    """Create a single-window app with multiple scenes."""
    
    def __init__(self, controller):
        """Initialize pygame and the application."""
        pg.init()        
        self.running = True         
    
    def run(self):
        """Run the main event loop."""
               
        while self.running:
            pass                   
       
 
if __name__ == '__main__':    
  
    m = maze.Maze()
    m.initialize(os.path.join(config.value['src']['data'], 'maze.csv'))
    print(m)