import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

        screen.fill("black")
        player.update_and_draw()
        pygame.display.flip()
        clock.tick(gv.FPS)
