"""
JuXYams — Game Logic
Reuses: combination_engine, player_engine
"""

import random, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.combination_engine import score_yams, available_yams_combos, YAMS_COMBINATIONS
from core.player_engine import make_game, current_player, next_player, log

def new_yams(player_names):
    g = make_game(player_names)
    g["type"] = "yams"
    for p in g["players"]:
        p["scorecard"] = {}   # combo -> score
        p["dice"] = [0,0,0,0,0]
        p["held"] = [False]*5
        p["rolls_left"] = 3
    return g

def roll_dice(game):
    p = current_player(game)
    if p["rolls_left"] <= 0:
        return {"error": "No rolls left"}
    for i in range(5):
        if not p["held"][i]:
            p["dice"][i] = random.randint(1, 6)
    p["rolls_left"] -= 1
    log(game, f"{p['name']} rolled — {p['dice']} ({p['rolls_left']} rolls left)")
    return {"dice": p["dice"], "rolls_left": p["rolls_left"]}

def toggle_hold(game, index):
    p = current_player(game)
    if p["rolls_left"] == 3:
        return {"error": "Roll first"}
    p["held"][index] = not p["held"][index]
    return {"held": p["held"]}

def score_combo(game, combo):
    p = current_player(game)
    if combo in p["scorecard"]:
        return {"error": f"{combo} already used"}
    if combo not in YAMS_COMBINATIONS:
        return {"error": "Unknown combination"}
    points = score_yams(p["dice"], combo)
    p["scorecard"][combo] = points
    p["score"] += points
    log(game, f"{p['name']} scored {combo}: {points} pts")
    # reset for next turn
    p["dice"] = [0,0,0,0,0]
    p["held"] = [False]*5
    p["rolls_left"] = 3
    next_player(game)
    return {"combo": combo, "points": points, "total": p["score"]}

def game_over(game):
    return all(
        len(p["scorecard"]) == len(YAMS_COMBINATIONS)
        for p in game["players"]
    )

def winner(game):
    return max(game["players"], key=lambda p: p["score"])

def yams_state(game):
    p = current_player(game)
    return {
        "current_player": p["name"],
        "dice": p["dice"],
        "held": p["held"],
        "rolls_left": p["rolls_left"],
        "scorecard": p["scorecard"],
        "available": available_yams_combos(p["scorecard"]),
        "players": [{"name": x["name"], "score": x["score"], "scorecard": x["scorecard"]} for x in game["players"]],
        "log": game["log"][-10:],
        "game_over": game_over(game),
        "winner": winner(game)["name"] if game_over(game) else None
    }
