import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player

def main_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Main Screen")
    frame_counter = 0

    titel_text = gv.FONT_BIG.render("Räuber", True, "white")
    starten_text = gv.FONT_MIDDLE.render("Starten", True, "white")
    titel_text_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 100))
    starten_text_rect = starten_text.get_rect(center=(gv.SCREEN_WIDTH / 2, gv.SCREEN_HIGHT / 2))

    Geldsack = Bilder("game/Bilder/Geldsack.png", 1, pygame.Rect(0, 0, 128, 128), 1)
    Hintergrund = Bilder("game/Bilder/Hintergrund.png", 16, pygame.Rect(0, 0, 1024, 1024), 10)
    Geldsack.load_spritesheet()
    Hintergrund.load_spritesheet()

    groesse = (400, 400)
    groesse_hintergrund = (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)

    Geldsack.images[0] = pygame.transform.smoothscale(Geldsack.images[0], groesse)
    original_hintergrund = Hintergrund.images[:]
    Hintergrund.images = [pygame.transform.smoothscale(img, groesse_hintergrund) for img in original_hintergrund]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return GameScreens.EXIT
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if starten_text_rect.collidepoint(event.pos):
                    return GameScreens.ANIMATION

        Hintergrund.draw(screen, 0, 0, frame_counter)
        screen.blit(titel_text, titel_text_rect)
        Geldsack.draw(screen, gv.SCREEN_WIDTH / 2 - groesse[0] / 2, gv.SCREEN_HIGHT / 2 - groesse[1] / 2 + 10, frame_counter)
        screen.blit(starten_text, starten_text_rect)

        frame_counter += 1
        pygame.display.flip()
        clock.tick(gv.FPS)


def play_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Play Screen")
    player_x_pos = gv.SCREEN_WIDTH / 2 - gv.player_size / 2
    player_y_pos = gv.SCREEN_HIGHT - gv.player_size - 10
    player = Player(
        screen=screen,
        player_x_pos=player_x_pos,
        player_y_pos=player_y_pos
    )

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
        player.update_and_draw()
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
                    return GameScreens.MAIN
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



def animation_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Animation")
    frame_counter = 0

    Geldsack = Bilder("game/Bilder/Geldsack.png", 1, pygame.Rect(0, 0, 128, 128), 1)
    Hintergrund = Bilder("game/Bilder/Hintergrund.png", 16, pygame.Rect(0, 0, 1024, 1024), 2)
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

def main():
    gv.init()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HIGHT))
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