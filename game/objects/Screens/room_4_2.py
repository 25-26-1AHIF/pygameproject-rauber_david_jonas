import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Uhr import Uhr
from objects.Coins import Coins
from objects.Screens.Object import Object

def room4_2(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Room_1 Screen")
    gv.current_screen = "room4"
    uhr = Uhr(screen)
    coins = Coins(screen)
    frame_counter = 0
    player_x_pos = gv.SCREEN_WIDTH / 2 - gv.player_size / 2
    player_y_pos = gv.SCREEN_HIGHT - gv.player_size - 110
    player = Player(
        screen=screen,
        player_x_pos=player_x_pos,
        player_y_pos=player_y_pos
    )


    raum = Bilder("../assats/Bilder/Rooms/Haus_2.png", 1,pygame.Rect(5120, 0, 1024, 1024),80)
    raum.load_spritesheet()
    orginal_raum = raum.images
    groesse_raum_1 = (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)
    raum.images = [pygame.transform.smoothscale(img, groesse_raum_1) for img in orginal_raum] # mit KI
    Wein = Object("../assats/Bilder/Weinflasche.png", 200, screen, 300, 260, pygame.Rect(0, 0, 150, 200), 1, 5, 1,gv.Wein_geklaut, gv.Wein_auszahlung)
    Wein.sprite.load_spritesheet()
    orginal_Wein = Wein.sprite.images
    groesse_Wein = (75, 100)
    Wein.sprite.images = [pygame.transform.smoothscale(img, groesse_Wein) for img in orginal_Wein]



    while True:
        frame_counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gv.paused_from = GameScreens.ROOM_4
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Wein.rect.collidepoint(event.pos):
                    Wein.geklaut = True
                    gv.Wein_geklaut = True
                    gv.Wein_auszahlung = True

        screen.fill("black")
        raum.draw(screen, 0,0,frame_counter)
        player.update_and_draw(gv.SCREEN_WIDTH, 0,
                               gv.SCREEN_HIGHT-110, gv.SCREEN_HIGHT/2 + 90)
        if player.player_x_pos < 60:
            return GameScreens.GANG2
        Wein.update_and_draw()
        uhr.uhr_update()
        coins.show_coins()
        pygame.display.flip()
        clock.tick(gv.FPS)
