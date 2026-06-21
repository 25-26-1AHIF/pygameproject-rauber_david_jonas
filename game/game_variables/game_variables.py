import pygame

class GameVariables:
    SCREEN_WIDTH = 800
    SCREEN_HIGHT = 600
    FPS = 60
    player_size = 32
    player_v = 5

    wohnwagen: bool = False
    #spiel_laden: bool = False

    blue_skin_gekauft = False
    red_skin_gekauft = False
    green_skin_gekauft = False
    rainbow_skin_gekauft = False
    aktueller_skin_standing = "basic"
    aktueller_skin_moving = "basic"

    coins = 0
    player_x = SCREEN_HIGHT / 2 - player_size / 2
    player_y = SCREEN_HIGHT - player_size - 10
    background_x = 1
    current_screen = "main"
    paused_from = "play"

    stunden = 0
    sekunden = 0

    FONT_BIG: pygame.font.Font = None
    FONT_MIDDLE: pygame.font.Font = None
    FONT_SMALL: pygame.font.Font = None

    #Test_object_geklaut = False
    #Test_object_auszahlung = False
    Pc_geklaut = False
    Pc_auszahlung = False
    Jonas_geklaut = False
    Jonas_auszahlung = False
    Wein_geklaut = False
    Wein_auszahlung = False
    Baer_geklaut = False
    Baer_auszahlung = False
    Truthahn_geklaut = False
    Truthahn_auszahlung = False
    Fahrrad_geklaut = False
    Fahrrad_auszahlung = False
    Fernseher_geklaut = False
    Fernseher_auszahlung = False

    @staticmethod
    def init():
        pygame.init()
        GameVariables.FONT_BIG = pygame.sysfont.SysFont("arial", 48, bold=True)
        GameVariables.FONT_MIDDLE = pygame.sysfont.SysFont("arial", 30, bold=True)
        GameVariables.FONT_SMALL = pygame.sysfont.SysFont("arial", 14, bold=True)


class GameScreens:

    MAIN = ("main")
    PLAY = ("play")
    ANIMATION = ("animation")
    PAUSED = ("paused")
    STR = ("str")
    EXIT = ("exit")
    MODE = ("mode")
    RIDDLE3 = ("riddle3")
    RIDDLE4 = ("riddle4")
    RIDDLE5 = ("riddle5")
    ROOM_1 = ("room1")
    ROOM_2 = ("room2")
    ROOM_3 = ("room3")
    ROOM_4 = ("room4")
    RIDDLE1 = ("riddle1")
    RIDDLE2 = ("riddle2")
    GANG1 = ("Gang_1")
    GANG2 = ("Gang_2")
    GANG3 = ("Gang_3")
    WAGEN = ("WAGEN")
    SHOP = ("shop")
    ROOM_1_2 = ("room1_2")
    ROOM_2_2 = ("room2_2")
    ROOM_3_2 = ("room3_2")
    ROOM_4_2 = ("room4_2")
    ROOM_1_3 = ("room1_3")
    ROOM_2_3 = ("room2_3")
    ROOM_3_3 = ("room3_3")
    ROOM_4_3 = ("room4_3")
    SCORES = ("scores")
    actual = MAIN