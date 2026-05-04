"""
JeuX — Core: Combination Engine
Shared by JuXYams and Poker.
NAME / FACT / TARGET.
"""

from collections import Counter

# ─── YAMS COMBINATIONS ───────────────────────────────────────────────────────

YAMS_COMBINATIONS = [
    "ones", "twos", "threes", "fours", "fives", "sixes",
    "three_of_a_kind", "four_of_a_kind", "full_house",
    "small_straight", "large_straight", "yams", "chance"
]

def score_yams(dice, combo):
    """Score a Yams combination given 5 dice values."""
    counts = Counter(dice)
    vals = sorted(counts.keys())
    total = sum(dice)

    if combo in ("ones","twos","threes","fours","fives","sixes"):
        face = ("ones","twos","threes","fours","fives","sixes").index(combo) + 1
        return sum(d for d in dice if d == face)

    if combo == "three_of_a_kind":
        return total if any(v >= 3 for v in counts.values()) else 0

    if combo == "four_of_a_kind":
        return total if any(v >= 4 for v in counts.values()) else 0

    if combo == "full_house":
        c = sorted(counts.values())
        return 25 if c == [2, 3] else 0

    if combo == "small_straight":
        sets = set(dice)
        if {1,2,3,4}.issubset(sets) or {2,3,4,5}.issubset(sets) or {3,4,5,6}.issubset(sets):
            return 30
        return 0

    if combo == "large_straight":
        if set(dice) in ({1,2,3,4,5}, {2,3,4,5,6}):
            return 40
        return 0

    if combo == "yams":
        return 50 if len(counts) == 1 else 0

    if combo == "chance":
        return total

    return 0

def available_yams_combos(used_combos):
    return [c for c in YAMS_COMBINATIONS if c not in used_combos]


# ─── POKER HAND EVALUATION ───────────────────────────────────────────────────

POKER_HANDS = [
    "high_card", "one_pair", "two_pair", "three_of_a_kind",
    "straight", "flush", "full_house", "four_of_a_kind",
    "straight_flush", "royal_flush"
]

HAND_RANK = {h: i for i, h in enumerate(POKER_HANDS)}

def evaluate_poker_hand(cards):
    """
    cards: list of (value, suit) tuples
    value: 2-14 (14=Ace), suit: 'S','H','D','C'
    Returns (hand_name, rank, tiebreak_values)
    """
    values = sorted([c[0] for c in cards], reverse=True)
    suits  = [c[1] for c in cards]
    counts = Counter(values)
    freq   = sorted(counts.values(), reverse=True)
    is_flush    = len(set(suits)) == 1
    is_straight = (len(set(values)) == 5 and (max(values) - min(values) == 4))
    # Ace-low straight: A-2-3-4-5
    ace_low = set(values) == {14, 2, 3, 4, 5}
    if ace_low:
        is_straight = True
        values = [5, 4, 3, 2, 1]  # tiebreak as 5-high

    if is_straight and is_flush:
        name = "royal_flush" if min(values) == 10 else "straight_flush"
    elif freq[0] == 4:
        name = "four_of_a_kind"
    elif freq[:2] == [3, 2]:
        name = "full_house"
    elif is_flush:
        name = "flush"
    elif is_straight:
        name = "straight"
    elif freq[0] == 3:
        name = "three_of_a_kind"
    elif freq[:2] == [2, 2]:
        name = "two_pair"
    elif freq[0] == 2:
        name = "one_pair"
    else:
        name = "high_card"

    # tiebreak: sort by frequency then value
    tiebreak = sorted(counts.keys(), key=lambda v: (counts[v], v), reverse=True)
    return name, HAND_RANK[name], tiebreak

def compare_hands(hand_a, hand_b):
    """Returns 1 if A wins, -1 if B wins, 0 if tie."""
    _, rank_a, tb_a = hand_a
    _, rank_b, tb_b = hand_b
    if rank_a != rank_b:
        return 1 if rank_a > rank_b else -1
    for a, b in zip(tb_a, tb_b):
        if a != b:
            return 1 if a > b else -1
    return 0
