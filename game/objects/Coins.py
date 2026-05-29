import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder


class Coins:
    def __init__(self, screen: pygame.Surface):
        self.anzahl_coins = 100
        self.screen = screen
    def show_coins(self) -> None:
        coins_text = gv.FONT_MIDDLE.render(f"Coins: {self.anzahl_coins}",
                                        True, "white")
        coins_text_rect = coins_text.get_rect(center=(gv.SCREEN_WIDTH - 100 , 50))
        self.screen.blit(coins_text, coins_text_rect)
    def change_coins(self, change: int):
        self.anzahl_coins = change + self.anzahl_coins
