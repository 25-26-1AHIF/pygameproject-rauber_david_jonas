import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player


def room1_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Room_1 Screen")
    frame_counter = 0


    raum = Bilder("../assats/Bilder/Raum 1.png", 2,pygame.Rect(0, 0, 1024, 1024),80)
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
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY

        screen.fill("black")
        raum.draw(screen, 0,0,frame_counter)

        pygame.display.flip()
        clock.tick(gv.FPS)
