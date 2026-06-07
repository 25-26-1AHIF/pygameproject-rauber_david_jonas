import json
from game_variables.game_variables import GameVariables as gv

def save_game():

    daten = {
    "coins": gv.coins,
    "player_x": gv.player_x,
    "player_y": gv.player_y,
    "screen": gv.current_screen,
    "stunden": gv.stunden,
    "sekunden": gv.sekunden,
    "background_x": gv.background_x
}

    with open("savegame.json", "w") as datei:
        json.dump(daten, datei)

def reset_game():
    daten = {
        "coins": 0,
        "player_x": 384,
        "player_y": 558,
        "screen": "main",
        "stunden": 0,
        "sekunden": 0
    }

    with open("savegame.json", "w") as datei:
        json.dump(daten, datei)

def load_game():
    try:

        with open("savegame.json", "r") as datei:
            daten = json.load(datei)

        gv.coins = daten["coins"]
        gv.player_x = daten["player_x"]
        gv.player_y = daten["player_y"]
        gv.current_screen = daten["screen"]
        gv.background_x = daten["background_x"]

        gv.stunden = daten["stunden"]
        gv.sekunden = daten["sekunden"]

    except:
        pass