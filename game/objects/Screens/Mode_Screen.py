import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.Coins import Coins

def mode_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Mode Screen")

    easy_text = gv.FONT_MIDDLE.render("Easy", True, "white")
    midd_text = gv.FONT_MIDDLE.render("Middle", True, "white")
    hard_text = gv.FONT_MIDDLE.render("Hard", True, "white")
    easy_text_rect = easy_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 100))
    midd_text_rect = midd_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 250))
    hard_text_rect = hard_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 400))


    coins = Coins(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN
                if event.key == pygame.K_SPACE:
                    return GameScreens.PLAY
                if event.key == pygame.K_x:
                    coins.change_coins(100)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY
                if midd_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY
                if hard_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY

        screen.fill((14, 0, 108))
        screen.blit(easy_text, easy_text_rect)
        screen.blit(midd_text, midd_text_rect)
        screen.blit(hard_text, hard_text_rect)
        coins.show_coins()
        pygame.display.flip()
        clock.tick(gv.FPS)
