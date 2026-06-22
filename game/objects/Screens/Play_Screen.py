import pygame
import random
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Coins import Coins
from objects.Uhr import Uhr


def play_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Play Screen")
    gv.current_screen = "play"
    player_x_pos = gv.player_x
    player_y_pos = gv.player_y
    player = Player(
        screen=screen,
        player_x_pos=player_x_pos,
        player_y_pos=player_y_pos
    )
    frame_counter = 0

    straße = Bilder("../assats/Bilder/Häuser_reihe_fertig.png", 1, pygame.Rect(0, 0, 8192, 1024), 80)
    straße.load_spritesheet()
    orginal_straße = straße.images

    bg_width = gv.SCREEN_WIDTH * 8
    bg_height = gv.SCREEN_HIGHT
    groesse_straße = (bg_width, bg_height)
    straße.images = [pygame.transform.smoothscale(img, groesse_straße) for img in orginal_straße]
    x_pos_hintergrund = gv.background_x
    coins = Coins(screen)
    uhr = Uhr(screen)

    # ### TÜREN ALS EINZELNE VARIABLEN BERECHNEN ###
    # Berechnung basiert auf den exakten Pixel-Koordinaten des Originalbildes (8192 x 1024)
    x_scale = bg_width / 8192.0
    y_scale = bg_height / 1024.0
    tuer_1_rect = pygame.Rect(1535 * x_scale, 555 * y_scale, 85 * x_scale, 160 * y_scale)
    tuer_2_rect = pygame.Rect(2515 * x_scale, 535 * y_scale, 85 * x_scale, 160 * y_scale)
    tuer_4_rect = pygame.Rect(5580 * x_scale, 565 * y_scale, 105 * x_scale, 185 * y_scale)
    tuer_3_rect = pygame.Rect(3490 * x_scale, 560 * y_scale, 95 * x_scale, 150 * y_scale)
    tuer_5_rect = pygame.Rect(6635 * x_scale, 555 * y_scale, 85 * x_scale, 160 * y_scale)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gv.paused_from = GameScreens.PLAY
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                event_x, event_y = event.pos
                x_Hintergrund = event_x - x_pos_hintergrund
                y_Hintergrund = event_y


                if tuer_1_rect.collidepoint(x_Hintergrund, y_Hintergrund):
                    return random.choice([GameScreens.RIDDLE1, GameScreens.RIDDLE2,
                                         GameScreens.RIDDLE3, GameScreens.RIDDLE4,
                                         GameScreens.RIDDLE5])

                elif tuer_2_rect.collidepoint(x_Hintergrund, y_Hintergrund):
                    gv.haus_2 = True
                    return random.choice([GameScreens.RIDDLE1, GameScreens.RIDDLE2,
                                         GameScreens.RIDDLE3, GameScreens.RIDDLE4,
                                         GameScreens.RIDDLE5])

                elif tuer_3_rect.collidepoint(x_Hintergrund, y_Hintergrund):
                    gv.wohnwagen = True
                    return random.choice([GameScreens.RIDDLE1, GameScreens.RIDDLE2,
                                         GameScreens.RIDDLE3, GameScreens.RIDDLE4,
                                         GameScreens.RIDDLE5])

                elif tuer_4_rect.collidepoint(x_Hintergrund, y_Hintergrund):
                    gv.haus_3 = True
                    return random.choice([GameScreens.RIDDLE1, GameScreens.RIDDLE2,
                                         GameScreens.RIDDLE3, GameScreens.RIDDLE4,
                                         GameScreens.RIDDLE5])

                elif tuer_5_rect.collidepoint(x_Hintergrund, y_Hintergrund):
                    return random.choice([GameScreens.RIDDLE1, GameScreens.RIDDLE2,
                                         GameScreens.RIDDLE3, GameScreens.RIDDLE4,
                                         GameScreens.RIDDLE5])

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if x_pos_hintergrund < -10:
                x_pos_hintergrund += 10

        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if x_pos_hintergrund > -5000:
                x_pos_hintergrund -= 10
        gv.background_x = x_pos_hintergrund

        screen.fill("black")
        straße.draw(screen, x_pos_hintergrund, 0, frame_counter)
        player.update_and_draw(
            max_x_pos=gv.SCREEN_WIDTH - 200,
            min_x_pos=200,
            max_y_pos=gv.SCREEN_HIGHT - gv.player_size - 100,
            min_y_pos=gv.SCREEN_HIGHT / 2 + 100)
        coins.show_coins()
        uhr.uhr_update()

        pygame.display.flip()
        clock.tick(gv.FPS)