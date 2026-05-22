import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder

def steuerung_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Steuerungs Screen")

    str_text = gv.FONT_BIG.render("Steuerung:", True, "white")
    zurueck_text = gv.FONT_MIDDLE.render("Zurück", True, "white")

    w_text = gv.FONT_MIDDLE.render("Move up:    W / ˄", True, "white")
    a_text = gv.FONT_MIDDLE.render("Move left:  A / ˃", True, "white")
    s_text = gv.FONT_MIDDLE.render("Move down:  S / ˅", True, "white")
    d_text = gv.FONT_MIDDLE.render("Move right: D / ˂", True, "white")

    pause_text_rect = str_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 100))
    zurueck_text_rect = zurueck_text.get_rect(center=(100, 100))

    w_text_rect = w_text.get_rect(center=(gv.SCREEN_WIDTH / 2 / 2, 300))
    a_text_rect = a_text.get_rect(center=(gv.SCREEN_WIDTH / 2 + gv.SCREEN_WIDTH / 2 /2,
                                          300))
    s_text_rect = s_text.get_rect(center=(gv.SCREEN_WIDTH / 2 + gv.SCREEN_WIDTH / 2 / 2,
                                          400))
    d_text_rect = d_text.get_rect(center=(gv.SCREEN_WIDTH / 2 / 2, 400))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN
                if event.key == pygame.K_SPACE:
                    return GameScreens.PLAY
            if event.type == pygame.MOUSEBUTTONDOWN:
                if zurueck_text_rect.collidepoint(event.pos):
                    return GameScreens.MAIN

        screen.fill("black")
        screen.blit(str_text, pause_text_rect)

        screen.blit(w_text, w_text_rect)
        screen.blit(a_text, a_text_rect)
        screen.blit(s_text, s_text_rect)
        screen.blit(d_text, d_text_rect)

        screen.blit(zurueck_text, zurueck_text_rect)

        pygame.display.flip()
        clock.tick(gv.FPS)
