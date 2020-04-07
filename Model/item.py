
import os
import pygame as pg
from Model.board import Cell

import Configuration.config as config

config.load('./configuration/initialisation.yml')


class Item(Cell):
    def __init__(self, x, y):
        """Constructor of the class Item.

        Arguments:
            Cell {Object} -- Parent of the class. It contains the width
            and height in pixel.
            x {int} -- Abscissa of the object.
            y {int} -- Ordinate of the object.
            """
        super().__init__(x, y)


class Needle(Item):
    def __init__(self, x, y):
        """Constructor of the class Needle.

        Arguments:
            Item {Object} -- Parent of the class.
            x {int} -- Abscissa of the object.
            y {int} -- Ordinate of the object.
            """
        super().__init__(x, y)
        self.image = pg.image.load(os.path.join(
            config.value['src']['images'], 'needle.png'))


class Tube(Item):
    def __init__(self, x, y):
        """Constructor of the class Tube.

        Arguments:
            Item {Object} -- Parent of the class.
            x {int} -- Abscissa of the object.
            y {int} -- Ordinate of the object.
            """
        super().__init__(x, y)
        self.image = pg.image.load(os.path.join(
            config.value['src']['images'], 'tube.png'))


class Ether(Item):
    def __init__(self, x, y):
        """Constructor of the class Ether.

        Arguments:
            Item {Object} -- Parent of the class.
            x {int} -- Abscissa of the object.
            y {int} -- Ordinate of the object.
            """
        super().__init__(x, y)
        self.image = pg.image.load(os.path.join(
            config.value['src']['images'], 'ether.png'))
