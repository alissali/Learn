# JeuX — Game Platform

**JuX → JeuX**. Three games. One engine.

## Games
- **JuXYams** — 5-dice Yams / Yahtzee
- **5-Card Draw Poker** — classic draw poker
- **Texas Hold'em** — community card poker

## Architecture
```
JeuX/
├── core/
│   ├── combination_engine.py   ← shared (Yams + Poker)
│   └── player_engine.py        ← shared (all games)
├── juxyams/yams.py
├── poker_draw/poker_draw.py
├── holdem/holdem.py
└── web/
    ├── app.py                  ← Flask, port 5002
    └── templates/jeux.html
```

## Run
```bash
cd JeuX
pip install flask
flask --app web/app run --port 5002
```
Open: http://localhost:5002

## CULTURE BUG
Part of JuXITT. Bugs named. Dated. Owned.
