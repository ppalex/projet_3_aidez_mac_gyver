
import os

import pygame as pg
from Model.board import Cell

import Configuration.config as config

config.load('./configuration/initialisation.yml')

class Wall(Cell):     
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pg.image.load(os.path.join(config.value['src']['images'],'wall.png'))
        
    
