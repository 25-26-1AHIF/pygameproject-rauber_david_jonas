import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder as B, Bilder


def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Main Screen")

    titel_text = gv.FONT_BIG.render("Räuber", True, "white")
    starten_text = gv.FONT_MIDDLE.render("Starten", True, "white")
    titel_text_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 100))
    starten_text_rect = starten_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 250))
    Geldsack = Bilder("Bilder/Geldsack.png", 1, pygame.Rect(0, 0, 48, 48), 1)
    Geldsack.load_spritesheet()
    groesse = (400,400)
    Geldsack.images[0] = pygame.transform.smoothscale(Geldsack.images[0], groesse)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.EXIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                if starten_text_rect.collidepoint(event.pos):
                    return GameScreens.ANIMATION



        screen.fill((14, 0, 108))
        screen.blit(titel_text, titel_text_rect)
        Geldsack.draw(screen, gv.SCREEN_WIDTH/2-groesse[0]/2+25,gv.SCREEN_HIGHT/2-groesse[0]/2-25, 1)
        screen.blit(starten_text, starten_text_rect)

        pygame.display.flip()
        clock.tick(gv.FPS)


def play_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pass

def animation_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Animation")

    clock = pygame.time.Clock()
    running = True

    Geldsack = Bilder("Bilder/Geldsack.png", 1, pygame.Rect(0, 0, 48, 48), 1)
    Geldsack.load_spritesheet()
    groesse = (400,400)
    Geldsack.images[0] = pygame.transform.smoothscale(Geldsack.images[0], groesse)
    Geldsack.draw(screen, gv.SCREEN_WIDTH / 2 - groesse[0] / 2 + 25, gv.SCREEN_HIGHT / 2 - groesse[0] / 2 - 25, 1)

    original = Geldsack.images[0]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        Geldsack.draw(screen, gv.SCREEN_WIDTH / 2 - groesse[0] / 2 + 25, gv.SCREEN_HIGHT / 2 - groesse[0] / 2 - 25,1)
        groesse_neu = (groesse[0] + 10, groesse[1] + 10)
        groesse = groesse_neu
        Geldsack.images[0] = pygame.transform.smoothscale(original, groesse)

        if groesse[0] > 10000:
            return GameScreens.PLAY

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def main():
    gv.init()
    screen = pygame.display.set_mode(
        (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)
    )
    clock = pygame.time.Clock()


    while True:
        if GameScreens.actual == GameScreens.MAIN:
            GameScreens.actual = main_screen(screen, clock)
        elif GameScreens.actual == GameScreens.ANIMATION:
            GameScreens.actual = animation_screen(screen, clock)
        elif GameScreens.actual == GameScreens.PLAY:
            GameScreens.actual = play_screen(screen, clock)
        elif GameScreens.actual == GameScreens.EXIT:
            break




    pygame.quit()


if __name__ == "__main__":
    main()
