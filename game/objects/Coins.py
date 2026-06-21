import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder


class Coins:
    def __init__(self, screen):
        self.screen = screen

    def show_coins(self):
        coins_text = gv.FONT_MIDDLE.render(f"Coins: {gv.coins}",True,
                                           "yellow")
        coins_rect = coins_text.get_rect(center=(gv.SCREEN_WIDTH - 100, 50))
        self.screen.blit(coins_text, coins_rect)
    def change_coins(self, change):
        gv.coins += change
