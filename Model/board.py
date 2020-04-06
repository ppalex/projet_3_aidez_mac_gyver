
class Cell():
    
    WIDTH_PX = 30
    HEIGHT_PX = 30
    
    def __init__(self, x, y):
            
        self.width_px, self.height_px = self.WIDTH_PX, self.HEIGHT_PX
        self.x, self.y = x, y