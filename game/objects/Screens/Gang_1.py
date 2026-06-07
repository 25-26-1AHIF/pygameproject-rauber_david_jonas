import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player


def Gang_1(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Room_1 Screen")
    frame_counter = 0

    # Spieler initialisieren
    player_x_pos = gv.SCREEN_WIDTH / 2 - gv.player_size / 2
    player_y_pos = gv.SCREEN_HIGHT - gv.player_size - 110
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

    #tür positionen wurden mithilfe gemini berechnet
    door1_rect = pygame.Rect(gv.SCREEN_WIDTH * 0.23, gv.SCREEN_HIGHT * 0.40, gv.SCREEN_WIDTH * 0.07,
                             gv.SCREEN_HIGHT * 0.35)  # Tür Links
    door2_rect = pygame.Rect(gv.SCREEN_WIDTH * 0.34, gv.SCREEN_HIGHT * 0.35, gv.SCREEN_WIDTH * 0.08,
                             gv.SCREEN_HIGHT * 0.20)  # Tür Hinten links
    door3_rect = pygame.Rect(gv.SCREEN_WIDTH * 0.47, gv.SCREEN_HIGHT * 0.35, gv.SCREEN_WIDTH * 0.08,
                             gv.SCREEN_HIGHT * 0.20)  # Tür Hinten rechts
    door4_rect = pygame.Rect(gv.SCREEN_WIDTH * 0.64, gv.SCREEN_HIGHT * 0.40, gv.SCREEN_WIDTH * 0.07,
                             gv.SCREEN_HIGHT * 0.35)  # Tür Rechts

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

        screen.fill("black")
        raum.draw(screen, 0, 0, frame_counter)
        player.update_and_draw(gv.SCREEN_WIDTH, 0, gv.SCREEN_HIGHT, 0)



        player_rect = pygame.Rect(player.player_x_pos, player.player_y_pos, gv.player_size, gv.player_size)


        if player_rect.colliderect(door1_rect):
            return GameScreens.ROOM_1
        elif player_rect.colliderect(door2_rect):
            return GameScreens.ROOM_2
        elif player_rect.colliderect(door3_rect):
            return GameScreens.ROOM_3
        elif player_rect.colliderect(door4_rect):
            return GameScreens.ROOM_4

        #hittboxen für türen zeichnen
        # pygame.draw.rect(screen, "red", door1_rect, 2)
        # pygame.draw.rect(screen, "blue", door2_rect, 2)
        # pygame.draw.rect(screen, "green", door3_rect, 2)
        # pygame.draw.rect(screen, "yellow", door4_rect, 2)
        # pygame.draw.rect(screen, "white", player_rect, 2)


        pygame.display.flip()
        clock.tick(gv.FPS)