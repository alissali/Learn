from flask import Flask, render_template, request, jsonify, session
import random
import json
import os

app = Flask(__name__)
app.secret_key = 'juxitt_monopoly_secret'

# ── BOARD DATA ──────────────────────────────────────────────────────────────
SQUARES = [
    {"name": "GO",              "type": "go",       "price": 0,   "color": None,      "rent": [0]},
    {"name": "Mediterranean",   "type": "property", "price": 60,  "color": "purple",  "rent": [2,10,30,90,160,250]},
    {"name": "Community Chest", "type": "cc",       "price": 0,   "color": None,      "rent": [0]},
    {"name": "Baltic",          "type": "property", "price": 60,  "color": "purple",  "rent": [4,20,60,180,320,450]},
    {"name": "Income Tax",      "type": "tax",      "price": 200, "color": None,      "rent": [0]},
    {"name": "Reading RR",      "type": "railroad", "price": 200, "color": "black",   "rent": [25,50,100,200]},
    {"name": "Oriental",        "type": "property", "price": 100, "color": "lblue",   "rent": [6,30,90,270,400,550]},
    {"name": "Chance",          "type": "chance",   "price": 0,   "color": None,      "rent": [0]},
    {"name": "Vermont",         "type": "property", "price": 100, "color": "lblue",   "rent": [6,30,90,270,400,550]},
    {"name": "Connecticut",     "type": "property", "price": 120, "color": "lblue",   "rent": [8,40,100,300,450,600]},
    {"name": "Jail/Visit",      "type": "jail",     "price": 0,   "color": None,      "rent": [0]},
    {"name": "St. Charles",     "type": "property", "price": 140, "color": "pink",    "rent": [10,50,150,450,625,750]},
    {"name": "Electric Co.",    "type": "utility",  "price": 150, "color": "white",   "rent": [0]},
    {"name": "States",          "type": "property", "price": 140, "color": "pink",    "rent": [10,50,150,450,625,750]},
    {"name": "Virginia",        "type": "property", "price": 160, "color": "pink",    "rent": [12,60,180,500,700,900]},
    {"name": "Pennsylvania RR", "type": "railroad", "price": 200, "color": "black",   "rent": [25,50,100,200]},
    {"name": "St. James",       "type": "property", "price": 180, "color": "orange",  "rent": [14,70,200,550,750,950]},
    {"name": "Community Chest", "type": "cc",       "price": 0,   "color": None,      "rent": [0]},
    {"name": "Tennessee",       "type": "property", "price": 180, "color": "orange",  "rent": [14,70,200,550,750,950]},
    {"name": "New York",        "type": "property", "price": 200, "color": "orange",  "rent": [16,80,220,600,800,1000]},
    {"name": "Free Parking",    "type": "parking",  "price": 0,   "color": None,      "rent": [0]},
    {"name": "Kentucky",        "type": "property", "price": 220, "color": "red",     "rent": [18,90,250,700,875,1050]},
    {"name": "Chance",          "type": "chance",   "price": 0,   "color": None,      "rent": [0]},
    {"name": "Indiana",         "type": "property", "price": 220, "color": "red",     "rent": [18,90,250,700,875,1050]},
    {"name": "Illinois",        "type": "property", "price": 240, "color": "red",     "rent": [20,100,300,750,925,1100]},
    {"name": "B&O RR",          "type": "railroad", "price": 200, "color": "black",   "rent": [25,50,100,200]},
    {"name": "Atlantic",        "type": "property", "price": 260, "color": "yellow",  "rent": [22,110,330,800,975,1150]},
    {"name": "Ventnor",         "type": "property", "price": 260, "color": "yellow",  "rent": [22,110,330,800,975,1150]},
    {"name": "Water Works",     "type": "utility",  "price": 150, "color": "white",   "rent": [0]},
    {"name": "Marvin Gardens",  "type": "property", "price": 280, "color": "yellow",  "rent": [24,120,360,850,1025,1200]},
    {"name": "Go To Jail",      "type": "gotojail", "price": 0,   "color": None,      "rent": [0]},
    {"name": "Pacific",         "type": "property", "price": 300, "color": "green",   "rent": [26,130,390,900,1100,1275]},
    {"name": "N. Carolina",     "type": "property", "price": 300, "color": "green",   "rent": [26,130,390,900,1100,1275]},
    {"name": "Community Chest", "type": "cc",       "price": 0,   "color": None,      "rent": [0]},
    {"name": "Pennsylvania",    "type": "property", "price": 320, "color": "green",   "rent": [28,150,450,1000,1200,1400]},
    {"name": "Short Line RR",   "type": "railroad", "price": 200, "color": "black",   "rent": [25,50,100,200]},
    {"name": "Chance",          "type": "chance",   "price": 0,   "color": None,      "rent": [0]},
    {"name": "Park Place",      "type": "property", "price": 350, "color": "dblue",   "rent": [35,175,500,1100,1300,1500]},
    {"name": "Luxury Tax",      "type": "tax",      "price": 75,  "color": None,      "rent": [0]},
    {"name": "Boardwalk",       "type": "property", "price": 400, "color": "dblue",   "rent": [50,200,600,1400,1700,2000]},
]

