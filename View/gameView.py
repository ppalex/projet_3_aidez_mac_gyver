import os

import pygame as pg

import Configuration.config as config

config.load('./configuration/initialisation.yml')

class View:    

    def __init__(self):
        self.game_view = GameDisplay()
        self.menu_view = MenuDisplay()
        
    @property
    def get_game_view(self):
        return self.game_view   

   
class MainDisplay():
    
    WHITE = (255,255,255)
    
    def __init__(self):
        self.width = 450
        self.height= 450
        
        pg.init()
        pg.display.set_caption('Mac Gyver game')
        pg.time.Clock().tick(10)       
    
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
    
        
    def draw_text(self, text, font, color, surface, x, y):
        
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
              
        
class GameDisplay(MainDisplay):
    def __init__(self):
        super().__init__()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.background = pg.image.load(os.path.join(config.value['src']['images'], 
                                                     'background.jpg')).convert()
        self.back_menu_button = pg.Rect(150, 150, 200, 50)
         

    def draw_inventory(self, items):        
        if not items:
            text = "Inventory: empty"        
        else:
            text = '/'.join(['%s: %s' % (key.capitalize(), value) for (key, value) in items.items()])             
        font = pg.font.SysFont(None, 25)
        self.draw_text(text, font, self.WHITE, self.screen, 100, 5)

    def game_over(self):
        text = "GAME OVER!"
        font = pg.font.SysFont(None, 50)
        self.draw_text(text, font, self.WHITE, self.screen, 100, 100)
        pg.draw.rect(self.screen, (255,69,0), self.back_menu_button)        
    
    def game_win(self):
        text = "YOU WIN!"
        font = pg.font.SysFont(None, 50)
        self.draw_text(text, font, self.WHITE, self.screen, 100, 100)
        pg.draw.rect(self.screen, (255,69,0), self.back_menu_button)


class MenuDisplay(MainDisplay):    
    def __init__(self, width=450, height=450):
        
        self.screen = pg.display.set_mode((width, height))
        self.background = pg.image.load(os.path.join(config.value['src']['images'], 'background_menu.png')).convert()
        self.font = pg.font.SysFont(None, 40)
        
        self.menu_button = pg.Rect(50, 100, 200, 50)
        self.quit_button = pg.Rect(50, 200, 200, 50)
            
        
    def draw_menu_view(self):      
        self.draw_text('MENU', self.font, self.WHITE, self.screen, 20, 20)
        self.draw_button()
        self.draw_text('NEW GAME', self.font, self.WHITE, self.screen, 80, 110)
        self.draw_text('QUIT', self.font, self.WHITE, self.screen, 80, 210)
        self.draw_text('Use TAB for help', self.font, self.WHITE, self.screen, 0, 420)        
        
    def draw_button(self):
        pg.draw.rect(self.screen, (255,69,0), self.menu_button)
        pg.draw.rect(self.screen, (255,69,0), self.quit_button)