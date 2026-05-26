import pygame
from game_variables.game_variables import GameVariables as gv
from objects.sprites import Bilder

class Player:
    def __init__(self, screen: pygame.Surface, player_x_pos, player_y_pos):
        self.player_x_pos = player_x_pos
        self.player_y_pos = player_y_pos
        self.screen = screen
        self.sprite = Bilder("assats/Bilder/Player_moving.png",2,pygame.Rect(0,0, 100,100), 2)
        self.sprite.load_spritesheet()

    def move(self, max_x_pos: int, min_x_pos: int,
             max_y_pos: int, min_y_pos: int) -> None:
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.player_x_pos -= gv.player_v
            if self.player_x_pos <= min_x_pos:
                self.player_x_pos = min_x_pos

        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.player_x_pos += gv.player_v
            if self.player_x_pos + gv.player_size >= max_x_pos:
                self.player_x_pos = max_x_pos - gv.player_size

        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            self.player_y_pos -= gv.player_v
            if self.player_y_pos <= min_y_pos:
                self.player_y_pos = min_y_pos

        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            self.player_y_pos += gv.player_v
            if self.player_y_pos + gv.player_size >= max_y_pos:
                self.player_y_pos = max_y_pos - gv.player_size

    def update_and_draw(self, max_x_pos: int, min_x_pos: int,
             max_y_pos: int, min_y_pos: int):
        self.move(max_x_pos, min_x_pos, max_y_pos, min_y_pos)


        self.sprite.draw(screen=self.screen,xpos=self.player_x_pos,ypos=self.player_y_pos,frame_counter=0)
