import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Uhr import Uhr
from objects.Coins import Coins

def room2_3(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Room_1 Screen")
    gv.current_screen = "room2"
    frame_counter = 0
    uhr = Uhr(screen)
    coins = Coins(screen)
    player_x_pos = gv.SCREEN_WIDTH / 2 - gv.player_size / 2
    player_y_pos = gv.SCREEN_HIGHT - gv.player_size - 110
    player = Player(
        screen=screen,
        player_x_pos=player_x_pos,
        player_y_pos=player_y_pos
    )

    raum = Bilder("../assats/Bilder/Rooms/Haus_reich.png", 1, pygame.Rect(1024, 0, 1024, 1024), 20)
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
                    gv.paused_from = GameScreens.ROOM_2
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY

        screen.fill("black")
        raum.draw(screen, 0,0,frame_counter)
        player.update_and_draw(gv.SCREEN_WIDTH, 0,
                               gv.SCREEN_HIGHT - 210, gv.SCREEN_HIGHT / 2)
        if player.player_x_pos > gv.SCREEN_WIDTH - 60:
            return GameScreens.GANG3
        uhr.uhr_update()
        coins.show_coins()
        pygame.display.flip()
        clock.tick(gv.FPS)
