import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder

def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Main Screen")
    frame_counter = 0

    titel_text = gv.FONT_BIG.render("Räuber", True, "white")
    starten_text = gv.FONT_MIDDLE.render("Starten", True, "white")
    exit_text = gv.FONT_MIDDLE.render("Exit", True, "white")
    str_text = gv.FONT_MIDDLE.render("Steuerung", True, "white")
    titel_text_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 100))
    starten_text_rect = starten_text.get_rect(center=(gv.SCREEN_WIDTH / 2 / 2, 250))
    exit_text_rect = exit_text.get_rect(center=(gv.SCREEN_WIDTH / 2 / 2, 450))
    str_text_rect = str_text.get_rect(center=(gv.SCREEN_WIDTH / 2 / 2, 350))

    Geldsack = Bilder("../assats/Bilder/Geldsack.png", 1, pygame.Rect(0, 0, 128, 128), 1)
    Hintergrund = Bilder("../assats/Bilder/Hintergrund.png", 16, pygame.Rect(0, 0, 1024, 1024), 10)
    Geldsack.load_spritesheet()
    Hintergrund.load_spritesheet()

    groesse = (400, 400)
    groesse_hintergrund = (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)

    Geldsack.images[0] = pygame.transform.smoothscale(Geldsack.images[0], groesse)
    original_hintergrund = Hintergrund.images[:]
    Hintergrund.images = [pygame.transform.smoothscale(img, groesse_hintergrund) for img in original_hintergrund] # mit KI

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return GameScreens.EXIT
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if starten_text_rect.collidepoint(event.pos):
                    return GameScreens.ANIMATION
                if exit_text_rect.collidepoint(event.pos):
                    return GameScreens.EXIT
                if str_text_rect.collidepoint(event.pos):
                    return GameScreens.STR

        Hintergrund.draw(screen, 0, 0, frame_counter)
        screen.blit(titel_text, titel_text_rect)
        Geldsack.draw(screen, gv.SCREEN_WIDTH / 2 - groesse[0] / 2, gv.SCREEN_HIGHT / 2 - groesse[1] / 2 + 10, frame_counter)
        screen.blit(starten_text, starten_text_rect)
        screen.blit(str_text, str_text_rect)
        screen.blit(exit_text, exit_text_rect)

        frame_counter += 1
        pygame.display.flip()
        clock.tick(gv.FPS)
