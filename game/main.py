import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.Screens.Main_Screen import main_screen
from objects.Screens.Play_Screen import play_screen
from objects.Screens.Paused_Screen import paused_screen
from objects.Screens.Steuerung_Screen import steuerung_screen
from objects.Screens.Animation_Screen import animation_screen
from objects.Screens.Finish_Screen import finish_screen
from objects.Screens.Room1_Screen import room1_screen
from objects.Screens.Room2_Screen import room2_screen
from objects.Screens.Room3_Screen import room3_screen
from objects.Screens.Room4_Screen import room4_screen
from objects.Screens.riddle1_Screen import riddle1_screen
from objects.Screens.riddle2_Screen import riddle2_screen
from objects.Screens.riddle3_Screen import riddle3_screen
from objects.Screens.riddle4_Screen import riddle4_screen
from objects.Screens.riddle5_Screen import riddle5_screen
from objects.Screens.Mode_Screen import mode_screen
from objects.Screens.Gang_1 import Gang_1
from objects.Screens.Gang_2 import Gang_2
from objects.Screens.Gang_3 import Gang_3
from objects.save_game import load_game, reset_game
from objects.Screens.Wohnwagen import Wohnwagen
from objects.Screens.shop_Screen import shop_screen
from objects.Screens.room_1_2 import room1_2
from objects.Screens.room_2_2 import room2_2
from objects.Screens.room_3_2 import room3_2
from objects.Screens.room_4_2 import room4_2
from objects.Screens.room_1_3 import room1_3
from objects.Screens.room_2_3 import room2_3
from objects.Screens.room_3_3 import room3_3
from objects.Screens.room_4_3 import room4_3
from objects.Screens.scores_Screen import scores_screen


def main():
    gv.init()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HIGHT))
    clock = pygame.time.Clock()
    GameScreens.actual = GameScreens.MAIN

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
        elif GameScreens.actual == GameScreens.ROOM_2:
            GameScreens.actual = room2_screen(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_3:
            GameScreens.actual = room3_screen(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_4:
            GameScreens.actual = room4_screen(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_1_2:
            GameScreens.actual = room1_2(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_2_2:
            GameScreens.actual = room2_2(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_3_2:
            GameScreens.actual = room3_2(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_4_2:
            GameScreens.actual = room4_2(screen, clock)
        elif GameScreens.actual == GameScreens.MODE:
            GameScreens.actual = mode_screen(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_1_3:
            GameScreens.actual = room1_3(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_2_3:
            GameScreens.actual = room2_3(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_3_3:
            GameScreens.actual = room3_3(screen, clock)
        elif GameScreens.actual == GameScreens.ROOM_4_3:
            GameScreens.actual = room4_3(screen, clock)
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
        elif GameScreens.actual == GameScreens.GANG1:
            GameScreens.actual = Gang_1(screen, clock)
        elif GameScreens.actual == GameScreens.GANG2:
            GameScreens.actual = Gang_2(screen, clock)
        elif GameScreens.actual == GameScreens.GANG3:
            GameScreens.actual = Gang_3(screen, clock)
        elif GameScreens.actual == GameScreens.WAGEN:
            GameScreens.actual = Wohnwagen(screen, clock)
        elif GameScreens.actual == GameScreens.SHOP:
            GameScreens.actual = shop_screen(screen, clock)
        elif GameScreens.actual == GameScreens.SCORES:
            GameScreens.actual = scores_screen(screen, clock)
        elif GameScreens.actual == GameScreens.FINISH:
            GameScreens.actual = finish_screen(screen, clock)
        elif GameScreens.actual == GameScreens.EXIT:
            break
    pygame.quit()

if __name__ == "__main__":
    main()
