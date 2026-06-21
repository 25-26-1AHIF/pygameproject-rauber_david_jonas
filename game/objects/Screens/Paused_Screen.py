import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.Coins import Coins
from objects.save_game import save_game

def paused_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Paused Screen")

    pause_text = gv.FONT_BIG.render("PAUSE", True, "white")
    weiter_text = gv.FONT_MIDDLE.render("Weiter Spielen", True, "white")
    pause_text_rect = pause_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 100))
    weiter_text_rect = weiter_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 250))
    speichern_text = gv.FONT_MIDDLE.render("Speichern", True, "white")
    speichern_rect = speichern_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 350))
    coins = Coins(screen)
    straße = Bilder("../assats/Bilder/Häuser_reihe_fertig.png", 1, pygame.Rect(0, 0, 8192, 1024), 80)
    straße.load_spritesheet()
    orginal_straße = straße.images
    bg_width = gv.SCREEN_WIDTH * 8
    bg_height = gv.SCREEN_HIGHT
    groesse_straße = (bg_width, bg_height)
    straße.images = [pygame.transform.smoothscale(img, groesse_straße) for img in orginal_straße]

    Polizei_auto = Bilder("../assats/Bilder/Polizei_auto.png", 2, pygame.Rect(0, 0, 1024, 1024), 30)
    Polizei_auto.load_spritesheet()
    orginal_Polizei_auto = Polizei_auto.images
    groesse_Polizei_auto = (400, 400)
    Polizei_auto.images = [pygame.transform.smoothscale(img, groesse_Polizei_auto) for img in orginal_Polizei_auto]

    xpos_straße = 0
    framecounter = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN
                if event.key == pygame.K_SPACE:
                    return gv.paused_from
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weiter_text_rect.collidepoint(event.pos):
                    return gv.paused_from
                if speichern_rect.collidepoint(event.pos):
                    save_game()
                    return GameScreens.MAIN

        xpos_straße += 70
        if xpos_straße >= bg_width-1024:
            xpos_straße = 0
        framecounter += 1

        screen.fill(("black"))
        straße.draw(screen, xpos_straße*-1, 0, 10)
        Polizei_auto.draw(screen, gv.SCREEN_WIDTH/2-groesse_Polizei_auto[1]/2, 200, framecounter)
        screen.blit(pause_text, pause_text_rect)
        screen.blit(weiter_text, weiter_text_rect)
        screen.blit(speichern_text, speichern_rect)
        coins.show_coins()
        pygame.display.flip()
        clock.tick(gv.FPS)

