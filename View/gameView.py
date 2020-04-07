import os

import pygame as pg

import Configuration.config as config
config.load('./configuration/initialisation.yml')

class View:

    def __init__(self):
        self.game_view = GameDisplay()
        
    @property
    def get_game_view(self):
        return self.game_view   

   
class MainDisplay():
    
    def __init__(self):
        self.width = 450
        self.height= 450
        pg.init()
        pg.time.Clock().tick(60)       
    
    @property
    def get_screen(self):
        return self.screen 
     
    def blit_background(self):
        self.screen.blit(self.background, (0,0))
        
    def blit_sprites(self, sprites):
        
        for sprite in sprites:
            self.screen.blit(sprite.image, 
                             (sprite.x * sprite.width_px, 
                              sprite.y * sprite.height_px))
        
    def update_display(self):
        pg.display.flip()
              
        
class GameDisplay(MainDisplay):
    def __init__(self):
        super().__init__()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.background = pg.image.load(os.path.join(config.value['src']['images'], 'background.jpg')).convert() 
 
class MenuDisplay(MainDisplay):    
    pass