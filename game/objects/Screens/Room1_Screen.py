import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.sprites import Bilder
from objects.player import Player
from objects.Uhr import Uhr
from objects.Coins import Coins
from objects.Screens.Object import Object

def room1_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("Room_1 Screen")
    gv.current_screen = "room1"
    frame_counter = 0
    player_x_pos = gv.player_x
    player_y_pos = gv.player_y
    player = Player(
        screen=screen,
        player_x_pos=player_x_pos,
        player_y_pos=player_y_pos
    )
    uhr = Uhr(screen)
    coins = Coins(screen)

    raum = Bilder("../assats/Bilder/Rooms/Raum 1.png", 2,pygame.Rect(0, 0, 1024, 1024),80)
    raum.load_spritesheet()
    orginal_raum = raum.images
    groesse_raum_1 = (gv.SCREEN_WIDTH, gv.SCREEN_HIGHT)
    raum.images = [pygame.transform.smoothscale(img, groesse_raum_1) for img in orginal_raum] # mit KI
    Jonas = Object("../assats/Bilder/Jonas_Bilderrahmen.png", 50, screen, 180, gv.SCREEN_WIDTH/2-37, pygame.Rect(0, 0, 150, 200), 1, 5, 1,gv.Jonas_geklaut, gv.Jonas_auszahlung)
    Jonas.sprite.load_spritesheet()
    orginal_Jonas = Jonas.sprite.images
    groesse_Jonas = (75, 100)
    Jonas.sprite.images = [pygame.transform.smoothscale(img, groesse_Jonas) for img in orginal_Jonas]




    while True:
        frame_counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gv.paused_from = GameScreens.ROOM_1
                    return GameScreens.PAUSED
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.PLAY
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Jonas.rect.collidepoint(event.pos):
                    Jonas.geklaut = True
                    gv.Jonas_geklaut = True
                    gv.Jonas_auszahlung = True

        screen.fill("black")
        raum.draw(screen, 0,0,frame_counter)
        player.update_and_draw(gv.SCREEN_WIDTH, 0,
                               gv.SCREEN_HIGHT-210, gv.SCREEN_HIGHT/2)

        if player.player_x_pos > gv.SCREEN_WIDTH - 60:
            return GameScreens.GANG1

        Jonas.update_and_draw()

        uhr.uhr_update()
        coins.show_coins()
        pygame.display.flip()
        clock.tick(gv.FPS)
