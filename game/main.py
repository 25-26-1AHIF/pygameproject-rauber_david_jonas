import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.Screens.Main_Screen import main_screen
from objects.Screens.Play_Screen import play_screen
from objects.Screens.Paused_Screen import paused_screen
from objects.Screens.Steuerung_Screen import steuerung_screen
from objects.Screens.Animation_Screen import animation_screen
from objects.Screens.Room1_Screen import room1_screen
from objects.Screens.riddle1_Screen import riddle1_screen

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
        elif GameScreens.actual == GameScreens.PAUSED:
            GameScreens.actual = paused_screen(screen, clock)
        elif GameScreens.actual == GameScreens.STR:
            GameScreens.actual = steuerung_screen(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_1:
            GameScreens.actual = room1_screen(screen, clock)
        elif GameScreens.actual == GameScreens.RIDDLE1:
            GameScreens.actual = riddle1_screen(screen, clock)
        elif GameScreens.actual == GameScreens.EXIT:
            break


    pygame.quit()

if __name__ == "__main__":
    main()
