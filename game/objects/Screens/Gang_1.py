import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Uhr import Uhr
from objects.Coins import Coins
from objects.Screens.Object import Object



def Gang_1(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Room_1 Screen")
    frame_counter = 0

    coins = Coins(screen)
    uhr = Uhr(screen)

    # Spieler initialisieren
    player_x_pos = gv.SCREEN_WIDTH / 2 - gv.player_size / 2
    player_y_pos = gv.SCREEN_HIGHT - gv.player_size - 110 -60
    player = Player(
        screen=screen,
        player_x_pos=player_x_pos,
        player_y_pos=player_y_pos
    )

    raum = Bilder("../assats/Bilder/Rooms/Gang_1.png", 1, pygame.Rect(0, 0, 1024, 1024), 1)
    raum.load_spritesheet()
    orginal_gang = raum.images
    groesse_gang = (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)
    raum.images = [pygame.transform.smoothscale(img, groesse_gang) for img in orginal_gang]

    #Test_object = Object("../assats/Bilder/Test_object.png", 100, screen, 50, 50, pygame.Rect(0, 0, 128, 128), 1, 1, 1, gv.Test_object_geklaut, gv.Test_object_auszahlung)
    #tür positionen wurden mithilfe gemini berechnet
    door1_rect = pygame.Rect(gv.SCREEN_WIDTH * 0.23, gv.SCREEN_HIGHT * 0.40, gv.SCREEN_WIDTH * 0.07,
                             gv.SCREEN_HIGHT * 0.35)  # Tür Links
    door2_rect = pygame.Rect(gv.SCREEN_WIDTH * 0.34, gv.SCREEN_HIGHT * 0.35, gv.SCREEN_WIDTH * 0.08,
                             gv.SCREEN_HIGHT * 0.20)  # Tür Hinten links
    door3_rect = pygame.Rect(gv.SCREEN_WIDTH * 0.47, gv.SCREEN_HIGHT * 0.35, gv.SCREEN_WIDTH * 0.08,
                             gv.SCREEN_HIGHT * 0.20)  # Tür Hinten rechts
    door4_rect = pygame.Rect(gv.SCREEN_WIDTH * 0.64, gv.SCREEN_HIGHT * 0.40, gv.SCREEN_WIDTH * 0.07,
                             gv.SCREEN_HIGHT * 0.35)  # Tür Rechts
    exit_rect = pygame.Rect(0, gv.SCREEN_HIGHT-70, gv.SCREEN_WIDTH, 10)



    while True:
        frame_counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY

            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if Test_object.rect.collidepoint(event.pos):
                    #Test_object.geklaut = True
                    #gv.Test_object_geklaut = True
                    #gv.Test_object_auszahlung = True


        screen.fill("black")
        raum.draw(screen, 0, 0, frame_counter)
        player.update_and_draw(gv.SCREEN_WIDTH - 280, gv.SCREEN_WIDTH / 2 / 2,
                               gv.SCREEN_HIGHT - 50, gv.SCREEN_HIGHT / 2 - 100)



        player_rect = pygame.Rect(player.player_x_pos + 60, player.player_y_pos + 65, gv.player_size, gv.player_size)


        if player_rect.colliderect(door1_rect):
            return GameScreens.ROOM_1
        elif player_rect.colliderect(door2_rect):
            return GameScreens.ROOM_2
        elif player_rect.colliderect(door3_rect):
            return GameScreens.ROOM_3
        elif player_rect.colliderect(door4_rect):
            return GameScreens.ROOM_4
        elif player_rect.colliderect(exit_rect):
            return GameScreens.PLAY

        #Test_object.update_and_draw()

        #hittboxen für türen zeichnen
        #pygame.draw.rect(screen, "red", door1_rect, 2)
        #pygame.draw.rect(screen, "blue", door2_rect, 2)
        #pygame.draw.rect(screen, "green", door3_rect, 2)
        #pygame.draw.rect(screen, "yellow", door4_rect, 2)
        #pygame.draw.rect(screen, "white", player_rect, 2)
        #pygame.draw.rect(screen, "red", exit_rect)


        coins.show_coins()
        uhr.uhr_update()

        pygame.display.flip()
        clock.tick(gv.FPS)

