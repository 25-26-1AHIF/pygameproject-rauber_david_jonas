import json
from game_variables.game_variables import GameVariables as gv

def save_game():
    altes_dict = load_entire_file()
    aktuelle_scores = altes_dict["scores"]

    spielstand = {
        "coins": gv.coins,
        "player_x": gv.player_x,
        "player_y": gv.player_y,
        "screen": gv.current_screen,
        "background_x": gv.background_x,
        "stunden": gv.stunden,
        "sekunden": gv.sekunden,
        "skin_standing": gv.aktueller_skin_standing,
        "skin_moving": gv.aktueller_skin_moving
    }

    haupt_daten = {
        "spielstand": spielstand,
        "scores": aktuelle_scores
    }

    with open("../savegame.json", "w") as datei:
        json.dump(haupt_daten, datei, indent=4)

def load_game():
    try:
        haupt_daten = load_entire_file()
        spielstand = haupt_daten["spielstand"]

        gv.coins = spielstand["coins"]
        gv.player_x = spielstand["player_x"]
        gv.player_y = spielstand["player_y"]
        gv.current_screen = spielstand["screen"]
        gv.background_x = spielstand["background_x"]
        gv.stunden = spielstand["stunden"]
        gv.sekunden = spielstand["sekunden"]
        gv.aktueller_skin_standing = spielstand["skin_standing"]
        gv.aktueller_skin_moving = spielstand["skin_moving"]
    except:
        pass


def check_and_save_score():
    haupt_daten = load_entire_file()
    scores = haupt_daten["scores"]

    meine_zeit = (gv.stunden * 3600) + gv.sekunden

    if meine_zeit == 0:
        return

    lauf_daten = {
        "zeit": meine_zeit,
        "coins": gv.coins
    }

    scores.append(lauf_daten)

    for i in range(len(scores)):
        for j in range(i + 1, len(scores)):
            if scores[i]["zeit"] > scores[j]["zeit"]:
                temporaer = scores[i]
                scores[i] = scores[j]
                scores[j] = temporaer

    if len(scores) > 3:
        scores = scores[0:3]

    haupt_daten["scores"] = scores
    with open("../savegame.json", "w") as datei:
        json.dump(haupt_daten, datei, indent=4)

def reset_game():
    check_and_save_score()

    gv.coins = 0
    gv.stunden = 0
    gv.sekunden = 0
    gv.player_x = gv.SCREEN_WIDTH / 2
    gv.player_y = gv.SCREEN_HIGHT - 100
    gv.background_x = 1
    gv.current_screen = "play"
    save_game()

def load_entire_file():
        try:
            with open("../savegame.json", "r") as datei:
                return json.load(datei)
        except:
            return {"spielstand": {}, "scores": []}
