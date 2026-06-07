import pygame
from game_variables.game_variables import GameVariables as gv

class Uhr:
    def __init__(self, screen):
        self.screen = screen
        self.last_update = pygame.time.get_ticks()

    def change_time(self):
        aktuelle_zeit = pygame.time.get_ticks()

        if aktuelle_zeit - self.last_update >= 1000:
            self.last_update = aktuelle_zeit

            if gv.sekunden >= 59:
                gv.stunden += 1
                gv.sekunden = 0
            else:
                gv.sekunden += 1

    def show_uhr(self):
        coins_text = gv.FONT_MIDDLE.render(
            f"Time: {gv.stunden}:{gv.sekunden}",
            True,
            "white"
        )

        coins_rect = coins_text.get_rect(center=(gv.SCREEN_WIDTH - 300, 50))
        self.screen.blit(coins_text, coins_rect)

    def uhr_update(self):
        self.show_uhr()
        self.change_time()