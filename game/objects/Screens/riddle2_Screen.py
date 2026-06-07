import pygame
import random
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder

def riddle2_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Riddle2 Screen")
    gv.current_screen = "riddle2"

    while True:
        schalter = []
        for i in range(4):
            schalter.append(random.choice([True, False]))
        if schalter == [True, True, True, True]:
            continue
        else:
            break

    if schalter[0] == True:
        schalter1_text = gv.FONT_MIDDLE.render("An", True, "green")
    else:
        schalter1_text = gv.FONT_MIDDLE.render("Aus", True, "red")

    if schalter[1] == True:
        schalter2_text = gv.FONT_MIDDLE.render("An", True, "green")
    else:
        schalter2_text = gv.FONT_MIDDLE.render("Aus", True, "red")

    if schalter[2] == True:
        schalter3_text = gv.FONT_MIDDLE.render("An", True, "green")
    else:
        schalter3_text = gv.FONT_MIDDLE.render("Aus", True, "red")

    if schalter[3] == True:
        schalter4_text = gv.FONT_MIDDLE.render("An", True, "green")
    else:
        schalter4_text = gv.FONT_MIDDLE.render("Aus", True, "red")

    schalter1_rect = schalter1_text.get_rect(center=(100, 300))
    schalter2_rect = schalter2_text.get_rect(center=(300, 300))
    schalter3_rect = schalter3_text.get_rect(center=(500, 300))
    schalter4_rect = schalter4_text.get_rect(center=(700, 300))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gv.paused_from = GameScreens.RIDDLE2
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if schalter1_rect.collidepoint(event.pos):
                    if schalter[0] == True:
                        schalter[0] = False
                    else:
                        schalter[0] = True

                if schalter2_rect.collidepoint(event.pos):
                    if schalter2_rect.collidepoint(event.pos):

                        if schalter[1] == True:
                            schalter[1] = False
                        else:
                            schalter[1] = True

                        if schalter[0] == True:
                            schalter[0] = False
                        else:
                            schalter[0] = True

                        if schalter[2] == True:
                            schalter[2] = False
                        else:
                            schalter[2] = True

                if schalter3_rect.collidepoint(event.pos):
                    if schalter3_rect.collidepoint(event.pos):

                        if schalter[2] == True:
                            schalter[2] = False
                        else:
                            schalter[2] = True

                        if schalter[1] == True:
                            schalter[1] = False
                        else:
                            schalter[1] = True

                        if schalter[3] == True:
                            schalter[3] = False
                        else:
                            schalter[3] = True

                if schalter4_rect.collidepoint(event.pos):
                    if schalter4_rect.collidepoint(event.pos):

                        if schalter[3] == True:
                            schalter[3] = False
                        else:
                            schalter[3] = True

                        if schalter[2] == True:
                            schalter[2] = False
                        else:
                            schalter[2] = True

                if schalter == [True, True, True, True]:
                    return GameScreens.GANG1

                screen.fill("black")

                if schalter[0] == True:
                    schalter1_text = gv.FONT_MIDDLE.render("An",
                                                           True, "green")
                else:
                    schalter1_text = gv.FONT_MIDDLE.render("Aus",
                                                           True, "red")

                if schalter[1] == True:
                    schalter2_text = gv.FONT_MIDDLE.render("An",
                                                           True, "green")
                else:
                    schalter2_text = gv.FONT_MIDDLE.render("Aus",
                                                           True, "red")

                if schalter[2] == True:
                    schalter3_text = gv.FONT_MIDDLE.render("An",
                                                           True, "green")
                else:
                    schalter3_text = gv.FONT_MIDDLE.render("Aus",
                                                           True, "red")

                if schalter[3] == True:
                    schalter4_text = gv.FONT_MIDDLE.render("An",
                                                           True, "green")
                else:
                    schalter4_text = gv.FONT_MIDDLE.render("Aus",
                                                           True, "red")

        screen.fill("black")
        screen.blit(schalter1_text, schalter1_rect)
        screen.blit(schalter2_text, schalter2_rect)
        screen.blit(schalter3_text, schalter3_rect)
        screen.blit(schalter4_text, schalter4_rect)

        pygame.display.flip()
        clock.tick(gv.FPS)