CHANCE_CARDS = [
    "Advance to GO. Collect $200.",
    "Bank pays you dividend of $50.",
    "Go back 3 spaces.",
    "Go to Jail.",
    "Pay poor tax of $15.",
    "Take a trip to Reading Railroad.",
    "You have been elected Chairman. Pay each player $50.",
    "Your building loan matures. Collect $150.",
    "Advance to Illinois Ave.",
    "Advance to St. Charles Place.",
]

CC_CARDS = [
    "Bank error in your favor. Collect $200.",
    "Doctor's fees. Pay $50.",
    "From sale of stock you get $50.",
    "Go to Jail.",
    "Holiday fund matures. Receive $100.",
    "Income tax refund. Collect $20.",
    "Life insurance matures. Collect $100.",
    "Pay hospital fees of $100.",
    "Pay school fees of $50.",
    "Receive $25 consultancy fee.",
]

COLORS = {
    "purple": ["Mediterranean", "Baltic"],
    "lblue":  ["Oriental", "Vermont", "Connecticut"],
    "pink":   ["St. Charles", "States", "Virginia"],
    "orange": ["St. James", "Tennessee", "New York"],
    "red":    ["Kentucky", "Indiana", "Illinois"],
    "yellow": ["Atlantic", "Ventnor", "Marvin Gardens"],
    "green":  ["Pacific", "N. Carolina", "Pennsylvania"],
    "dblue":  ["Park Place", "Boardwalk"],
}

def new_game(player_names):
    players = []
    tokens = ["🎩", "🚗", "🐕", "⚓", "🎸", "✈️"]
    for i, name in enumerate(player_names):
        players.append({
            "name": name,
            "cash": 1500,
            "position": 0,
            "properties": [],
            "in_jail": False,
            "jail_turns": 0,
            "out_of_jail_cards": 0,
            "token": tokens[i % len(tokens)],
            "active": True,
        })
    return {
        "players": players,
        "current": 0,
        "board": SQUARES,
        "owners": {},     # square_index -> player_index
        "houses": {},     # square_index -> house count (4=hotel)
        "mortgaged": {},  # square_index -> True if mortgaged
        "log": ["Game started! Good luck to all players! 🎲"],
        "phase": "roll",  # roll | action | buy | end
        "last_roll": None,
        "chance_deck": CHANCE_CARDS.copy(),
        "cc_deck": CC_CARDS.copy(),
        "free_parking_pot": 0,
    }

def roll_dice():
    d1, d2 = random.randint(1,6), random.randint(1,6)
    return d1, d2

def get_color_owner(game, color):
    props = COLORS.get(color, [])
    owners = set()
    for i, sq in enumerate(game["board"]):
        if sq["name"] in props:
            o = game["owners"].get(i)
            if o is None:
                return None
            owners.add(o)
    return owners.pop() if len(owners) == 1 else None

