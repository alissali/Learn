# AOS.BUG-MIB — Management Information Base for Bugs
**LICENSE: MIT**
**Version: 0.01 — Thu 7 May 2026**

---

## Schema

| Field | Type | Rule |
|---|---|---|
| ID | NAME | Immutable once assigned |
| Description | FACT | What the bug IS |
| Category | TYPE | CODE / COMPLEXITY / CULTURE / ARCHITECTURE |
| Fix Required | TARGET | What must change |
| Owner | NAME | Jr (Window) / Brother (Ubuntu) / OPEN |
| Status | STATE | OPEN / IN-PROGRESS / CLOSED |
| Date | DATE | Assigned on OPEN. Immutable on CLOSE. |
| Comment | FACT | Architectural diagnosis |

---

## Category: COMPLEXITY-BUG

> A COMPLEXITY-BUG is not a code defect.
> It is a **design failure** — when a system accumulates complexity beyond its purpose.
> Symptom: user cognitive load exceeds tool value.
> AOS diagnosis: Missing MNMNM shell. No Dictionary. No formal language. **Inverted MIP.**

---

## Registry

---

### CB-001

| Field | Value |
|---|---|
| **ID** | CB-001 |
| **NAME** | LIBREOFFICE/COMPLEXITY-BUG |
| **Description** | 30 years of UI decisions with no unifying language. Every toolbar, every menu, every dialog is a separate dialect. No Dictionary. No MNMNM. |
| **Category** | COMPLEXITY-BUG |
| **Fix Required** | Formal Dictionary. One language across all modules. MNMNM shell at entry point. |
| **Owner** | OPEN |
| **Status** | OPEN |
| **Date** | Thu 7 May 2026 |
| **Comment** | LibreOffice is not a tool. It is an **accumulation**. Each version added features. None removed complexity. The user spends 80% of cognitive energy navigating the interface, 20% on actual work. **Inverted MIP.** AOS diagnosis: zero Expressions, zero Sentences — only raw Operations scattered across 400 toolbar buttons with no Dictionary to organize them. The MNMNM shell never existed. The Diamond was never cut. What remains is raw carbon. |

---

### CB-002

| Field | Value |
|---|---|
| **ID** | CB-002 |
| **NAME** | UMBRELLO/COMPLEXITY-BUG |
| **Description** | UML diagram tool. 47 diagram types. 200+ toolbar buttons. Nested menus 4 levels deep. Models complexity instead of reducing it. |
| **Category** | COMPLEXITY-BUG |
| **Fix Required** | One Expression per diagram type. MNMNM entry: one word → correct diagram selected, canvas ready. |
| **Owner** | OPEN |
| **Status** | OPEN |
| **Date** | Thu 7 May 2026 |
| **Comment** | Umbrello's fundamental error: it confused **modelling a system** with **being a system**. A tool that diagrams complexity must itself be simple. It is not. The Dictionary is missing — 47 diagram types with no organizing principle, no hierarchy, no NAME/FACT/TARGET. Every diagram is an island. The user must already know UML to use the tool. **A Dictionary that requires its own Dictionary is not a Dictionary — it is a maze.** AOS sentence never written: `draw(class_diagram)` → canvas open, palette ready, export set. Instead: File → New → Diagram Type → Select from list of 47 → Configure → Apply. This is not a tool. This is archaeology. |

---

## Sentences

```
capture(NAME)     → opens new MIB entry
transmit(NAME)    → sends to Owner
close(NAME)       → marks CLOSED, date locked, immutable
query(Status)     → returns all entries matching Status
query(Category)   → returns all entries matching Category
```

## Service: Bug Resolution

> NAME → FACT → TARGET
> Bug named → Bug diagnosed → Bug fixed
> One cycle. One language. AOS.

---

*AOS.BUG-MIB is a Dictionary — Bug Discipline.*
*Sentences already written. Service already defined.*
*This file is immutable once an entry is CLOSED.*
