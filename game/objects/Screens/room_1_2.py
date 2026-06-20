import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Uhr import Uhr
from objects.Coins import Coins

def room1_2(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Room_1 Screen")
    gv.current_screen = "room1"
    frame_counter = 0
    player_x_pos = gv.player_x
    player_y_pos = gv.player_y
    player = Player(
        screen=screen,
        player_x_pos=player_x_pos,
        player_y_pos=player_y_pos
    )
    uhr = Uhr(screen)
    coins = Coins(screen)

    raum = Bilder("../assats/Bilder/Rooms/Haus_2.png", 3,pygame.Rect(0, 0, 1024, 1024),10)
    raum.load_spritesheet()
    orginal_raum = raum.images
    groesse_raum_1 = (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)
    raum.images = [pygame.transform.smoothscale(img, groesse_raum_1) for img in orginal_raum] # mit KI



    while True:
        frame_counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gv.paused_from = GameScreens.ROOM_1
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY

        screen.fill("black")
        raum.draw(screen, 0,0,frame_counter)
        player.update_and_draw(gv.SCREEN_WIDTH, 0,
                               gv.SCREEN_HIGHT-110, gv.SCREEN_HIGHT/2 + 90)

        if player.player_x_pos > gv.SCREEN_WIDTH - 60:
            return GameScreens.GANG2

        uhr.uhr_update()
        coins.show_coins()
        pygame.display.flip()
        clock.tick(gv.FPS)
