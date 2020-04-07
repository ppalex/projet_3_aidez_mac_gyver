import os

import pygame as pg

import Configuration.config as config
from Model.board import Cell

config.load('./configuration/initialisation.yml')


class Guardian(Cell):
    def __init__(self, x, y):
        """Constructor of the class Guardian.

        Arguments:
            Cell {Object} -- Parent of the class. It contains the width
            and height in pixel.
            x {int} -- Abscissa of the object.
            y {int} -- Ordinate of the object.
            """
        super().__init__(x, y)
        self.image = pg.image.load(os.path.join(
            config.value['src']['images'], 'guardian.png'))
        self.sleep = False

    def is_sleeping(self):
        """This function determine if the guardian is sleeping or not.

        Returns:
            [Boolean] -- True if the guardian is sleeping. False if not.
        """
        return self.sleep