def calc_rent(game, sq_idx, player_idx, dice_total):
    # B7 — Railroad rent: verified correct.
    # owned_rr=1 → rent[0]=$25, 2 → rent[1]=$50, 3 → rent[2]=$100, 4 → rent[3]=$200.
    # Uses sq["rent"][min(owned_rr-1, 3)] which is correct. ✓
    sq = game["board"][sq_idx]
    owner_idx = game["owners"].get(sq_idx)
    if owner_idx is None or owner_idx == player_idx:
        return 0
    if game["mortgaged"].get(sq_idx):
        return 0  # mortgaged — no rent
    if sq["type"] == "railroad":
        owned_rr = sum(1 for i,o in game["owners"].items() if o == owner_idx and game["board"][i]["type"] == "railroad")
        return sq["rent"][min(owned_rr-1, 3)]
    if sq["type"] == "utility":
        owned_ut = sum(1 for i,o in game["owners"].items() if o == owner_idx and game["board"][i]["type"] == "utility")
        return dice_total * (4 if owned_ut == 1 else 10)
    houses = game["houses"].get(sq_idx, 0)
    color_owner = get_color_owner(game, sq["color"])
    if houses == 0 and color_owner == owner_idx:
        return sq["rent"][0] * 2
    return sq["rent"][min(houses, len(sq["rent"])-1)]

# B9 — land_on_square: extracted from do_roll so card moves can trigger square effects.
def land_on_square(game, log, dice_total=0):
    """Handle ALL square landing effects for the current player at their current position."""
    player = game["players"][game["current"]]
    sq_idx = player["position"]
    sq = game["board"][sq_idx]

    game["phase"] = "action"
    game["pending_action"] = None

    if sq["type"] == "go":
        game["phase"] = "end"
    elif sq["type"] == "gotojail":
        player["in_jail"] = True
        player["position"] = 10
        log.append(f"👮 {player['name']} went to Jail!")
        game["phase"] = "end"
    elif sq["type"] == "tax":
        player["cash"] -= sq["price"]
        game["free_parking_pot"] += sq["price"]
        log.append(f"💸 {player['name']} paid tax of ${sq['price']}.")
        # B16 — debt warning after tax payment
        if player["cash"] < 0:
            log.append(f"⚠️ {player['name']} is in debt! Cash: ${player['cash']}. Must sell or mortgage to recover.")
        game["phase"] = "end"
    elif sq["type"] == "parking":
        pot = game["free_parking_pot"]
        player["cash"] += pot
        game["free_parking_pot"] = 0
        log.append(f"🅿️ {player['name']} collected Free Parking pot: ${pot}!")
        game["phase"] = "end"
    elif sq["type"] == "jail":
        log.append(f"👀 {player['name']} is just visiting jail.")
        game["phase"] = "end"
    elif sq["type"] == "chance":
        card = game["chance_deck"].pop(0)
        game["chance_deck"].append(card)
        log.append(f"🃏 Chance: {card}")
        game = apply_card(game, card, log)
    elif sq["type"] == "cc":
        card = game["cc_deck"].pop(0)
        game["cc_deck"].append(card)
        log.append(f"📦 Community Chest: {card}")
        game = apply_card(game, card, log)
    elif sq["type"] in ("property", "railroad", "utility"):
        owner_idx = game["owners"].get(sq_idx)
        if owner_idx is None:
            game["phase"] = "buy"
            log.append(f"🏠 {sq['name']} is available for ${sq['price']}. Buy?")
        elif owner_idx == game["current"]:
            log.append(f"🏠 You own {sq['name']}.")
            game["phase"] = "end"
        else:
            rent = calc_rent(game, sq_idx, game["current"], dice_total)
            owner = game["players"][owner_idx]
            player["cash"] -= rent
            owner["cash"] += rent
            log.append(f"💰 {player['name']} paid ${rent} rent to {owner['name']}.")
            # B16 — debt warning after rent payment
            if player["cash"] < 0:
                log.append(f"⚠️ {player['name']} is in debt! Cash: ${player['cash']}. Must sell or mortgage to recover.")
            game["phase"] = "end"

    return game

