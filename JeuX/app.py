"""
JeuX — Game Platform
Flask app: JuXYams + 5-Card Draw + Texas Hold'em
Port: 5002
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, jsonify, request, render_template, session
from juxyams.yams import new_yams, roll_dice, toggle_hold, score_combo, yams_state, game_over, winner
from poker_draw.poker_draw import new_draw_poker, deal, toggle_hold_poker, draw, showdown, draw_poker_state
from holdem.holdem import new_holdem, deal_holdem, deal_flop, deal_turn, deal_river, bet, fold, holdem_showdown, holdem_state

app = Flask(__name__)
app.secret_key = "jeux-jux-2026"

# ─── SHARED STATE ─────────────────────────────────────────────────────────────
_games = {}

def get_game(key):
    return _games.get(key)

def set_game(key, g):
    _games[key] = g

# ─── MAIN PAGE ────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("jeux.html")

# ─── YAMS ROUTES ──────────────────────────────────────────────────────────────

@app.route("/yams/new", methods=["POST"])
def yams_new():
    data = request.json
    players = data.get("players", ["Player 1", "Player 2"])
    g = new_yams(players)
    set_game("yams", g)
    return jsonify(yams_state(g))

@app.route("/yams/roll", methods=["POST"])
def yams_roll():
    g = get_game("yams")
    if not g: return jsonify({"error": "No game"})
    return jsonify(roll_dice(g))

@app.route("/yams/hold", methods=["POST"])
def yams_hold():
    g = get_game("yams")
    if not g: return jsonify({"error": "No game"})
    idx = request.json.get("index")
    return jsonify(toggle_hold(g, idx))

@app.route("/yams/score", methods=["POST"])
def yams_score():
    g = get_game("yams")
    if not g: return jsonify({"error": "No game"})
    combo = request.json.get("combo")
    result = score_combo(g, combo)
    result["state"] = yams_state(g)
    return jsonify(result)

@app.route("/yams/state")
def yams_state_route():
    g = get_game("yams")
    if not g: return jsonify({"error": "No game"})
    return jsonify(yams_state(g))

# ─── 5-CARD DRAW ROUTES ───────────────────────────────────────────────────────

@app.route("/draw/new", methods=["POST"])
def draw_new():
    data = request.json
    players = data.get("players", ["Player 1", "Player 2"])
    g = new_draw_poker(players)
    set_game("draw", g)
    return jsonify(draw_poker_state(g))

@app.route("/draw/deal", methods=["POST"])
def draw_deal():
    g = get_game("draw")
    if not g: return jsonify({"error": "No game"})
    return jsonify(deal(g))

@app.route("/draw/hold", methods=["POST"])
def draw_hold():
    g = get_game("draw")
    if not g: return jsonify({"error": "No game"})
    data = request.json
    return jsonify(toggle_hold_poker(g, data["player"], data["card"]))

@app.route("/draw/draw", methods=["POST"])
def draw_draw():
    g = get_game("draw")
    if not g: return jsonify({"error": "No game"})
    pidx = request.json.get("player", 0)
    return jsonify(draw(g, pidx))

@app.route("/draw/showdown", methods=["POST"])
def draw_showdown():
    g = get_game("draw")
    if not g: return jsonify({"error": "No game"})
    return jsonify(showdown(g))

@app.route("/draw/state")
def draw_state():
    g = get_game("draw")
    if not g: return jsonify({"error": "No game"})
    pidx = int(request.args.get("player", 0))
    return jsonify(draw_poker_state(g, pidx))

# ─── HOLD'EM ROUTES ───────────────────────────────────────────────────────────

@app.route("/holdem/new", methods=["POST"])
def holdem_new():
    data = request.json
    players = data.get("players", ["Player 1", "Player 2"])
    g = new_holdem(players)
    set_game("holdem", g)
    return jsonify(holdem_state(g))

@app.route("/holdem/deal", methods=["POST"])
def holdem_deal():
    g = get_game("holdem")
    if not g: return jsonify({"error": "No game"})
    return jsonify(deal_holdem(g))

@app.route("/holdem/flop", methods=["POST"])
def holdem_flop():
    g = get_game("holdem")
    if not g: return jsonify({"error": "No game"})
    return jsonify(deal_flop(g))

@app.route("/holdem/turn", methods=["POST"])
def holdem_turn():
    g = get_game("holdem")
    if not g: return jsonify({"error": "No game"})
    return jsonify(deal_turn(g))

@app.route("/holdem/river", methods=["POST"])
def holdem_river():
    g = get_game("holdem")
    if not g: return jsonify({"error": "No game"})
    return jsonify(deal_river(g))

@app.route("/holdem/bet", methods=["POST"])
def holdem_bet():
    g = get_game("holdem")
    if not g: return jsonify({"error": "No game"})
    data = request.json
    return jsonify(bet(g, data["player"], data["amount"]))

@app.route("/holdem/fold", methods=["POST"])
def holdem_fold():
    g = get_game("holdem")
    if not g: return jsonify({"error": "No game"})
    return jsonify(fold(g, request.json["player"]))

@app.route("/holdem/showdown", methods=["POST"])
def holdem_showdown_route():
    g = get_game("holdem")
    if not g: return jsonify({"error": "No game"})
    return jsonify(holdem_showdown(g))

@app.route("/holdem/state")
def holdem_state_route():
    g = get_game("holdem")
    if not g: return jsonify({"error": "No game"})
    pidx = int(request.args.get("player", 0))
    return jsonify(holdem_state(g, pidx))

if __name__ == "__main__":
    app.run(port=5002, debug=True)
