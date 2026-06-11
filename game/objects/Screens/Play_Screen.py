import pygame
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

    straße = Bilder("../assats/Bilder/Häuser_reihe_fertig.png", 1, pygame.Rect(0, 0, 6144, 1024), 80)
    straße.load_spritesheet()
    orginal_straße = straße.images

    bg_width = gv.SCREEN_WIDTH * 6
    bg_height = gv.SCREEN_HIGHT
    groesse_straße = (bg_width, bg_height)
    straße.images = [pygame.transform.smoothscale(img, groesse_straße) for img in orginal_straße]
    x_pos_hintergrund = gv.background_x
    coins = Coins(screen)
    uhr = Uhr(screen)

    # ### TÜREN ALS EINZELNE VARIABLEN BERECHNEN ###
    # Wir berechnen die Rects einmalig vor der Schleife und speichern sie ab.
    tuer_1_rect = pygame.Rect(0.080 * bg_width, 0.55 * bg_height, 0.04 * bg_width, 0.25 * bg_height)
    tuer_2_rect = pygame.Rect(0.245 * bg_width, 0.55 * bg_height, 0.04 * bg_width, 0.25 * bg_height)
    tuer_3_rect = pygame.Rect(0.405 * bg_width, 0.55 * bg_height, 0.04 * bg_width, 0.25 * bg_height)
    tuer_4_rect = pygame.Rect(0.745 * bg_width, 0.55 * bg_height, 0.04 * bg_width, 0.25 * bg_height)
    tuer_5_rect = pygame.Rect(0.915 * bg_width, 0.55 * bg_height, 0.04 * bg_width, 0.25 * bg_height)

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
                    return GameScreens.RIDDLE1

                elif tuer_2_rect.collidepoint(x_Hintergrund, y_Hintergrund):
                    return GameScreens.RIDDLE2

                elif tuer_3_rect.collidepoint(x_Hintergrund, y_Hintergrund):
                    return GameScreens.RIDDLE3

                elif tuer_4_rect.collidepoint(x_Hintergrund, y_Hintergrund):
                    return GameScreens.RIDDLE4

                elif tuer_5_rect.collidepoint(x_Hintergrund, y_Hintergrund):
                    return GameScreens.RIDDLE5

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if x_pos_hintergrund < -10:
                x_pos_hintergrund += 10

        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if x_pos_hintergrund > -3950:
                x_pos_hintergrund -= 10
        gv.background_x = x_pos_hintergrund

        screen.fill("black")
        straße.draw(screen, x_pos_hintergrund, 0, frame_counter)
        player.update_and_draw(
            max_x_pos=gv.SCREEN_WIDTH / 2 + 1,
            min_x_pos=gv.SCREEN_WIDTH / 2,
            max_y_pos=gv.SCREEN_HIGHT,
            min_y_pos=gv.SCREEN_HIGHT / 2 + 100
        )
        coins.show_coins()
        uhr.uhr_update()

        pygame.display.flip()
        clock.tick(gv.FPS)