def do_roll(game):
    player = game["players"][game["current"]]
    d1, d2 = roll_dice()
    total = d1 + d2
    game["last_roll"] = [d1, d2]
    log = []

    if player["in_jail"]:
        if d1 == d2:
            player["in_jail"] = False
            player["jail_turns"] = 0
            log.append(f"🎲 {player['name']} rolled doubles ({d1}+{d2}) and got out of jail!")
        else:
            player["jail_turns"] += 1
            if player["jail_turns"] >= 3:
                player["cash"] -= 50
                player["in_jail"] = False
                player["jail_turns"] = 0
                log.append(f"🎲 {player['name']} rolled {d1}+{d2}. Paid $50 to get out of jail!")
                # B16 — debt warning after jail fee payment
                if player["cash"] < 0:
                    log.append(f"⚠️ {player['name']} is in debt! Cash: ${player['cash']}. Must sell or mortgage to recover.")
            else:
                log.append(f"🎲 {player['name']} rolled {d1}+{d2}. Still in jail (turn {player['jail_turns']}/3).")
                game["phase"] = "end"
                game["log"] += log
                return game

    old_pos = player["position"]
    player["position"] = (player["position"] + total) % 40
    if player["position"] < old_pos:
        player["cash"] += 200
        log.append(f"✈️ {player['name']} passed GO! Collected $200.")

    sq = game["board"][player["position"]]
    log.append(f"🎲 {player['name']} rolled {d1}+{d2}={total} → landed on {sq['name']}")

    # B9 — delegate all square handling to land_on_square()
    game = land_on_square(game, log, total)

    game["log"] += log
    return game

def apply_card(game, card, log):
    player = game["players"][game["current"]]
    card_l = card.lower()
    if "advance to go" in card_l:
        # Advance to GO: collect $200, no square effect needed
        player["position"] = 0
        player["cash"] += 200
        game["phase"] = "end"
    elif "go to jail" in card_l:
        # Go to Jail: just jail, no square effect
        player["in_jail"] = True
        player["position"] = 10
        game["phase"] = "end"
    elif "back 3 spaces" in card_l:
        # B9 — movement card: trigger square effect at new position
        player["position"] = max(0, player["position"] - 3)
        game = land_on_square(game, log)
    elif "dividend" in card_l or "bank error" in card_l or "holiday" in card_l or "insurance" in card_l or "consultancy" in card_l:
        amt = int(''.join(filter(str.isdigit, card))) if any(c.isdigit() for c in card) else 50
        player["cash"] += amt
        game["phase"] = "end"
    elif "pay" in card_l or "fees" in card_l or "tax" in card_l:
        amt = int(''.join(filter(str.isdigit, card))) if any(c.isdigit() for c in card) else 50
        player["cash"] -= amt
        game["free_parking_pot"] += amt
        game["phase"] = "end"
    elif "reading railroad" in card_l:
        # B9 — movement card: trigger square effect at Reading RR (pos 5)
        player["position"] = 5
        game = land_on_square(game, log)
    elif "illinois" in card_l:
        # B9 — movement card: trigger square effect at Illinois Ave (pos 24)
        player["position"] = 24
        game = land_on_square(game, log)
    elif "st. charles" in card_l:
        # B9 — movement card: trigger square effect at St. Charles (pos 11)
        player["position"] = 11
        game = land_on_square(game, log)
    elif "chairman" in card_l:
        amt = 50
        for i, p in enumerate(game["players"]):
            if i != game["current"] and p["active"]:
                p["cash"] += amt
                player["cash"] -= amt
        game["phase"] = "end"
    else:
        game["phase"] = "end"
    return game

def do_buy(game):
    player = game["players"][game["current"]]
    sq_idx = player["position"]
    sq = game["board"][sq_idx]
    if player["cash"] >= sq["price"]:
        player["cash"] -= sq["price"]
        game["owners"][sq_idx] = game["current"]
        player["properties"].append(sq_idx)
        game["log"].append(f"✅ {player['name']} bought {sq['name']} for ${sq['price']}!")
    else:
        game["log"].append(f"❌ Not enough cash to buy {sq['name']}!")
    game["phase"] = "end"
    return game

