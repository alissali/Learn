# AOS.CONTEXT — Formal Specification
**AOS 1 — Multi-Discipline Interpretation**
MIT License — Open. Free. Forever.

---

## NAME
AOS.CONTEXT

## FACT
An Expression has no absolute meaning.
Meaning is relative to the active Dictionary.
The Dictionary IS the Context.
Interpretation is always **In Current Context**.

---

## FORMAL RULE

```
interpret(Expression) → SUSPENDED
interpret(Expression, Dictionary) → Operation
```

Without Context → Expression is **suspended**.
With Context → Expression is **executable**.

---

## DEFINITION

| Term | AOS Object | Meaning |
|---|---|---|
| Expression | NAME / FACT / TARGET | One coherent unit of meaning |
| Dictionary | Context | Active discipline at interpretation time |
| Operation | Executable | Result of interpret(Expression, Dictionary) |

---

## MULTI-DISCIPLINE EXAMPLE

**Expression:** `buy / acquire asset / portfolio`

| Dictionary | Interpretation |
|---|---|
| AOS.JuX | financial transaction — `execute(buy)` |
| AOS.LEGAL | contractual obligation — `validate(buy)` |
| AOS.MEDICAL | contraindicated — `block(buy)` |
| AOS.ARABIC | root ب-ي-ع → derive() → Forms I–X |

One Expression. Four Disciplines. Four Operations. Zero ambiguity — within Context.

---

## POSITION IN AOS HIERARCHY

```
1. Objects (NAME / FACT / TARGET)
2. Expressions
3. Sentences        ← interpret(Expression, Context) fires here
4. Dictionaries     ← Context lives here
5. Services
```

Context is **not a sixth level.**
Context is the **active Dictionary at interpretation time.**

---

## RELATION TO MNMNM

```
MNMNM → selects Context → fires Expression → AOS executes
```

MNMNM is the shell.
Context is the resolver.
AOS is the engine.

---

## RELATION TO AOS DICTIONARIES

| Dictionary | Domain | Context activates |
|---|---|---|
| AOS.MINIMAL | Foundation | base Operations |
| AOS.JuX | Software / Finance | buy, mortgage, roll, pay |
| AOS.BUG-MIB | Bug Management | capture, transmit, close |
| AOS.MEDICAL | Symptom → Outcome | diagnose, treat, discharge |
| AOS.ENGINEERING | Requirement → System | specify, build, validate |
| AOS.LEGAL | Claim → Verdict | file, argue, rule |
| AOS.ARABIC | Root → Derivative | derive, form, pattern |

---

## AOS 1 — THE ADVANCEMENT

AOS 0: One Dictionary. One discipline. Expressions interpreted globally.
AOS 1: Multiple Disciplines. Same Expression. Interpreted **In Current Context**.

**AOS 1 is not a new architecture. It is AOS fully operational.**

---

## LICENSE
MIT — Open. Free. Forever.
