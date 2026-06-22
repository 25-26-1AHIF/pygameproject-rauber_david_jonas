import pygame
import random
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens

def riddle5_screen(screen, clock):
    pygame.display.set_caption("Riddle 5")
    gv.current_screen = "riddle5"
    ziel = pygame.Rect(300, 300, 60, 60)
    letzter_wechsel = pygame.time.get_ticks()

    text = gv.FONT_MIDDLE.render("Klicke den grünen Block", True,
                                 "white")
    text_rect = text.get_rect(center=(220, 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ziel.collidepoint(event.pos):
                    if gv.wohnwagen == True:
                        gv.wohnwagen = False
                        return GameScreens.WAGEN
                    elif gv.haus_2 == True:
                        gv.haus_2 = False
                        return GameScreens.GANG2
                    elif gv.haus_3 == True:
                        gv.haus_3 = False
                        return GameScreens.GANG3
                    elif gv.haus_4 == True:
                        gv.haus_4 = False
                        return GameScreens.GANG4
                    else:
                        return GameScreens.GANG1

        aktuelle_zeit = pygame.time.get_ticks()

        if aktuelle_zeit - letzter_wechsel > 1000:
            ziel.x = random.randint(50, 690)
            ziel.y = random.randint(100, 490)
            letzter_wechsel = aktuelle_zeit

        screen.fill("black")
        screen.blit(text, text_rect)
        pygame.draw.rect(screen, "green", ziel, width=0)
        pygame.display.flip()
        clock.tick(gv.FPS)