def do_mortgage(game, sq_idx):
    player = game["players"][game["current"]]
    sq = game["board"][sq_idx]
    owner_idx = game["owners"].get(sq_idx)
    if owner_idx != game["current"]:
        game["log"].append(f"❌ You don't own {sq['name']}.")
        return game
    if game["mortgaged"].get(sq_idx):
        game["log"].append(f"❌ {sq['name']} is already mortgaged.")
        return game
    if game["houses"].get(sq_idx, 0) > 0:
        game["log"].append(f"❌ Remove houses from {sq['name']} before mortgaging.")
        return game
    mortgage_value = sq["price"] // 2
    player["cash"] += mortgage_value
    game["mortgaged"][sq_idx] = True
    game["log"].append(f"🏦 {player['name']} mortgaged {sq['name']} for ${mortgage_value}.")
    return game

def do_unmortgage(game, sq_idx):
    player = game["players"][game["current"]]
    sq = game["board"][sq_idx]
    owner_idx = game["owners"].get(sq_idx)
    if owner_idx != game["current"]:
        game["log"].append(f"❌ You don't own {sq['name']}.")
        return game
    if not game["mortgaged"].get(sq_idx):
        game["log"].append(f"❌ {sq['name']} is not mortgaged.")
        return game
    cost = int(sq["price"] // 2 * 1.1)  # mortgage value + 10% interest
    if player["cash"] < cost:
        game["log"].append(f"❌ Need ${cost} to unmortgage {sq['name']}. You have ${player['cash']}.")
        return game
    player["cash"] -= cost
    game["mortgaged"][sq_idx] = False
    game["log"].append(f"✅ {player['name']} unmortgaged {sq['name']} for ${cost} (10% interest included).")
    return game

def do_pass(game):
    game["log"].append(f"⏭️ {game['players'][game['current']]['name']} passed on buying.")
    game["phase"] = "end"
    return game

def end_turn(game):
    n = len(game["players"])
    next_p = (game["current"] + 1) % n
    count = 0
    while not game["players"][next_p]["active"] and count < n:
        next_p = (next_p + 1) % n
        count += 1
    game["current"] = next_p
    game["phase"] = "roll"
    game["log"].append(f"--- {game['players'][next_p]['name']}'s turn ---")
    return game

# ── ROUTES ───────────────────────────────────────────────────────────────────
@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/api/new", methods=["POST"])
def api_new():
    data = request.get_json()
    names = data.get("players", ["Player 1", "Player 2"])
    game = new_game(names)
    session["game"] = game
    return jsonify(game)

@app.route("/api/state", methods=["GET"])
def api_state():
    game = session.get("game")
    if not game:
        return jsonify({"error": "No game"}), 404
    return jsonify(game)

@app.route("/api/roll", methods=["POST"])
def api_roll():
    game = session.get("game")
    if not game:
        return jsonify({"error": "No game"}), 404
    game = do_roll(game)
    session["game"] = game
    return jsonify(game)

@app.route("/api/buy", methods=["POST"])
def api_buy():
    game = session.get("game")
    if not game:
        return jsonify({"error": "No game"}), 404
    game = do_buy(game)
    session["game"] = game
    return jsonify(game)

@app.route("/api/pass", methods=["POST"])
def api_pass():
    game = session.get("game")
    if not game:
        return jsonify({"error": "No game"}), 404
    game = do_pass(game)
    session["game"] = game
    return jsonify(game)

@app.route("/api/mortgage", methods=["POST"])
def api_mortgage():
    game = session.get("game")
    if not game:
        return jsonify({"error": "No game"}), 404
    data = request.get_json()
    sq_idx = int(data.get("sq_idx", -1))
    game = do_mortgage(game, sq_idx)
    session["game"] = game
    return jsonify(game)

@app.route("/api/unmortgage", methods=["POST"])
def api_unmortgage():
    game = session.get("game")
    if not game:
        return jsonify({"error": "No game"}), 404
    data = request.get_json()
    sq_idx = int(data.get("sq_idx", -1))
    game = do_unmortgage(game, sq_idx)
    session["game"] = game
    return jsonify(game)

@app.route("/api/end_turn", methods=["POST"])
def api_end_turn():
    game = session.get("game")
    if not game:
        return jsonify({"error": "No game"}), 404
    game = end_turn(game)
    session["game"] = game
    return jsonify(game)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
