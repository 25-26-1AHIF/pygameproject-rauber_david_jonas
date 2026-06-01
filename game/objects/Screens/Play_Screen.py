import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Coins import Coins

def play_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Play Screen")
    player_x_pos = gv.SCREEN_WIDTH / 2 - gv.player_size / 2
    player_y_pos = gv.SCREEN_HIGHT - gv.player_size - 10
    player = Player(
        screen=screen,
        player_x_pos=player_x_pos,
        player_y_pos=player_y_pos
    )
    frame_counter = 0


    straße = Bilder("../assats/Bilder/Häuser_reihe_fertig.png", 1, pygame.Rect(0, 0, 6144, 1024), 80)
    straße.load_spritesheet()
    orginal_straße = straße.images
    groesse_straße = (gv.SCREEN_WIDTH*6, gv.SCREEN_HIGHT)
    straße.images = [pygame.transform.smoothscale(img, groesse_straße) for img in orginal_straße]  # mit KI
    x_pos_hintergrund = 1
    coins = Coins(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN
                if event.key == pygame.K_q:
                    return GameScreens.RIDDLE1
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
                if x_pos_hintergrund < -10:
                    x_pos_hintergrund += 10
            if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
                if x_pos_hintergrund > -6134:
                    x_pos_hintergrund += -10

        screen.fill("black")
        straße.draw(screen,x_pos_hintergrund, 0, frame_counter)
        player.update_and_draw(max_x_pos=gv.SCREEN_WIDTH/2, min_x_pos=gv.SCREEN_WIDTH/2-1, max_y_pos=gv.SCREEN_HIGHT, min_y_pos=gv.SCREEN_HIGHT/3*2)
        coins.show_coins()
        pygame.display.flip()
        clock.tick(gv.FPS)
