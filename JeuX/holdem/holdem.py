"""
JeuX — Texas Hold'em Poker
Reuses: combination_engine (evaluate_poker_hand, compare_hands), player_engine
Extension: community cards, betting rounds
"""

import random, sys, os
from itertools import combinations as combos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.combination_engine import evaluate_poker_hand, compare_hands
from core.player_engine import make_game, log

SUITS = ['S', 'H', 'D', 'C']
VALUES = list(range(2, 15))
SUIT_SYMBOLS = {'S': '♠', 'H': '♥', 'D': '♦', 'C': '♣'}
VALUE_NAMES = {11:'J', 12:'Q', 13:'K', 14:'A'}

def card_name(card):
    v, s = card
    return f"{VALUE_NAMES.get(v,str(v))}{SUIT_SYMBOLS[s]}"

def make_deck():
    deck = [(v, s) for s in SUITS for v in VALUES]
    random.shuffle(deck)
    return deck

def best_5_from_7(cards):
    """Find best 5-card hand from 7 cards (2 hole + 5 community)."""
    best = None
    for five in combos(cards, 5):
        h = evaluate_poker_hand(list(five))
        if best is None or compare_hands(h, best) > 0:
            best = h
    return best

def new_holdem(player_names, small_blind=10, big_blind=20):
    g = make_game(player_names, chips=1000)
    g["type"] = "holdem"
    g["deck"] = make_deck()
    g["community"] = []
    g["pot"] = 0
    g["small_blind"] = small_blind
    g["big_blind"] = big_blind
    g["phase"] = "preflop"  # preflop -> flop -> turn -> river -> showdown
    g["dealer"] = 0
    for p in g["players"]:
        p["hole"] = []
        p["folded"] = False
        p["bet"] = 0
        p["all_in"] = False
    return g

def deal_holdem(game):
    """Deal hole cards + collect blinds."""
    n = len(game["players"])
    sb_idx = (game["dealer"] + 1) % n
    bb_idx = (game["dealer"] + 2) % n
    # Blinds
    game["players"][sb_idx]["chips"] -= game["small_blind"]
    game["players"][sb_idx]["bet"] = game["small_blind"]
    game["pot"] += game["small_blind"]
    game["players"][bb_idx]["chips"] -= game["big_blind"]
    game["players"][bb_idx]["bet"] = game["big_blind"]
    game["pot"] += game["big_blind"]
    # Deal 2 hole cards each
    for p in game["players"]:
        p["hole"] = [game["deck"].pop(), game["deck"].pop()]
        p["folded"] = False
    game["phase"] = "preflop"
    log(game, f"Dealt. SB={game['players'][sb_idx]['name']} BB={game['players'][bb_idx]['name']} Pot={game['pot']}")
    return {"phase": "preflop"}

def deal_flop(game):
    game["deck"].pop()  # burn
    game["community"] = [game["deck"].pop() for _ in range(3)]
    game["phase"] = "flop"
    log(game, f"FLOP: {[card_name(c) for c in game['community']]}")
    return {"community": [card_name(c) for c in game["community"]], "phase": "flop"}

def deal_turn(game):
    game["deck"].pop()
    game["community"].append(game["deck"].pop())
    game["phase"] = "turn"
    log(game, f"TURN: {card_name(game['community'][-1])}")
    return {"community": [card_name(c) for c in game["community"]], "phase": "turn"}

def deal_river(game):
    game["deck"].pop()
    game["community"].append(game["deck"].pop())
    game["phase"] = "river"
    log(game, f"RIVER: {card_name(game['community'][-1])}")
    return {"community": [card_name(c) for c in game["community"]], "phase": "river"}

def bet(game, player_idx, amount):
    p = game["players"][player_idx]
    amount = min(amount, p["chips"])
    p["chips"] -= amount
    p["bet"] += amount
    game["pot"] += amount
    log(game, f"{p['name']} bets {amount}. Pot={game['pot']}")
    return {"pot": game["pot"], "chips": p["chips"]}

def fold(game, player_idx):
    game["players"][player_idx]["folded"] = True
    log(game, f"{game['players'][player_idx]['name']} folds")
    return {"folded": True}

def holdem_showdown(game):
    results = []
    best_player = None
    best_hand = None
    for p in game["players"]:
        if p["folded"]:
            results.append({"name": p["name"], "folded": True})
            continue
        all_cards = p["hole"] + game["community"]
        hand_eval = best_5_from_7(all_cards)
        results.append({
            "name": p["name"],
            "hole": [card_name(c) for c in p["hole"]],
            "hand_name": hand_eval[0]
        })
        if best_hand is None or compare_hands(hand_eval, best_hand) > 0:
            best_hand = hand_eval
            best_player = p
    best_player["chips"] += game["pot"]
    log(game, f"{best_player['name']} wins {game['pot']} with {best_hand[0]}!")
    game["phase"] = "done"
    return {"results": results, "winner": best_player["name"], "hand": best_hand[0], "pot": game["pot"]}

def holdem_state(game, viewer_idx=0):
    p = game["players"][viewer_idx]
    return {
        "phase": game["phase"],
        "pot": game["pot"],
        "community": [card_name(c) for c in game["community"]],
        "your_hole": [card_name(c) for c in p["hole"]],
        "players": [{"name": x["name"], "chips": x["chips"], "folded": x["folded"], "bet": x["bet"]} for x in game["players"]],
        "log": game["log"][-10:]
    }
