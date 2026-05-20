import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens

def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Main Screen")

    titel_text = gv.FONT_BIG.render("Räuber", True, "white")
    starten_text = gv.FONT_MIDDLE.render("Starten", True, "white")
    titel_text_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 100))
    starten_text_rect = starten_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 250))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.EXIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                if starten_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY

        screen.fill((14, 0, 108))
        screen.blit(titel_text, titel_text_rect)
        pygame.draw.rect(
            surface=screen,
            rect=starten_text_rect,
            color=(14,0,108),
            width=0
        )
        screen.blit(starten_text, starten_text_rect)

        pygame.display.flip()
        clock.tick(gv.FPS)


def play_screen(screen: pygame.Surface, clock: pygame.time.Clock):

    pygame.init()
    pygame.display.set_caption("Play Screen")



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN

        screen.fill("black")
        pygame.display.flip()
        clock.tick(gv.FPS)

def paused_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Paused Screen")

    pause_text = gv.FONT_BIG.render("PAUSE", True, "white")
    weiter_text = gv.FONT_MIDDLE.render("Weiter Spielen", True, "white")
    pause_text_rect = pause_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 100))
    weiter_text_rect = weiter_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 250))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.EXIT
                if event.key == pygame.K_SPACE:
                    return GameScreens.PLAY
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weiter_text_rect.collidepoint(event.pos):
                    return GameScreens.PLAY

        screen.fill((14, 0, 108))
        screen.blit(pause_text, pause_text_rect)
        pygame.draw.rect(
            surface=screen,
            rect=weiter_text_rect,
            color=(14, 0, 108),
            width=0
        )
        screen.blit(weiter_text, weiter_text_rect)

        pygame.display.flip()
        clock.tick(gv.FPS)

def main():
    gv.init()
    screen = pygame.display.set_mode(
        (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)
    )
    clock = pygame.time.Clock()

    while True:
        if GameScreens.actual == GameScreens.MAIN:
            GameScreens.actual = main_screen(screen, clock)
        elif GameScreens.actual == GameScreens.PLAY:
            GameScreens.actual = play_screen(screen, clock)
        elif GameScreens.actual == GameScreens.PAUSED:
            GameScreens.actual = paused_screen(screen, clock)
        elif GameScreens.actual == GameScreens.EXIT:
            break
    pygame.quit()


if __name__ == "__main__":
    main()
