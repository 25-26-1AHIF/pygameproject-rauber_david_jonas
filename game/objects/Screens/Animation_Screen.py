import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder

def animation_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Animation")
    frame_counter = 0

    Geldsack = Bilder("../assats/Bilder/Geldsack.png", 1, pygame.Rect(0, 0, 128, 128), 1)
    Hintergrund = Bilder("../assats/Bilder/Hintergrund.png", 15, pygame.Rect(0, 0, 1024, 1024), 2)
    Geldsack.load_spritesheet()
    Hintergrund.load_spritesheet()

    groesse = (400, 400)
    groesse_hintergrund = (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)

    original_geldsack = Geldsack.images[0]
    original_hintergrund = Hintergrund.images[:]
    Hintergrund.images = [pygame.transform.smoothscale(img, groesse_hintergrund) for img in original_hintergrund]
    Geldsack.images[0] = pygame.transform.smoothscale(original_geldsack, groesse)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return GameScreens.EXIT

        screen.fill("black")
        Hintergrund.draw(screen, 0, 0, frame_counter)

        Geldsack.draw(
            screen,
            gv.SCREEN_WIDTH / 2 - groesse[0] / 2,
            gv.SCREEN_HIGHT / 2 - groesse[1] / 2 + 10,
            frame_counter
        )

        groesse = (groesse[0] + 50, groesse[1] + 50)
        Geldsack.images[0] = pygame.transform.smoothscale(original_geldsack, groesse)

        frame_counter += 1

        if groesse[0] > gv.SCREEN_WIDTH * 3:
            return GameScreens.PLAY

        pygame.display.flip()
        clock.tick(60)
