import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder


class Uhr:
    def __init__(self, screen):
        self.uhr = [0, 0]
        self.screen = screen
        self.last_update = pygame.time.get_ticks()

    def change_time(self):
        aktuelle_zeit = pygame.time.get_ticks()

        if aktuelle_zeit - self.last_update >= 1000:
            self.last_update = aktuelle_zeit

            if self.uhr[1] >= 59:
                self.uhr[0] += 1
                self.uhr[1] = 0
            else:
                self.uhr[1] += 1

    def show_uhr(self) -> None:
        uhr_text = gv.FONT_MIDDLE.render(f"Time: {self.uhr[0]} : {self.uhr[1]}",
                                        True, "white")
        coins_text_rect = uhr_text.get_rect(center=(gv.SCREEN_WIDTH - 300 , 50))
        self.screen.blit(uhr_text, coins_text_rect)

    def uhr_update(self):
        self.show_uhr()
        self.change_time()
