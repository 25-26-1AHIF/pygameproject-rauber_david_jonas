import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder

def shop_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Shop Screen")

    back_text = gv.FONT_MIDDLE.render("Zurück", True, "white")
    back_text_rect = back_text.get_rect(center=(100, 50))

    blue_skin = Bilder("../assats/Bilder/Player_standing_blue.png",
        1,
        image_rect=pygame.Rect(0, 0, 400, 400),
        animation_speed=1
    )

    red_skin = Bilder("../assats/Bilder/Player_standing_red.png",
        1,
        image_rect=pygame.Rect(0, 0, 400, 400),
        animation_speed=1
    )

    green_skin = Bilder("../assats/Bilder/Player_standing_green.png",
        1,
        image_rect=pygame.Rect(0, 0, 400, 400),
        animation_speed=1
    )

    yellow_skin = Bilder("../assats/Bilder/Player_standing_rainbow.png",
        1,
        image_rect=pygame.Rect(0, 0, 400, 400),
        animation_speed=1
    )

    basic_skin = Bilder("../assats/Bilder/PLayer standing.png",
                        1,
                        image_rect=pygame.Rect(0, 0, 400, 400),
                        animation_speed=1)

    blue_skin.load_spritesheet()
    red_skin.load_spritesheet()
    green_skin.load_spritesheet()
    yellow_skin.load_spritesheet()
    basic_skin.load_spritesheet()

    # Start KI
    blue_skin.images[0] = pygame.transform.scale(
        blue_skin.images[0], (200, 200)
    )

    red_skin.images[0] = pygame.transform.scale(
        red_skin.images[0], (200, 200)
    )

    green_skin.images[0] = pygame.transform.scale(
        green_skin.images[0], (200, 200)
    )

    yellow_skin.images[0] = pygame.transform.scale(
        yellow_skin.images[0], (200, 200)
    )

    basic_skin.images[0] = pygame.transform.scale(
        basic_skin.images[0], (200, 200)
    )
    # Ende KI

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN
                if event.key == pygame.K_SPACE:
                    return GameScreens.PLAY
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_text_rect.collidepoint(event.pos):
                    return GameScreens.MAIN

        screen.fill("black")

        # Start von KI
        screen.blit(blue_skin.images[0], (500, 50))
        screen.blit(red_skin.images[0], (50, 350))
        screen.blit(green_skin.images[0], (300, 350))
        screen.blit(yellow_skin.images[0], (550, 350))
        screen.blit(basic_skin.images[0], (250, 50))
        # Ende KI

        screen.blit(back_text, back_text_rect)

        pygame.display.flip()
        clock.tick(gv.FPS)
