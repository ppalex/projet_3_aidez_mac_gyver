
import os


import Configuration.config as config

config.load('./configuration/initialisation.yml')

from Model.board import Cell

class Gate(Cell):     
    def __init__(self, x, y):
        super().__init__(x, y)
        self.open = False
        