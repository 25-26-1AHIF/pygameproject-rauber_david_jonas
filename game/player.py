import pygame
from game_variables.game_variables import GameVariables as gv

class Player:
    def __init__(self, screen: pygame.Surface, player_x_pos, player_y_pos):
        self.player_x_pos = player_x_pos
        self.player_y_pos = player_y_pos
        self.screen = screen

    def move(self) -> None:
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            self.player_x_pos -= gv.player_v
            if self.player_x_pos <= 0:
                self.player_x_pos = 0

        if pressed_keys[pygame.K_d]:
            self.player_x_pos += gv.player_v
            if self.player_x_pos + gv.player_size >= gv.SCREEN_WIDTH:
                self.player_x_pos = gv.SCREEN_WIDTH - gv.player_size

        if pressed_keys[pygame.K_w]:
            self.player_y_pos -= gv.player_v
            if self.player_y_pos <= 0:
                self.player_y_pos = 0

        if pressed_keys[pygame.K_s]:
            self.player_y_pos += gv.player_v
            if self.player_y_pos + gv.player_size >= gv.SCREEN_HIGHT:
                self.player_y_pos = gv.SCREEN_HIGHT - gv.player_size

    def update_and_draw(self):
        self.move()

        pygame.draw.rect(
            surface=self.screen,
            rect=(
                self.player_x_pos,
                self.player_y_pos,
                gv.player_size,
                gv.player_size
            ),
            color="red",
            width=0
            )
