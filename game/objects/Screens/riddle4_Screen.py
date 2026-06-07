import pygame
import random
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens

def riddle4_screen(screen, clock):
    pygame.display.set_caption("Riddle 4")
    gv.current_screen = "riddle4"

    buttons = []
    for i in range(6):
        buttons.append(pygame.Rect(100 + i * 100, 250, 60, 60)) # Ki hilfe

    richtiger = random.randint(0, 5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    if buttons[i].collidepoint(event.pos):
                        if i == richtiger:
                            return GameScreens.ROOM_1

        screen.fill("black")
        text = gv.FONT_MIDDLE.render("Finde den richtigen Knopf",True,
                                     "white")
        text_rect = text.get_rect(center=(220, 100))
        screen.blit(text, text_rect)
        for button in buttons:
            pygame.draw.rect(screen, "red", button)
        pygame.display.flip()
        clock.tick(gv.FPS)