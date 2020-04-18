import os

import pygame as pg

import Configuration.config as config

config.load('./configuration/initialisation.yml')


class View:

    def __init__(self):
        """Constructor of the View.
        The view contains two views:
                    - The game display (when the player plays)
                    - The menu display
        """
        self.game_view = GameDisplay()
        self.menu_view = MenuDisplay()

    @property
    def get_game_view(self):
        """This method get the game view object.

        Returns:
            [Object] -- Display the game.
        """
        return self.game_view


class MainDisplay():

    WHITE = (255, 255, 255)

    def __init__(self):
        """Constructor of the class MainDisplay.
        """
        self.width = 450
        self.height = 450

        pg.init()
        pg.display.set_caption('Mac Gyver game')
        pg.time.Clock().tick(60)

    @property
    def get_screen(self):
        """This method get the screen of the main display.

        Returns:
            [Object] -- Screen from pg.display to control
                        the display window and screen
        """
        return self.screen

    @property
    def get_width(self):
        """This method get the width of the screen.

        Returns:
            [Integer] -- Width of the screen.
        """
        return self.width

    @property
    def get_height(self):
        """This method get the height of the screen.

        Returns:
            [Integer] -- Height of the screen.
        """
        return self.height

    def blit_background(self):
        """ This method draw the image background.
        It uses the blit function from the module pygame.
        """
        self.screen.blit(self.background, (0, 0))

    def blit_sprites(self, sprites):
        """This method draw all the sprites on the screen.
        It uses the blit function from the module pygame.

        Arguments:
            sprites {List} -- Contains all the sprites from the
                                game.
        """
        for sprite in sprites:
            self.screen.blit(sprite.image,
                             (sprite.x * sprite.width_px,
                              sprite.y * sprite.height_px))

    def update_display(self):
        """This method will update the entire display.
        It uses the flip function from the module pygame.
        """
        pg.display.flip()

    def draw_text(self, text, font, color, surface, x, y):
        """This function allows to draw text on the screen.

        Arguments:
            text {String} -- Text to draw on the screen.
            font {Font} -- pygame object for Font representations.
            color {Color} --Pygame object for Color representations.
            surface {Surface} -- Pygame object for representing images.
            x {Integer} -- Position.
            y {Integer} -- Position.
        """
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


class GameDisplay(MainDisplay):
    def __init__(self):
        super().__init__()
        """Constructor of the class GameDisplay.
        """
        self.screen = pg.display.set_mode((self.width, self.height))
        self.background = pg.image.load(os.path.join(
            config.value['src']['images'], 'background.jpg')).convert()
        self.back_menu_button = pg.Rect(150, 150, 200, 50)

    def draw_inventory(self, items):
        """This method shows the inventory information on the screen.

        Arguments:
            items {Dict} -- Dictionnary that contains information
                            about the inventory.
        """
        if not items:
            text = "Inventory: empty"
        else:
            text = '/'.join(['%s: %s' % (key.capitalize(), value)
                             for (key, value) in items.items()])
        font = pg.font.SysFont(None, 25)
        self.draw_text(text, font, self.WHITE, self.screen, 100, 5)

    def print_help(self):
        """This method shows the help information on the screen.
        """
        help = "USE KEYS ARROWS TO MOVE."
        font = pg.font.SysFont(None, 25)
        self.draw_text(help, font, self.WHITE, self.screen, 100, 150)

    def game_over(self):
        """This method shows the game over end on the screen.
        """
        text = "GAME OVER!"
        text_button = 'MENU'
        font = pg.font.SysFont(None, 50)
        self.draw_text(text, font, self.WHITE, self.screen, 150, 100)
        pg.draw.rect(self.screen, (0, 0, 0), self.back_menu_button)
        self.draw_text(text_button, font, self.WHITE, self.screen, 185, 155)

    def game_win(self):
        """This method shows the game win end on the screen.
        """
        text = "YOU WIN!"
        text_button = 'MENU'
        font = pg.font.SysFont(None, 50)
        self.draw_text(text, font, self.WHITE, self.screen, 150, 100)
        pg.draw.rect(self.screen, (0, 0, 0), self.back_menu_button)
        self.draw_text(text_button, font, self.WHITE, self.screen, 185, 155)


class MenuDisplay(MainDisplay):
    def __init__(self, width=450, height=450):
        """Constructor class of the MenuDisplay.

        Arguments:
            MainDisplay {Object} -- Parent class.

        Keyword Arguments:
            width {int} -- Width size (default: {450})
            height {int} -- Height size (default: {450})
        """
        self.screen = pg.display.set_mode((width, height))
        self.background = pg.image.load(os.path.join(
            config.value['src']['images'], 'background_menu.png')).convert()
        self.font = pg.font.SysFont(None, 40)
        self.menu_button = pg.Rect(50, 100, 200, 50)
        self.quit_button = pg.Rect(50, 200, 200, 50)

    def draw_menu_view(self):
        """This method shows the menu view on the screen.
        """
        self.draw_text('MENU', self.font, self.WHITE, self.screen, 20, 20)
        self.draw_button()
        self.draw_text('NEW GAME', self.font, self.WHITE, self.screen, 80, 110)
        self.draw_text('QUIT', self.font, self.WHITE, self.screen, 80, 210)
        # self.draw_text('Use TAB for help', self.font,
        #                self.WHITE, self.screen, 0, 420)

    def draw_button(self):
        """This method draw two buttons for the menu.
        """
        pg.draw.rect(self.screen, (255, 69, 0), self.menu_button)
        pg.draw.rect(self.screen, (255, 69, 0), self.quit_button)
