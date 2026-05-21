import pygame
from pygame.surface import Surface

from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder


def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Main Screen")
    Geldsack = Bilder("game/Bilder/Geldsack.png", image_count=1, animation_speed=1, image_rect=pygame.Rect(0, 0, 500, 500))
    Geldsack.load_spritesheet()

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



        screen.fill((14, 100, 255))
        screen.blit(titel_text, titel_text_rect)

        screen.blit(starten_text, starten_text_rect)
        Geldsack.draw(screen=screen, xpos=30, ypos=30, frame_counter=1)
        pygame.display.flip()
        clock.tick(gv.FPS)


def play_screen():
    pass

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
        elif GameScreens.actual == GameScreens.EXIT:
            break
    pygame.quit()


if __name__ == "__main__":
    main()
