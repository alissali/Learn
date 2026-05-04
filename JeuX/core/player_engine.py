"""
JeuX — Core: Player Engine
Shared by all JeuX games.
"""

def make_player(name, chips=1000):
    return {"name": name, "chips": chips, "score": 0, "active": True}

def make_game(player_names, chips=1000):
    return {
        "players": [make_player(n, chips) for n in player_names],
        "current": 0,
        "round": 1,
        "log": []
    }

def current_player(game):
    return game["players"][game["current"]]

def next_player(game):
    n = len(game["players"])
    game["current"] = (game["current"] + 1) % n
    game["round"] += 1

def log(game, msg):
    game["log"].append(msg)
    if len(game["log"]) > 50:
        game["log"] = game["log"][-50:]
