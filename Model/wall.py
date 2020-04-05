
import os

from Model.board import Cell

import Configuration.config as config

config.load('./configuration/initialisation.yml')

class Wall(Cell):     
    def __init__(self, x, y):
        super().__init__(x, y)
        
    
