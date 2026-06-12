import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens
import random

def riddle3_screen(screen, clock):
    pygame.display.set_caption("Riddle 3")
    gv.current_screen = "riddle3"

    zahl = str(random.randint(1000, 9999))

    text = gv.FONT_BIG.render(zahl, True, "white")

    screen.fill("black")
    screen.blit(text, (300, 250))
    pygame.display.flip()
    pygame.time.delay(3000)

    eingabe = "" # Mit Hilfe von KI

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY
                if event.key == pygame.K_RETURN:
                    if eingabe == zahl:
                        return GameScreens.WAGEN
                    else:
                        screen.fill("black")
                        screen.blit(text, (300, 250))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                    eingabe = ""
                elif event.key == pygame.K_BACKSPACE:
                    eingabe = eingabe[:-1]
                else:
                    eingabe += event.unicode

        screen.fill("black")
        info = gv.FONT_MIDDLE.render(
            "Welche Zahl wurde gezeigt?",
            True,
            "white"
        )
        user_text = gv.FONT_BIG.render(eingabe, True, "green")
        screen.blit(info, (180, 150))
        screen.blit(user_text, (300, 300))
        pygame.display.flip()
        clock.tick(gv.FPS)
