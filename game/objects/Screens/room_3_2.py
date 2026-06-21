import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Uhr import Uhr
from objects.Coins import Coins
from objects.Screens.Object import Object


def room3_2(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Room_1 Screen")
    gv.current_screen = "room3"
    uhr = Uhr(screen)
    coins = Coins(screen)
    frame_counter = 0
    player_x_pos = gv.SCREEN_WIDTH / 2 - gv.player_size / 2
    player_y_pos = gv.SCREEN_HIGHT - gv.player_size - 110

    player = Player(
        screen=screen,
        player_x_pos=player_x_pos,
        player_y_pos=player_y_pos
    )

    raum = Bilder("../assats/Bilder/Rooms/Haus_2.png", 1, pygame.Rect(4096, 0, 1024, 1024), 80)
    Pc = Object("../assats/Bilder/Pc.png", 1000, screen, 280, 300, pygame.Rect(0, 0, 300, 300), 12, 5, 12,gv.Pc_geklaut, gv.Pc_auszahlung)

    raum.load_spritesheet()
    Pc.sprite.load_spritesheet()


    orginal_raum = raum.images
    orginal_Pc = Pc.sprite.images

    groesse_raum_1 = (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)
    groesse_Pc = (200, 200)

    raum.images = [pygame.transform.smoothscale(img, groesse_raum_1) for img in orginal_raum]
    Pc.sprite.images = [pygame.transform.smoothscale(img, groesse_Pc) for img in orginal_Pc]
    while True:
        frame_counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gv.paused_from = GameScreens.ROOM_3
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Pc.rect.collidepoint(event.pos):
                    Pc.geklaut = True
                    gv.Pc_auszahlung = True
                    gv.Pc_geklaut = True

        screen.fill("black")
        raum.draw(screen, 0, 0, frame_counter)
        player.update_and_draw(gv.SCREEN_WIDTH, 0, gv.SCREEN_HIGHT - 110, gv.SCREEN_HIGHT / 2 + 90)


        Pc.update_and_draw()

        if player.player_x_pos < 60:
            return GameScreens.GANG2

        uhr.uhr_update()
        coins.show_coins()

        pygame.display.flip()
        clock.tick(gv.FPS)
