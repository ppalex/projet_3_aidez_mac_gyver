
from Model.board import Cell
import os

import pygame as pg

import Configuration.config as config

config.load('./configuration/initialisation.yml')


class Gate(Cell):
    def __init__(self, x, y):
        """Constructor of the class Gate.

        Arguments:
            Cell {Object} -- Parent of the class. It contains the width
            and height in pixel.
            x {int} -- Abscissa of the object.
            y {int} -- Ordinate of the object.
            """
        super().__init__(x, y)
        self.image = pg.image.load(os.path.join(
            config.value['src']['images'], 'gate.png'))
        self.open = False
