import Model.character as character
import Model.maze as maze


class Model:
    def __init__(self):
        """Constructor of the Model.
        The model contains the maze object and the character object.
        """
        self.character = character.Character()
        self.maze = maze.Maze()

    @property
    def get_maze(self):
        """This function get the Maze object of the Model.

        Returns:
            [Object] -- [Maze object]
        """
        return self.maze

    @property
    def get_character(self):
        """This function get the Character object of the Model.

        Returns:
            [Object] -- [Character object]
        """
        return self.character

    def get_all_sprites(self):
        """This function return all sprites of the Maze object and the
        character object.

        Returns:
            [List] -- [The list contains walls sprites, gates sprites,
            items sprites, guardians sprites and the character sprite]
        """
        all_sprites = self.maze.walls + self.maze.gates + \
            self.maze.items + self.maze.guardians
        all_sprites.append(self.character)

        return all_sprites
