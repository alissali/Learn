"""
JeuX — 5-Card Draw Poker
Reuses: combination_engine (evaluate_poker_hand, compare_hands), player_engine
"""

import random, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.combination_engine import evaluate_poker_hand, compare_hands
from core.player_engine import make_game, current_player, log

SUITS = ['S', 'H', 'D', 'C']
VALUES = list(range(2, 15))  # 2-14, 14=Ace
SUIT_SYMBOLS = {'S': '♠', 'H': '♥', 'D': '♦', 'C': '♣'}
VALUE_NAMES = {11:'J', 12:'Q', 13:'K', 14:'A'}

def card_name(card):
    v, s = card
    vn = VALUE_NAMES.get(v, str(v))
    return f"{vn}{SUIT_SYMBOLS[s]}"

def make_deck():
    deck = [(v, s) for s in SUITS for v in VALUES]
    random.shuffle(deck)
    return deck

def new_draw_poker(player_names, ante=10):
    g = make_game(player_names, chips=500)
    g["type"] = "draw_poker"
    g["deck"] = make_deck()
    g["pot"] = 0
    g["ante"] = ante
    g["phase"] = "ante"   # ante -> deal -> draw -> showdown
    for p in g["players"]:
        p["hand"] = []
        p["held"] = [False]*5
        p["folded"] = False
        p["bet"] = 0
    return g

def deal(game):
    if game["phase"] != "ante":
        return {"error": "Wrong phase"}
    # collect ante
    for p in game["players"]:
        p["chips"] -= game["ante"]
        p["bet"] = game["ante"]
        game["pot"] += game["ante"]
    # deal 5 cards each
    for p in game["players"]:
        p["hand"] = [game["deck"].pop() for _ in range(5)]
        p["held"] = [False]*5
        p["folded"] = False
        p["drew"] = False
    game["phase"] = "draw"
    log(game, f"Dealt. Pot: {game['pot']}")
    return {"phase": "draw"}

def toggle_hold_poker(game, player_idx, card_idx):
    p = game["players"][player_idx]
    p["held"][card_idx] = not p["held"][card_idx]
    return {"held": p["held"]}

def draw(game, player_idx):
    if game["phase"] != "draw":
        return {"error": "Wrong phase"}
    p = game["players"][player_idx]
    if p.get("drew"):
        return {"error": "Already drew"}
    for i in range(5):
        if not p["held"][i]:
            if game["deck"]:
                p["hand"][i] = game["deck"].pop()
    p["drew"] = True
    log(game, f"{p['name']} drew new cards")
    # Move to showdown only when all players have drawn
    if all(pl.get("drew") for pl in game["players"]):
        game["phase"] = "showdown"
    return {"hand": [card_name(c) for c in p["hand"]], "phase": game["phase"]}

def showdown(game):
    if game["phase"] != "showdown":
        return {"error": "Wrong phase"}
    results = []
    best_player = None
    best_hand = None
    for p in game["players"]:
        if p["folded"]:
            continue
        hand_eval = evaluate_poker_hand(p["hand"])
        results.append({"name": p["name"], "hand_name": hand_eval[0], "cards": [card_name(c) for c in p["hand"]]})
        if best_hand is None or compare_hands(hand_eval, best_hand) > 0:
            best_hand = hand_eval
            best_player = p
    # Award pot
    best_player["chips"] += game["pot"]
    log(game, f"{best_player['name']} wins pot of {game['pot']} with {best_hand[0]}!")
    game["phase"] = "done"
    return {
        "results": results,
        "winner": best_player["name"],
        "hand": best_hand[0],
        "pot": game["pot"]
    }

def draw_poker_state(game, viewer_idx=0):
    p = game["players"][viewer_idx]
    return {
        "phase": game["phase"],
        "pot": game["pot"],
        "your_hand": [card_name(c) for c in p["hand"]],
        "held": p["held"],
        "players": [{"name": x["name"], "chips": x["chips"], "folded": x["folded"]} for x in game["players"]],
        "log": game["log"][-10:]
    }
