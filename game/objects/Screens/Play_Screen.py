import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Coins import Coins
from objects.Uhr import Uhr
import random

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

    tueren_relativ = [
        (0.080, 0.55, 0.04, 0.25),
        (0.245, 0.55, 0.04, 0.25),
        (0.405, 0.55, 0.04, 0.25),
        (0.745, 0.55, 0.04, 0.25),
        (0.915, 0.55, 0.04, 0.25)
    ]

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
                mx, my = event.pos
                bg_click_x = mx - x_pos_hintergrund
                bg_click_y = my

                for tx, ty, tw, th in tueren_relativ:
                    door_rect = pygame.Rect(
                        tx * bg_width,
                        ty * bg_height,
                        tw * bg_width,
                        th * bg_height
                    )

                    if door_rect.collidepoint(bg_click_x, bg_click_y):
                        return random.choice([GameScreens.RIDDLE1, GameScreens.RIDDLE2,
                                              GameScreens.RIDDLE3, GameScreens.RIDDLE4,
                                              GameScreens.RIDDLE5])

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if x_pos_hintergrund < -10:
                x_pos_hintergrund += 10

        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if x_pos_hintergrund > -6134:
                x_pos_hintergrund -= 10
        gv.background_x = x_pos_hintergrund

        screen.fill("black")
        straße.draw(screen, x_pos_hintergrund, 0, frame_counter)
        player.update_and_draw(
            max_x_pos=450,
            min_x_pos=50,
            max_y_pos=gv.SCREEN_HIGHT,
            min_y_pos=gv.SCREEN_HIGHT / 2 + 100
        )
        coins.show_coins()
        uhr.uhr_update()

        pygame.display.flip()
        clock.tick(gv.FPS)

