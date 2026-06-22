import pygame
import random
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens

def riddle1_screen(screen, clock):
    pygame.display.set_caption("Simon Says")
    gv.current_screen = "riddle1"

    RED = (255, 0, 0)
    DARK_RED = (120, 0, 0)

    BLUE = (0, 0, 255)
    DARK_BLUE = (0, 0, 120)

    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 120, 0)

    YELLOW = (255, 255, 0)
    DARK_YELLOW = (120, 120, 0)

    red_rect = pygame.Rect(100, 250, 100, 100)
    blue_rect = pygame.Rect(250, 250, 100, 100)
    green_rect = pygame.Rect(400, 250, 100, 100)
    yellow_rect = pygame.Rect(550, 250, 100, 100)

    colors = ["red", "blue", "green", "yellow"]

    showing_colors = []

    for i in range(3):
        showing_colors.append(random.choice(colors))

    while True:
        player_input = []
        for color in showing_colors:
            screen.fill("black")
            text = gv.FONT_MIDDLE.render(
                "Merke dir die Reihenfolge und wiederhole sie",
                True,
                "white"
            )
            screen.blit(text, (100, 100))

            pygame.draw.rect(screen, DARK_RED, red_rect)
            pygame.draw.rect(screen, DARK_BLUE, blue_rect)
            pygame.draw.rect(screen, DARK_GREEN, green_rect)
            pygame.draw.rect(screen, DARK_YELLOW, yellow_rect)

            if color == "red":
                pygame.draw.rect(screen, RED, red_rect)

            if color == "blue":
                pygame.draw.rect(screen, BLUE, blue_rect)

            if color == "green":
                pygame.draw.rect(screen, GREEN, green_rect)

            if color == "yellow":
                pygame.draw.rect(screen, YELLOW, yellow_rect)

            pygame.display.flip()
            pygame.time.delay(700) # Hilfe KI Gemini Prompt: Wie kann ich eine Pause in Pygame machen

            pygame.draw.rect(screen, DARK_RED, red_rect)
            pygame.draw.rect(screen, DARK_BLUE, blue_rect)
            pygame.draw.rect(screen, DARK_GREEN, green_rect)
            pygame.draw.rect(screen, DARK_YELLOW, yellow_rect)

            pygame.display.flip()
            pygame.time.delay(300)

        while True:
            pygame.draw.rect(screen, DARK_RED, red_rect)
            pygame.draw.rect(screen, DARK_BLUE, blue_rect)
            pygame.draw.rect(screen, DARK_GREEN, green_rect)
            pygame.draw.rect(screen, DARK_YELLOW, yellow_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameScreens.EXIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return GameScreens.PLAY
                    if event.key == pygame.K_SPACE:
                        gv.paused_from = GameScreens.RIDDLE1
                        return GameScreens.PAUSED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if red_rect.collidepoint(event.pos):
                        player_input.append("red")
                        pygame.draw.rect(screen, RED, red_rect)
                        pygame.display.flip()
                        pygame.time.delay(300)
                        pygame.draw.rect(screen, DARK_RED, red_rect)

                    if blue_rect.collidepoint(event.pos):
                        player_input.append("blue")
                        pygame.draw.rect(screen, BLUE, blue_rect)
                        pygame.display.flip()
                        pygame.time.delay(300)
                        pygame.draw.rect(screen, BLUE, blue_rect)

                    if green_rect.collidepoint(event.pos):
                        player_input.append("green")
                        pygame.draw.rect(screen, GREEN, green_rect)
                        pygame.display.flip()
                        pygame.time.delay(300)
                        pygame.draw.rect(screen, DARK_GREEN, green_rect)

                    if yellow_rect.collidepoint(event.pos):
                        player_input.append("yellow")
                        pygame.draw.rect(screen, YELLOW, yellow_rect)
                        pygame.display.flip()
                        pygame.time.delay(300)
                        pygame.draw.rect(screen, DARK_YELLOW, yellow_rect)

                    index = len(player_input) - 1 # das -1 mit KI Hilfe

                    if player_input[index] != showing_colors[index]:
                        break
                    if player_input == showing_colors:
                        if gv.wohnwagen == True:
                            gv.wohnwagen = False
                            return GameScreens.WAGEN
                        elif gv.haus_2 == True:
                            gv.haus_2 = False
                            return GameScreens.GANG2
                        elif gv.haus_3 == True:
                            gv.haus_3 = False
                            return GameScreens.GANG3
                        elif gv.haus_4 == True:
                            gv.haus_4 = False
                            return GameScreens.GANG4
                        else:
                            return GameScreens.GANG1
            else:
                pygame.display.flip()
                clock.tick(gv.FPS)
                continue

            break
