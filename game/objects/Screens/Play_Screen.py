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

        screen.fill("black")
        player.update_and_draw(gv.SCREEN_WIDTH, 0, gv.SCREEN_HIGHT, 0)
        coins.show_coins()
        pygame.display.flip()
        clock.tick(gv.FPS)
