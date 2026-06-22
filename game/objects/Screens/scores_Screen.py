import pygame
from game_variables.game_variables import GameVariables as gv
from game_variables.game_variables import GameScreens as GameScreens
from objects.save_game import load_entire_file

def scores_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.display.set_caption("Highscores")
    haupt_daten = load_entire_file()
    scores_liste = haupt_daten["scores"]

    titel_text = gv.FONT_BIG.render("TOP 3 BESTZEITEN", True, "white")
    titel_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 80))
    zurueck_text = gv.FONT_MIDDLE.render("Zurück", True, "gray")
    zurueck_rect = zurueck_text.get_rect(center=(gv.SCREEN_WIDTH / 2, gv.SCREEN_HIGHT - 80))

    platz1_str = "1. Platz: -  (0 Coins)"
    platz2_str = "2. Platz: -  (0 Coins)"
    platz3_str = "3. Platz: -  (0 Coins)"

    if len(scores_liste) >= 1:
        ges_sek = scores_liste[0]["zeit"]
        m_coins = scores_liste[0]["coins"]
        minuten = ges_sek // 60 # Berechnung mit KI ChatGPT Prompt: Berechne die Zeit korrekt
        sekunden = ges_sek % 60 # Berechnung mit KI ChatGPT
        platz1_str = f"1. Platz: {minuten:02d}:{sekunden:02d}  ({m_coins} Coins)"
    if len(scores_liste) >= 2:
        ges_sek = scores_liste[1]["zeit"]
        m_coins = scores_liste[1]["coins"]
        minuten = ges_sek // 60
        sekunden = ges_sek % 60
        platz2_str = f"2. Platz: {minuten:02d}:{sekunden:02d}  ({m_coins} Coins)"
    if len(scores_liste) >= 3:
        ges_sek = scores_liste[2]["zeit"]
        m_coins = scores_liste[2]["coins"]
        minuten = ges_sek // 60
        sekunden = ges_sek % 60
        platz3_str = f"3. Platz: {minuten:02d}:{sekunden:02d}  ({m_coins} Coins)"

    p1_text = gv.FONT_MIDDLE.render(platz1_str, True, "yellow")
    p2_text = gv.FONT_MIDDLE.render(platz2_str, True, "white")
    p3_text = gv.FONT_MIDDLE.render(platz3_str, True, "white")
    p1_rect = p1_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 220))
    p2_rect = p2_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 300))
    p3_rect = p3_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 380))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameScreens.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameScreens.MAIN
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if zurueck_rect.collidepoint(event.pos):
                    return GameScreens.MAIN

        screen.fill("blue")

        screen.blit(titel_text, titel_rect)
        screen.blit(p1_text, p1_rect)
        screen.blit(p2_text, p2_rect)
        screen.blit(p3_text, p3_rect)
        screen.blit(zurueck_text, zurueck_rect)
        pygame.display.flip()
        clock.tick(gv.FPS)
