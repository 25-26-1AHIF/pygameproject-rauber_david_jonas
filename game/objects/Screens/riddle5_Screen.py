import pygame
import random
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens

def riddle5_screen(screen, clock):
    pygame.display.set_caption("Riddle 5")
    gv.current_screen = "riddle5"
    ziel = pygame.Rect(300, 300, 60, 60)
    letzter_wechsel = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ziel.collidepoint(event.pos):
                    return GameScreens.ROOM_1

        aktuelle_zeit = pygame.time.get_ticks()

        if aktuelle_zeit - letzter_wechsel > 1000:
            ziel.x = random.randint(50, 690)
            ziel.y = random.randint(100, 490)
            letzter_wechsel = aktuelle_zeit

        screen.fill("black")
        text = gv.FONT_MIDDLE.render("Klicke den grünen Block",True,
                                     "white")
        text_rect = text.get_rect(center=(220, 50))
        screen.blit(text, text_rect)
        pygame.draw.rect(screen, "green", ziel, width=0)
        pygame.display.flip()
        clock.tick(gv.FPS)
