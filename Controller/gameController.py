import os
import sys

import pygame as pg

import Configuration.config as config
import Model.gameModel as gameModel
import View.gameView as gameView

config.load('./configuration/initialisation.yml')


class Controller:
    def __init__(self):
        """Constructor of the Controller.
        The model contains the Model object and the View object.
        """
        self.model = gameModel.Model()
        self.view = gameView.View()

    @property
    def get_model(self):
        """This methode get the model from the controller.

        Returns:
            [Object] -- The model object.
        """
        return self.model

    @property
    def get_view(self):
        """This methode get the view from the controller.

        Returns:
            [Object] --  The view object.
        """
        return self.view

    def on_init(self):
        """This method initialize the model with the structure from
        the csv file.
        """
        self.model.maze.initialize(os.path.join(
            config.value['src']['data'], 'maze.csv'))

    def keyboard_game_control(self, app):
        """This method provide the key board control when the user is
        playing into the game.

        Arguments:
            app {Object} -- Application.
        """

        character = self.get_model.get_character
        maze = self.get_model.get_maze
        game_view = self.get_view.get_game_view

        keys = pg.key.get_pressed()

        if keys[pg.K_TAB]:
            print('HELP')
            game_view.print_help()

        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

            elif keys[pg.K_RIGHT]:
                print('RIGHT')
                current_x, current_y = character.get_current_pos()
                character.move_right(current_x, current_y, maze)
                character.check_cell(character.x, character.y, maze)
                maze.update_character_position(
                    character.x, character.y, current_x, current_y)
                print(self.get_model.get_maze)

            elif keys[pg.K_LEFT]:
                print('LEFT')
                current_x, current_y = character.get_current_pos()
                character.move_left(current_x, current_y, maze)
                character.check_cell(character.x, character.y, maze)
                maze.update_character_position(
                    character.x, character.y, current_x, current_y)
                print(self.get_model.get_maze)

            elif keys[pg.K_DOWN]:
                print('DOWN')
                current_x, current_y = character.get_current_pos()
                character.move_down(current_x, current_y, maze)
                character.check_cell(character.x, character.y, maze)
                maze.update_character_position(
                    character.x, character.y, current_x, current_y)
                print(self.get_model.get_maze)

            elif keys[pg.K_UP]:
                print('UP')
                current_x, current_y = character.get_current_pos()
                character.move_up(current_x, current_y, maze)
                character.check_cell(character.x, character.y, maze)
                maze.update_character_position(
                    character.x, character.y, current_x, current_y)
                print(self.get_model.get_maze)

        if character.check_items_picked_up(maze):
            character.all_items = True

        if maze.gates_opened():
            app.game_running = False

    def keyboard_menu_control(self, app):
        """This method provide the key board control when the user is
        playing into menu.

        Arguments:
            app {Object} -- Application.
        """
        mx, my = pg.mouse.get_pos()
        click = False

        menu_view = self.get_view.menu_view

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if menu_view.menu_button.collidepoint((mx, my)):
            if click:
                app.menu_view_running = False

        if menu_view.quit_button.collidepoint((mx, my)):
            if click:
                pg.quit()
                sys.exit(0)

    def keyboard_end_game_control(self, app):
        """This method provide the key board control when the user end a game.

        Arguments:
            app {Object} -- Application.
        """
        mx, my = pg.mouse.get_pos()
        click = False

        game_view = self.get_view.game_view

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if game_view.back_menu_button.collidepoint((mx, my)):
            if click:
                app.end_game_running = False

    def display_menu(self):
        menu_view = self.get_view.menu_view
        menu_view.blit_background()
        menu_view.draw_menu_view()
        menu_view.update_display()

    def display_game(self):
        game_view = self.get_view.get_game_view
        model = self.get_model
        character = model.get_character

        game_view.blit_background()
        game_view.blit_sprites(model.get_all_sprites())
        game_view.draw_inventory(character.bag_of_items)
        game_view.update_display()

    def display_end_game(self):
        game_view = self.get_view.get_game_view
        character = self.model.get_character

        if character.alive:
            game_view.game_win()
        else:
            game_view.game_over()

        game_view.update_display()

    def is_character_alive(self):
        return self.get_model.get_character.alive
