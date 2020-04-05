import os

from Model.board import Cell


import Configuration.config as config

config.load('./configuration/initialisation.yml')

class Guardian(Cell):     
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sleep = False    
    
    def is_sleeping(self):
        return self.sleep