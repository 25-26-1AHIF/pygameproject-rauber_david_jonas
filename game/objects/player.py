import pygame
from game_variables.game_variables import GameVariables as gv
from objects.sprites import Bilder

class Player:
    def __init__(self, screen: pygame.Surface, player_x_pos, player_y_pos):
        self.player_x_pos = player_x_pos
        self.player_y_pos = player_y_pos
        self.screen = screen

        self.moving_sprite_basic = Bilder("../assats/Bilder/Player_moving.png",
                                          2,pygame.Rect(0,0, 100,100),
                                          30)
        self.moving_sprite_blue = Bilder("../assats/Bilder/Player_moving_blue.png",
                                         2, pygame.Rect(0, 0, 100, 100),
                                         30)
        self.moving_sprite_red = Bilder("../assats/Bilder/Player_moving_red.png",
                                         2, pygame.Rect(0, 0, 100, 100),
                                         30)
        self.moving_sprite_green = Bilder("../assats/Bilder/Player_moving_green.png",
                                         2, pygame.Rect(0, 0, 100, 100),
                                         30)
        self.moving_sprite_rainbow = Bilder("../assats/Bilder/Player_moving_rainbow.png",
                                         2, pygame.Rect(0, 0, 100, 100),
                                         30)

        self.aktueller_moving_skin = self.moving_sprite_basic
        if gv.aktueller_skin_moving == "basic":
            self.aktueller_moving_skin = self.moving_sprite_basic
        elif gv.aktueller_skin_moving == "blue":
            self.aktueller_moving_skin = self.moving_sprite_blue
        elif gv.aktueller_skin_moving == "red":
            self.aktueller_moving_skin = self.moving_sprite_red
        elif gv.aktueller_skin_moving == "green":
            self.aktueller_moving_skin = self.moving_sprite_green
        elif gv.aktueller_skin_moving == "rainbow":
            self.aktueller_moving_skin = self.moving_sprite_rainbow

        self.aktueller_moving_skin.load_spritesheet()
        for i in range(len(self.aktueller_moving_skin.images)): #KI Start
            self.aktueller_moving_skin.images[i] = pygame.transform.scale(
                self.aktueller_moving_skin.images[i],
                (100, 100)) # KI Ende

        self.standing_sprite_basic = Bilder("../assats/Bilder/Player standing.png",
                                            1,pygame.Rect(0, 0, 400, 400),
                                            1)
        self.standing_sprite_blue = Bilder("../assats/Bilder/Player_standing_blue.png",
                                           1, pygame.Rect(0, 0, 400, 400),
                                           1)
        self.standing_sprite_red = Bilder("../assats/Bilder/Player_standing_red.png",
                                           1, pygame.Rect(0, 0, 400, 400),
                                           1)
        self.standing_sprite_green = Bilder("../assats/Bilder/Player_standing_green.png",
                                           1, pygame.Rect(0, 0, 400, 400),
                                           1)
        self.standing_sprite_rainbow = Bilder("../assats/Bilder/Player_standing_rainbow.png",
                                           1, pygame.Rect(0, 0, 400, 400),
                                           1)

        self.aktueller_standing_skin = self.standing_sprite_basic
        if gv.aktueller_skin_standing == "basic":
            self.aktueller_standing_skin = self.standing_sprite_basic
        elif gv.aktueller_skin_standing == "red":
            self.aktueller_standing_skin = self.standing_sprite_red
        elif gv.aktueller_skin_standing == "green":
            self.aktueller_standing_skin = self.standing_sprite_green
        elif gv.aktueller_skin_standing == "blue":
            self.aktueller_standing_skin = self.standing_sprite_blue
        elif gv.aktueller_skin_standing == "rainbow":
            self.aktueller_standing_skin = self.standing_sprite_rainbow

        self.aktueller_standing_skin.load_spritesheet()
        self.aktueller_standing_skin.images[0] = pygame.transform.scale(
            self.aktueller_standing_skin.images[0],
            (200, 200)
        )
        self.frame_counter = 0
        self.speed = 0
        self.moving: bool = False

    def move(self, max_x_pos: int, min_x_pos: int,
             max_y_pos: int, min_y_pos: int) -> None:
        self.moving = False
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.moving = True
            self.player_x_pos -= gv.player_v
            if self.player_x_pos < min_x_pos:
                self.player_x_pos = min_x_pos

        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.moving = True
            self.player_x_pos += gv.player_v
            if self.player_x_pos > max_x_pos - gv.player_size:
                self.player_x_pos = max_x_pos - gv.player_size

        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            self.moving = True
            self.player_y_pos -= gv.player_v
            if self.player_y_pos <= min_y_pos:
                self.player_y_pos = min_y_pos

        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            self.moving = True
            self.player_y_pos += gv.player_v
            if self.player_y_pos + gv.player_size >= max_y_pos:
                self.player_y_pos = max_y_pos - gv.player_size

        gv.player_x = self.player_x_pos
        gv.player_y = self.player_y_pos

    def update_and_draw(self, max_x_pos: int, min_x_pos: int,
                        max_y_pos: int, min_y_pos: int):
        self.move(max_x_pos, min_x_pos, max_y_pos, min_y_pos)

        offset_x = 60
        offset_y = 65

        if self.moving == True:
            self.speed += 1 / self.aktueller_moving_skin.animation_speed
            if self.speed >= 1:
                self.frame_counter += 1

            self.aktueller_moving_skin.draw(
                screen=self.screen,
                xpos=self.player_x_pos + offset_x,
                ypos=self.player_y_pos + offset_y,
                frame_counter=self.frame_counter)
        else:
            self.aktueller_standing_skin.draw(
                screen=self.screen,
                xpos=self.player_x_pos,
                ypos=self.player_y_pos,
                frame_counter=0)
