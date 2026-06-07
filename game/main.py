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
from objects.Screens.Mode_Screen import mode_screen
from objects.Screens.riddle2_Screen import riddle2_screen
from objects.Screens.riddle3_Screen import riddle3_screen
from objects.Screens.riddle4_Screen import riddle4_screen
from objects.Screens.riddle5_Screen import riddle5_screen
from objects.save_game import load_game, reset_game


def main():
    gv.init()
    load_game()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HIGHT))
    clock = pygame.time.Clock()

    if gv.current_screen == "play":
        GameScreens.actual = GameScreens.PLAY
    elif gv.current_screen == "room1":
        GameScreens.actual = GameScreens.ROOM_1
    elif gv.current_screen == "riddle1":
        GameScreens.actual = GameScreens.RIDDLE1
    elif gv.current_screen == "riddle2":
        GameScreens.actual = GameScreens.RIDDLE2

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
        elif GameScreens.actual == GameScreens.MODE:
            GameScreens.actual = mode_screen(screen, clock)
        elif GameScreens.actual == GameScreens.RIDDLE1:
            GameScreens.actual = riddle1_screen(screen, clock)
        elif GameScreens.actual == GameScreens.RIDDLE2:
            GameScreens.actual = riddle2_screen(screen, clock)
        elif GameScreens.actual == GameScreens.RIDDLE3:
            GameScreens.actual = riddle3_screen(screen, clock)
        elif GameScreens.actual == GameScreens.RIDDLE4:
            GameScreens.actual = riddle4_screen(screen, clock)
        elif GameScreens.actual == GameScreens.RIDDLE5:
            GameScreens.actual = riddle5_screen(screen, clock)
        elif GameScreens.actual == GameScreens.EXIT:
            break
    reset_game()
    pygame.quit()

if __name__ == "__main__":
    main()
