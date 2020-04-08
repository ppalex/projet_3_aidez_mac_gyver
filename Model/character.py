import os
import pygame as pg

import Configuration.config as config

from Model.board import Cell

config.load('./configuration/initialisation.yml')


class Character(Cell):

    SPEED = 1
    INIT_X = 0
    INIT_Y = 0

    def __init__(self, x=INIT_X, y=INIT_Y):
        """Constructor of the class Character.

        Keyword Arguments:
            x {Integer} -- [Abscissa] (default: {INIT_X})
            y {Integer} -- [Ordinate] (default: {INIT_Y})
        """
        super().__init__(x, y)
        self.image = pg.image.load(os.path.join(
            config.value['src']['images'], 'player.png'))
        self.change_x = 0
        self.change_y = 0

        self.alive = True

        self.bag_of_items = {}
        self.all_items = False

    def get_current_pos(self):
        """This method get the current position of the character.

        Returns:
            [Tuple] -- It contains the coordonates of the character.
        """
        return (self.x, self.y)

    def set_current_pos(self, x, y):
        """This method modify the current position of the character.

        Arguments:
            x {Integer} -- New abscissa.
            y {Integer} -- New ordinate.
        """
        self.x = x
        self.y = y

    def move_right(self, current_x, current_y, maze):
        """This method move the character to the right in the maze.

        Arguments:
            current_x {Integer} -- Current abscissa.
            current_y {Integer} -- Current ordinate.
            maze {Object} -- Object from the class Maze.
        """
        self.change_x += self.SPEED
        width, _ = maze.get_map_size()

        if current_x < (width - 1) and \
                (not self.check_collision(
                    current_x+self.change_x, current_y, maze)):

            self.set_current_pos(current_x+self.change_x, current_y)

        self.change_x -= self.SPEED

    def move_left(self, current_x, current_y, maze):
        """This method move the character to the left in the maze.

        Arguments:
            current_x {Integer} -- Current abscissa.
            current_y {Integer} -- Current ordinate.
            maze {Object} -- Object from the class Maze.
        """
        self.change_x -= self.SPEED
        width, _ = maze.get_map_size()

        if current_x > (0) and \
                (not self.check_collision(
                    current_x+self.change_x, current_y, maze)):
            self.set_current_pos(current_x+self.change_x, current_y)

        self.change_x += self.SPEED

    def move_down(self, current_x, current_y, maze):
        """This method move the character to down in the maze.

        Arguments:
            current_x {Integer} -- Current abscissa.
            current_y {Integer} -- [Current ordinate.
            maze {Object} -- Object from the class Maze.
        """
        self.change_y += self.SPEED
        _, heigth = maze.get_map_size()

        if current_y < (heigth - 1) and \
                (not self.check_collision(
                    current_x, current_y+self.change_y, maze)):
            self.set_current_pos(current_x, current_y+self.change_y)

        self.change_y -= self.SPEED

    def move_up(self, current_x, current_y, maze):
        """This method move the character to up in the maze.

        Arguments:
            current_x {Integer} -- Current abscissa.
            current_y {Integer} -- Current ordinate.
            maze {Object} -- Object from the class Maze.
        """

        self.change_y -= self.SPEED
        _, heigth = maze.get_map_size()

        if current_y > 0 and \
                (not self.check_collision(
                    current_x, current_y+self.change_y, maze)):

            self.set_current_pos(current_x, current_y+self.change_y)

        self.change_y += self.SPEED

    def check_collision(self, next_x, next_y, maze):
        """this method allows the characted if he can move
        to the next cell.
        If there is a wall he can not move to the cell.

        Arguments:
            next_x {Integer} -- Next abscissa.
            next_y {Integer} -- Next ordinate.
            maze {Object} -- Maze object.

        Returns:
            [Boolean] -- True if there is a collision with a wall.
                            False if not.
        """
        collision = False

        if maze.map[next_y][next_x] == maze.symbol['wall']:
            print('COLLISION')
            collision = True

        return collision

    def check_cell(self, current_x, current_y, maze):
        """This method allows the character to check the cell and
        what kind of element is on the cell.

        Arguments:
            current_x {Integer} -- Current abscissa.
            current_y {Integer} -- Current ordinate.
            maze {Object} -- Object from the class Maze.
        """

        element_on_cell = maze.map[current_y][current_x]

        if element_on_cell != maze.symbol['path'] and \
                element_on_cell != maze.symbol['gate'] and \
                element_on_cell != maze.symbol['gardian'] and \
                element_on_cell != maze.symbol['character']:
            self.pick_up_item(element_on_cell, maze)

        elif element_on_cell == maze.symbol['gardian']:
            self.hit_guardian(maze)

        elif element_on_cell == maze.symbol['gate']:
            self.open_gate(maze)

    def pick_up_item(self, element_on_cell, maze):
        """This method allows the character to pick up
        an item.

        Arguments:
            element_on_cell {Object} -- Object from the  abstract class Item.
            maze {Object} -- Object from the class Maze.
        """
        element_name = [k for k, v in maze.symbol.items() if v ==
                        element_on_cell][0]

        if element_name not in self.bag_of_items:
            self.bag_of_items[element_name] = 1
        else:
            self.bag_of_items[element_name] += 1

        maze.remove_item_from_list(self.x, self.y)

    def check_items_picked_up(self, maze):
        """This method allows the character to check if he has
        taken all the items from the maze.

        Arguments:
             maze {Object} -- Object from the class Maze.

        Returns:
            [Boolean] -- True if all items are taken. False if not.
        """
        return len(self.bag_of_items) == maze.get_number_of_items()

    def open_gate(self, maze):
        """This method allows the character to open the gate.

        Arguments:
           maze {Object} -- Object from the class Maze.
        """
        print('GATE')
        asleep_guardians = [guardian.is_sleeping()
                            for guardian in maze.guardians]

        if set(asleep_guardians).pop():
            for gate in maze.gates:
                gate.open = True

    def hit_guardian(self, maze):
        """This method allows the character to fall asleep the guardian.

        Arguments:
            maze {Object} -- Object from the class Maze.
        """
        guardian = maze.guardians[0]

        if self.all_items:
            print('GUARDIAN SLEEP')
            guardian.sleep = True
        else:
            print('YOU DIE')
            self.alive = False
