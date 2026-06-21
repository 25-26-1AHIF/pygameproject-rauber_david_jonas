import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.Coins import Coins

def shop_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Shop Screen")

    coins = Coins(screen)

    back_text = gv.FONT_MIDDLE.render("Zurück", True, "white")
    back_text_rect = back_text.get_rect(center=(100, 50))

    basic_text = gv.FONT_MIDDLE.render("Ausgerüstet", True, "green")
    basic_text_rect = basic_text.get_rect(center=(350, 280))
    kaufen_text_blue = gv.FONT_MIDDLE.render("100$", True, "white")
    kaufen_text_blue_rect = kaufen_text_blue.get_rect(center=(600, 280))
    kaufen_text_red = gv.FONT_MIDDLE.render("200$", True, "white")
    kaufen_text_red_rect = kaufen_text_red.get_rect(center=(150, 580))
    kaufen_text_green = gv.FONT_MIDDLE.render("500$", True, "white")
    kaufen_text_green_rect = kaufen_text_green.get_rect(center=(400, 580))
    kaufen_text_rainbow = gv.FONT_MIDDLE.render("1000$", True, "white")
    kaufen_text_rainbow_rect = kaufen_text_rainbow.get_rect(center=(650, 580))

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

    rainbow_skin = Bilder("../assats/Bilder/Player_standing_rainbow.png",
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
    rainbow_skin.load_spritesheet()
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

    rainbow_skin.images[0] = pygame.transform.scale(
        rainbow_skin.images[0], (200, 200)
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

                if basic_text_rect.collidepoint(event.pos):
                    gv.aktueller_skin_standing = "basic"
                    gv.aktueller_skin_moving = "basic"

                if kaufen_text_blue_rect.collidepoint(event.pos):
                    if gv.blue_skin_gekauft == False:
                        if gv.coins >= 100:
                            gv.coins -= 100
                            gv.blue_skin_gekauft = True
                    else:
                        gv.aktueller_skin_standing = "blue"
                        gv.aktueller_skin_moving = "blue"
                if kaufen_text_red_rect.collidepoint(event.pos):
                    if gv.red_skin_gekauft == False:
                        if gv.coins >= 200:
                            gv.coins -= 200
                            gv.red_skin_gekauft = True
                    else:
                        gv.aktueller_skin_standing = "red"
                        gv.aktueller_skin_moving = "red"
                if kaufen_text_green_rect.collidepoint(event.pos):
                    if gv.green_skin_gekauft == False:
                        if gv.coins >= 500:
                            gv.coins -= 500
                            gv.green_skin_gekauft = True
                    else:
                        gv.aktueller_skin_standing = "green"
                        gv.aktueller_skin_moving = "green"
                if kaufen_text_rainbow_rect.collidepoint(event.pos):
                    if gv.rainbow_skin_gekauft == False:
                        if gv.coins >= 1000:
                            gv.coins -= 1000
                            gv.rainbow_skin_gekauft = True
                    else:
                        gv.aktueller_skin_standing = "rainbow"
                        gv.aktueller_skin_moving = "rainbow"

        screen.fill("black")

        # Start von KI
        screen.blit(blue_skin.images[0], (500, 50))
        screen.blit(red_skin.images[0], (50, 350))
        screen.blit(green_skin.images[0], (300, 350))
        screen.blit(rainbow_skin.images[0], (550, 350))
        screen.blit(basic_skin.images[0], (250, 50))
        # Ende KI

        if gv.aktueller_skin_standing == "basic":
            basic_text = gv.FONT_MIDDLE.render("Ausgerüstet", True, "green")
        else:
            basic_text = gv.FONT_MIDDLE.render("Ausrüsten", True, "white")

        if gv.blue_skin_gekauft:
            if gv.aktueller_skin_standing == "blue":
                kaufen_text_blue = gv.FONT_MIDDLE.render("Ausgerüstet", True, "green")
            else:
                kaufen_text_blue = gv.FONT_MIDDLE.render("Ausrüsten", True, "white")

        if gv.red_skin_gekauft:
            if gv.aktueller_skin_standing == "red":
                kaufen_text_red = gv.FONT_MIDDLE.render("Ausgerüstet", True, "green")
            else:
                kaufen_text_red = gv.FONT_MIDDLE.render("Ausrüsten", True, "white")

        if gv.green_skin_gekauft:
            if gv.aktueller_skin_standing == "green":
                kaufen_text_green = gv.FONT_MIDDLE.render("Ausgerüstet", True, "green")
            else:
                kaufen_text_green = gv.FONT_MIDDLE.render("Ausrüsten", True, "white")

        if gv.rainbow_skin_gekauft:
            if gv.aktueller_skin_standing == "rainbow":
                kaufen_text_rainbow = gv.FONT_MIDDLE.render("Ausgerüstet", True, "green")
            else:
                kaufen_text_rainbow = gv.FONT_MIDDLE.render("Ausrüsten", True, "white")

        coins.show_coins()

        screen.blit(basic_text, basic_text_rect)
        screen.blit(kaufen_text_blue, kaufen_text_blue_rect)
        screen.blit(kaufen_text_red, kaufen_text_red_rect)
        screen.blit(kaufen_text_green, kaufen_text_green_rect)
        screen.blit(kaufen_text_rainbow, kaufen_text_rainbow_rect)
        screen.blit(back_text, back_text_rect)
        pygame.display.flip()
        clock.tick(gv.FPS)
