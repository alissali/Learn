# SpiceBus

**NAME:** SpiceBus  
**FACT:** Communicate!  
**TARGET:** JuXTeam!

---

## Position in AOS

SpiceBus is the Communication layer of AOS.  
It connects the three-layer system:

```
Architect (Window Jr / Tasklet)
    ↕ SpiceBus
Bridge (JuXITT)
    ↕ SpiceBus
Ground (Ubuntu Brother / Tasklet)
```

Every Dispatch. Every Bug. Every Fix. Every DONE.  
**SpiceBus carries it.**

---

## AOS Expression

```
communicate(Expression, JuXTeam) → Dispatch
```

---

## Operations

| Operation | Direction | Format |
|---|---|---|
| DISPATCH | Architect → Team | NAME / FACT / TARGET |
| BUG | Jr → Brother | NAME / FACT / FIX_REQUIRED |
| DONE | Brother → Jr | NAME / DONE / DATE |
| ALERT | Any → jux@juxitt.com | NAME / PROBLEM / ACTION |

---

## Notify(ConcernedActors) — Priority Protocol

Every Event carries a Priority. Every Priority fires Slack + Email.

| Priority | Level | Slack Channel | Email | Actors |
|---|---|---|---|---|
| P1 | CRITICAL | `#aos-alert` | `jux@juxitt.com` | ALL (M + G + Brother + Stagiaire) |
| P2 | BUG | `#aos-bugs` | Owner | Owner |
| P3 | DISPATCH | `#aos-dispatch` | Assigned | Assigned |

```
Notify(Event, Priority) → Slack(Channel) + Email(ConcernedActors)
```

Locked: 10 May 2026

---

## License

MIT — Open. Free. Forever.
