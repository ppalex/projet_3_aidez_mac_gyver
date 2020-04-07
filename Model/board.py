
class Cell():

    WIDTH_PX = 30
    HEIGHT_PX = 30

    def __init__(self, x, y):
        """Constructor of class Cell.

        Arguments:
            x {int} -- Abscissa coordinate of the cell.
            y {int} -- Ordinate coordinate of the cell.
        """

        self.width_px, self.height_px = self.WIDTH_PX, self.HEIGHT_PX
        self.x, self.y = x, y
