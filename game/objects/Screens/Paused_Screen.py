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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN
                if event.key == pygame.K_SPACE:
                    return gv.paused_from
                if event.key == pygame.K_x:
                    coins.change_coins(100)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weiter_text_rect.collidepoint(event.pos):
                    return gv.paused_from
                if speichern_rect.collidepoint(event.pos):
                    save_game()
                    return GameScreens.MAIN

        screen.fill((14, 0, 108))
        screen.blit(pause_text, pause_text_rect)
        screen.blit(weiter_text, weiter_text_rect)
        screen.blit(speichern_text, speichern_rect)
        coins.show_coins()
        pygame.display.flip()
        clock.tick(gv.FPS)

