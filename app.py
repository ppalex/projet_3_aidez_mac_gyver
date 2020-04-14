import Configuration.config as config
import Controller.gameController as gameController

config.load('./configuration/initialisation.yml')


class App:

    def __init__(self):
        """Initialize pygame and the application."""

        self.controller = None

        self.game_running = False
        self.menu_view_running = False
        self.end_game_running = False

    def on_init(self):
        """This method create and assign an object Controller to the
        app.
        """
        self.controller = gameController.Controller()

    def run(self):
        """This method run the game and display the menu.
        """
        print('MENU')
        self.on_init()
        controller = self.controller
        controller.display_menu()

        self.menu_view_running = True

        while self.menu_view_running:
            controller.keyboard_menu_control(self)

        self.start_game()

    def start_game(self):
        """This method start a new game.
        """
        controller = self.controller
        controller.on_init()

        self.game_running = True

        while self.game_running and controller.is_character_alive():
            controller.keyboard_game_control(self)

        self.game_running = False

        self.end_game()

    def end_game(self):
        """This method display the end screen.

        Arguments:
            character {Object} -- Character of the game.
            game_view {Object} -- Game view.
            controller {Object} -- Controller.
        """
        controller = self.controller
        self.end_game_running = True

        while self.end_game_running:
            controller.keyboard_end_game_control(self)
            controller.display_end_game()

        self.reset_game()
        self.run()

    def reset_game(self):
        print('RESET')
        del self.controller
