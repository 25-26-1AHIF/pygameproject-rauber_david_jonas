import pygame





class GameVariables:
    SCREEN_WIDTH = 800
    SCREEN_HIGHT = 600
    FPS = 60

    FONT_BIG: pygame.font.Font = None
    FONT_MIDDLE: pygame.font.Font = None
    FONT_SMALL: pygame.font.Font = None

    @staticmethod
    def init():
        pygame.init()
        GameVariables.FONT_BIG = pygame.sysfont.SysFont("arial", 48, bold=True)
        GameVariables.FONT_MIDDLE = pygame.sysfont.SysFont("arial", 30, bold=True)
        GameVariables.FONT_SMALL = pygame.sysfont.SysFont("arial", 14, bold=True)


class GameScreens:

    MAIN = ("main")
    PLAY = ("play")
    EXIT = ("exit")
    actual = MAIN