# mMonopoly — Backlog

NAME: mMonopoly Backlog  
FACT: Extracted from Monopoly.py TODO block. Separated from code. Living document.  
RULE: Every item here has a TYPE, a STATUS, and a NAME. No noise.

---

## BUGS

| # | Name | Location | Status | Note |
|---|------|----------|--------|------|
| B1 | IndexError in buyHouse | line 727, menu → buyHouses() | Open | `list index out of range` |
| B2 | IndexError in playCard | line 602, playCard | Open | `pop from empty list` |
| B3 | AttributeError in cmpHouses | line 246, UtilitySquare | **SOLVED** | Tue Mar 25 17:13:46 CET 2025 @717 /Internet Time/ — `UtilitySquare` has no `getnbHouses` |
| B4 | Double addition mortgage amount | unmortgageProperty | **DONE** | |
| B5 | attemptPurchase return type | attemptPurchase → bool | Check needed | `TODO: check` |

---

## FEATURES

### Core Game Logic

| # | Name | Priority | Status | Note |
|---|------|----------|--------|------|
| F1 | Player knows game (out-of-game detection) | Medium | Open | Players eliminated from game |
| F2 | tax square | Medium | Open | |
| F3 | buyHouses(): 2 by default | Low | Open | |
| F4 | addHouse() and rent calculation | Medium | Open | |
| F5 | priceHotel instead of price[4] | Low | Open | mini-feature |
| F6 | exchange(): check owner | Medium | Open | |
| F7 | mortgage value from DB | Medium | Open | |
| F8 | sell and/or exchange out-of-jail card | Low | Open | mini-feature |
| F9 | Using out-of-jail card: not auto | Medium | Open | U.I. |

### Payment / Cash Logic

| # | Name | Priority | Status | Note |
|---|------|----------|--------|------|
| P1 | Not enough cash — all situations handled | **High** | Open | Occurs in: payRent, Chance card, buyHouses, jail exit, passing departure |
| P2 | attemptPurchase: use sellHouses + mortgage when not enough cash | High | Open | |
| P3 | payPlayer() | Medium | Open | |
| P4 | getCash() | Medium | Open | line 928 |
| P5 | Decorator-like solution for no-cash situations | Medium | Open | "decorator-lime solution seems appropriate" |

### UI / Menu

| # | Name | Priority | Status | Note |
|---|------|----------|--------|------|
| U1 | principal menu: adapt to player.properties | **Urgent** | Open | `adapt principal menu(player | player.properties)` |
| U2 | After attemptPurchase: propose menu() | Medium | Open | micro-feature |
| U3 | Menu after: no money, jail exit, passing departure | Medium | Open | Extension |

---

## TECHNICAL DEBT / CODE SMELL

| # | Name | Location | Status | Note |
|---|------|----------|--------|------|
| T1 | exchangeProperty UnitOfWork | exchange() | Open | Technical feature — needs proper UoW pattern |
| T2 | Player.attemptPurchase: replace insert+sort with insertInSorted | attemptPurchase | Open | Performance |
| T3 | Use Square.ind instead of board.index() | Multiple | Open | |
| T4 | List Collection — clean up | Multiple | Open | |
| T5 | Register Players — clean up | Init | Open | |
| T6 | Defensive Programming — Collection methods | Collections | Open | Long colorname expression needs cleanup |
| T7 | unmortgageProperty: mortgagedList smell | unmortgageProperty | Open | code smell |

---

## DONE ✅

| # | Name | Done When | Note |
|---|------|-----------|------|
| D1 | Property exchange | — | Done |
| D2 | mortgage | — | Done |
| D3 | Addresses in Cards (+MySQL) | — | Done |
| D4 | rent in DB and initialisation | — | Done after infinite parties |
| D5 | payRent: payOwner(allIveGot) when defect | — | Done |
| D6 | check mortgage amounts | — | Done (double addition fixed) |
| D7 | Parking — nothing to do per standard rules | — | Done, no more occurrences |
| D8 | BUG: printProperties AttributeError UtilitySquare | Tue Mar 25 17:13:46 CET 2025 @717 /Internet Time/ | **CULTURE BUG** — Solved to the second |

---

## CONTINUOUS

| # | Name | Note |
|---|------|------|
| C1 | Testing | Continuous. Always. |

---

*Living document. Extracted from code. Belongs here, not in Monopoly.py.*  
*"I produce Coherent Software that handles its own worms."*
