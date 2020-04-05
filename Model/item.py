
import os
import pygame as pg

from Model.board import Cell

import Configuration.config as config

config.load('./configuration/initialisation.yml')

class Item(Cell):     
    def __init__(self, x, y):
        super().__init__(x, y)
            

class Needle(Item):
    def __init__(self, x, y):
        super().__init__(x, y)
                
        
class Tube(Item):
    def __init__(self, x, y):
        super().__init__(x, y)
        

class Ether(Item):
    def __init__(self, x, y):
        super().__init__(x, y)
        