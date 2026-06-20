import pygame
from objects.sprites import Bilder
from game_variables.game_variables import GameVariables as gv



class Object:
    def __init__(self, path: str, wert: int, screen: pygame.Surface , ypos: int, xpos: int, rect: pygame.rect, imagecount: int, animationspeed: int, framecounter:int, geklaut:bool, auszahlung:bool):
        self.geklaut: bool = geklaut
        self.path = path
        self.rect = rect
        self.imagecount = imagecount
        self.animationspeed = animationspeed
        self.sprite = Bilder(self.path, self.imagecount, self.rect, self.animationspeed)
        self.sprite.load_spritesheet()
        self.screen = screen
        self.xpos = xpos
        self.ypos = ypos
        self.framecounter = framecounter
        self.wert: int = wert
        self.Auszahlung = auszahlung


    def update_and_draw(self):
        if self.geklaut == False:
            self.sprite.draw(self.screen, self.xpos, self.ypos, self.framecounter)

        elif self.geklaut == True and self.Auszahlung == False:
            gv.coins += self.wert
            self.Auszahlung = True



