import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens

def riddle4_screen(screen, clock):
    pygame.display.set_caption("Riddle 4")
    gv.current_screen = "riddle4"

    player_xpos = 50
    player_ypos = 50

    ziel_rect = pygame.Rect(gv.SCREEN_WIDTH / 2 + 300, gv.SCREEN_HIGHT - 100, 50, 50)

    walls = [
        pygame.Rect(150, 0, 20, 400),
        pygame.Rect(300, 200, 20, 400),
        pygame.Rect(450, 0, 20, 400),
        pygame.Rect(600, 200, 20, 400)
    ] # Mit Hilfe von KI berechnet

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            if player_ypos <= 0:
                player_ypos = 0
            else:
                player_ypos -= 5
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            if player_ypos >= gv.SCREEN_HIGHT - gv.player_size:
                player_ypos = gv.SCREEN_HIGHT - gv.player_size
            else:
                player_ypos += 5
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if player_xpos <= 0:
                player_xpos = 0
            else:
                player_xpos -= 5
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if player_xpos >= gv.SCREEN_WIDTH - gv.player_size:
                player_xpos = gv.SCREEN_WIDTH - gv.player_size
            else:
                player_xpos += 5

        player_rect = pygame.Rect(player_xpos, player_ypos, 32, 32)

        for wall in walls:
            if player_rect.colliderect(wall):
                player_xpos = 50
                player_ypos = 50

        if player_rect.colliderect(ziel_rect):
            if gv.wohnwagen == True:
                gv.wohnwagen = False
                return GameScreens.WAGEN
            elif gv.haus_2 == True:
                gv.haus_2 = False
                return GameScreens.GANG2
            else:
                return GameScreens.GANG1

        screen.fill("black")
        pygame.draw.rect(screen, "green", ziel_rect)
        pygame.draw.rect(screen, "white", player_rect)

        for wall in walls:
            pygame.draw.rect(screen, "red", rect=(wall))
        text = gv.FONT_MIDDLE.render("Erreiche das grüne Feld",True,
                                     "white")
        text_rect = text.get_rect(
            center=(gv.SCREEN_WIDTH // 2, 50))
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(gv.FPS)