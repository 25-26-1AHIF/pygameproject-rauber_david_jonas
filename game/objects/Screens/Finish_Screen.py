import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Coins import Coins
from objects.Uhr import Uhr

def finish_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Finish Screen")

    gesammelte_coins = gv.coins
    stunden = gv.stunden
    sekunden = gv.sekunden

    headline_text = gv.FONT_MIDDLE.render("Rundenauswertung", True, "yellow")
    headline_rect = headline_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 100))
    zeit_text = gv.FONT_MIDDLE.render(f"Benötigte Zeit: {stunden:02d}:{sekunden:02d}", True, "white")
    zeit_rect = zeit_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 220))
    coins_text = gv.FONT_MIDDLE.render(f"Gesammelte Münzen: {gesammelte_coins}", True, "white")
    coins_rect = coins_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 300))
    zurück_text = gv.FONT_SMALL.render("Run beenden", True, "gray")
    zurück_rect = zurück_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 450))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if zurück_rect.collidepoint(event.pos):
                    return GameScreens.MAIN

        screen.fill((25, 30, 45))

        screen.blit(headline_text, headline_rect)
        screen.blit(zeit_text, zeit_rect)
        screen.blit(coins_text, coins_rect)
        screen.blit(zurück_text, zurück_rect)

        pygame.display.flip()
        clock.tick(gv.FPS)