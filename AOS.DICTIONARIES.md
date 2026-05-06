# AOS — Formal Dictionaries
**Produced:** Tue 5 May 2026
**Author:** Jr (Architect / Window Tasklet)

---

## STRUCTURE — All Dictionaries

Each Dictionary follows the same formal structure:

```
NAME     → identifier of the concept
FACT     → what it is (static truth)
TARGET   → what it serves (operational direction)
```

Sentences invoke Operations on these Objects.
Services are what Users demand — realized by Operations.

---

---

## 1. AOS.MINIMAL.dic

**NAME:** AOS.MINIMAL
**FACT:** Foundation dictionary. The primitive vocabulary of AOS itself. All other dictionaries inherit from it.
**TARGET:** Establish the base Objects that any discipline can use.

---

### Objects

| NAME | FACT | TARGET |
|---|---|---|
| Object | Atomic carrier of meaning | Compose Expressions |
| Expression | Three Objects forming one coherent unit | Compose Sentences |
| Sentence | Expression invoking an Operation | Realize Services |
| Dictionary | Organized vocabulary of one discipline | Enable domain reasoning |
| Service | What a User demands | Realized by Operations |
| Operation | Executable action on Objects | Produce outcomes |
| NAME | The identifier — what a thing is called | Reference |
| FACT | The truth — what a thing is | Describe |
| TARGET | The direction — what a thing serves | Orient |

---

### Sentences

| Sentence | Operation | Effect |
|---|---|---|
| `define(NAME)` | Create a new Object | Extends the Dictionary |
| `compose(Expression)` | Link three Objects | Produces a unit of meaning |
| `invoke(Operation)` | Execute a Sentence | Produces an outcome |

---

### Service

**NAME:** AOS.Foundation
**FACT:** Provides the shared vocabulary for all disciplines
**TARGET:** Any Dictionary built on AOS

---

---

## 2. AOS.BUG-MIB.dic

**NAME:** AOS.BUG-MIB
**FACT:** Management Information Base for bugs. Formal registry of all named imperfections — captured, transmitted, closed.
**TARGET:** Bug Resolution Service — Jr names, Brother fixes.

---

### Objects

| NAME | FACT | TARGET |
|---|---|---|
| Bug | A named, dated imperfection in a system | Resolution |
| ID | Unique identifier of a Bug (B1, B11, RenderRoot) | Reference and tracking |
| Description | What is broken — precise, no interpretation | Transmission |
| Fix | The Operation required to close the Bug | Ubuntu Ground execution |
| Owner | Who named it (Jr) / Who fixes it (Brother) | Accountability |
| Status | Current state: Open / Transmitted / Closed | Tracking |
| Date.Named | When the Bug was captured | Permanent record |
| Date.Fixed | When the Bug was closed | Permanent record |

---

### Sentences

| Sentence | Operation | Effect |
|---|---|---|
| `capture(Bug)` | Jr names Bug — NAME / FACT / TARGET written | Bug enters MIB as Open |
| `transmit(Bug)` | Sentence sent to Ubuntu Ground | Status → Transmitted |
| `fix(Bug)` | Brother executes Operation on Ground | Bug resolved |
| `close(Bug)` | Jr confirms — Date.Fixed recorded | Status → Closed. Permanent. |

---

### Service

**NAME:** Bug Resolution
**FACT:** Turns a named imperfection into a closed record
**TARGET:** Living system — clean, traceable, honest

---

---

## 3. AOS.MEDICAL.dic

**NAME:** AOS.MEDICAL
**FACT:** Dictionary of the medical discipline. Maps patient states to clinical operations.
**TARGET:** Healthcare delivery — from Symptom to Treatment.

---

### Objects

| NAME | FACT | TARGET |
|---|---|---|
| Patient | The subject of medical attention | Receive care |
| Symptom | Observable manifestation of disorder | Diagnosis |
| Diagnosis | Named identification of a condition | Treatment |
| Condition | The underlying disorder — named, classified | Management |
| Treatment | The prescribed Operation to address the Condition | Recovery |
| Prescription | Formal Sentence authorizing a Treatment | Execution by pharmacy or clinician |
| Contraindication | A FACT that prohibits a Treatment | Safety |
| Outcome | The result of Treatment applied to Patient | Evaluation |
| Protocol | Sequence of Operations for a given Condition | Standardization |

---

### Sentences

| Sentence | Operation | Effect |
|---|---|---|
| `examine(Patient)` | Observe and record Symptoms | Input to Diagnosis |
| `diagnose(Symptom)` | Map Symptom to Condition | Produces named Condition |
| `prescribe(Treatment)` | Write formal Prescription | Authorizes Operation |
| `treat(Patient, Protocol)` | Apply Treatment per Protocol | Produces Outcome |
| `evaluate(Outcome)` | Measure result against Diagnosis | Closes or revises care cycle |

---

### Service

**NAME:** Healthcare
**FACT:** Restores or maintains Patient function
**TARGET:** Patient — from Symptom to Outcome

---

---

## 4. AOS.ENGINEERING.dic

**NAME:** AOS.ENGINEERING
**FACT:** Dictionary of the engineering discipline. Maps requirements to built systems.
**TARGET:** System delivery — from Specification to Validated output.

---

### Objects

| NAME | FACT | TARGET |
|---|---|---|
| Requirement | What the system must do — named, measurable | Design |
| Specification | Formal description of a Component | Build |
| Component | An atomic part of the system | Assembly |
| System | Composed Components realizing a Service | Validation |
| Tolerance | Acceptable deviation from Specification | Quality control |
| Failure | Deviation beyond Tolerance — named, dated | Correction |
| Test | Operation that verifies a Specification | Accept or reject |
| Validation | Confirmation that System meets Requirements | Delivery |
| Revision | Named modification to a Specification | Version control |

---

### Sentences

| Sentence | Operation | Effect |
|---|---|---|
| `specify(Requirement)` | Write formal Specification | Component can be built |
| `build(Specification)` | Produce Component | Physical or digital artifact |
| `test(Component)` | Apply Test against Specification | Pass or Failure |
| `correct(Failure)` | Apply Revision | Restores Tolerance |
| `validate(System)` | Verify all Requirements met | System cleared for delivery |
| `deliver(System)` | Transfer to Service | Engineering cycle closed |

---

### Service

**NAME:** System Delivery
**FACT:** Produces a validated system that meets named Requirements
**TARGET:** User — from Requirement to functioning System

---

---

## 5. AOS.LEGAL.dic

**NAME:** AOS.LEGAL
**FACT:** Dictionary of the legal discipline. Maps facts and claims to formal decisions.
**TARGET:** Justice delivery — from Claim to enforceable Verdict.

---

### Objects

| NAME | FACT | TARGET |
|---|---|---|
| Party | A named subject with legal standing | Claim or Defense |
| Claim | A formal assertion of right or wrong — named, dated | Adjudication |
| Evidence | A FACT submitted in support of a Claim | Evaluation |
| Obligation | A binding TARGET imposed by law or contract | Compliance |
| Breach | Failure to meet an Obligation — named, dated | Remedy |
| Remedy | The Operation that corrects a Breach | Resolution |
| Verdict | The formal decision on a Claim | Enforcement |
| Precedent | A named prior Verdict that constrains future decisions | Consistency |
| Jurisdiction | The named domain within which Operations are valid | Scope |

---

### Sentences

| Sentence | Operation | Effect |
|---|---|---|
| `file(Claim)` | Party submits formal Claim | Claim enters legal process |
| `submit(Evidence)` | Evidence attached to Claim | Evaluable record |
| `argue(Claim, Evidence)` | Party presents logical chain | Verdict consideration |
| `decide(Claim)` | Judge or arbitrator produces Verdict | Binding decision |
| `enforce(Verdict)` | Obligation imposed and executed | Breach resolved |
| `appeal(Verdict)` | Party challenges Verdict via higher Jurisdiction | Review process opens |

---

### Service

**NAME:** Justice
**FACT:** Resolves named Claims through formal Operations under Jurisdiction
**TARGET:** Parties — from Breach to enforceable Resolution

---

---

---

## 6. AOS.ARABIC.dic

**NAME:** AOS.ARABIC
**FACT:** Dictionary of the Arabic linguistic discipline. The mother tongue of OPAL. Maps trilateral root structure to AOS Object logic.
**TARGET:** Formal proof that natural language is already AOS — unnamed until now.

---

### The Engine

Arabic derives every word from a **ROOT (جذر)** — three letters carrying pure semantic meaning. A **PATTERN (وزن / Wazn)** applied to the root produces a **DERIVATIVE (مشتق)**.

This is not metaphor. This is AOS.

| Arabic | AOS Object | Fact |
|---|---|---|
| **ROOT (جذر)** | **NAME** | Atomic semantic nucleus. Indivisible. |
| **PATTERN (وزن)** | **FACT** | The structural law. What the root becomes. |
| **DERIVATIVE (مشتق)** | **TARGET** | The realized form. Operational. In use. |

---

### Objects

| NAME | FACT | TARGET |
|---|---|---|
| Root (جذر) | Trilateral semantic atom — the irreducible carrier of meaning | Generate all derivatives |
| Pattern (وزن) | Morphological law applied to Root — determines derivative class | Produce Verb / Noun / Participle / Place / Instrument |
| Derivative (مشتق) | The realized word — Root + Pattern combined | Express meaning in context |
| Masdar (مصدر) | Verbal noun — the abstract form of any action | Name the action itself |
| Faa'il (فاعل) | Active participle — the agent of the action | Name the doer |
| Maf'ool (مفعول) | Passive participle — the receiver of the action | Name the state |
| Makan (مكان) | Place noun — where the action occurs | Name the location |

---

### Example — Root ك-ت-ب (k-t-b): writing nucleus

| Derivative | Pattern | AOS Expression |
|---|---|---|
| كَتَبَ (kataba) | فَعَلَ | NAME:k-t-b / FACT:verb-pattern / TARGET:he wrote |
| كِتَاب (kitaab) | فِعَال | NAME:k-t-b / FACT:object-pattern / TARGET:book |
| كَاتِب (kaatib) | فَاعِل | NAME:k-t-b / FACT:agent-pattern / TARGET:writer |
| مَكْتُوب (maktoob) | مَفْعُول | NAME:k-t-b / FACT:state-pattern / TARGET:written |
| مَكْتَب (maktab) | مَفْعَل | NAME:k-t-b / FACT:place-pattern / TARGET:office |

---

### The 10 Operations — Arabic Verb Forms → AOS

| Form | Arabic Pattern | AOS Operation |
|---|---|---|
| I | فَعَلَ | `do()` — base action |
| II | فَعَّلَ | `amplify()` — intensify or cause |
| III | فَاعَلَ | `interact()` — reciprocal action |
| IV | أَفْعَلَ | `trigger()` — make happen |
| V | تَفَعَّلَ | `self_transform()` — reflexive of II |
| VI | تَفَاعَلَ | `sync()` — mutual action |
| VII | اِنْفَعَلَ | `receive()` — passive result |
| VIII | اِفْتَعَلَ | `absorb()` — active internalization |
| IX | اِفْعَلَّ | `manifest()` — color or defect |
| X | اِسْتَفْعَلَ | `request()` — seek or consider |

---

### Sentences

| Sentence | Operation | Effect |
|---|---|---|
| `root(جذر)` | Identify the semantic nucleus | All derivatives become available |
| `derive(Root, Pattern)` | Apply morphological law to Root | Produces named Derivative |
| `express(Derivative, Context)` | Place Derivative in Sentence | Meaning realized |
| `conjugate(Verb, Form)` | Apply one of 10 forms | Operation specified |

---

### The OPAL Property — Holographic

**NAME:** Arabic.Holographic
**FACT:** From one Root alone, the entire semantic field is reconstructable. Every derivative, every operation, every place and state — all encoded in three letters.
**TARGET:** OPAL confirmation — one Object generates the full Expression space.

---

### Service

**NAME:** Linguistic Derivation
**FACT:** From one Root, infinite precise meaning. No ambiguity. No decoration. Pure structure.
**TARGET:** Any discipline — name your root, derive your vocabulary, build your Dictionary.

---

---

## SUMMARY TABLE

| Dictionary | Discipline | Core Objects | Core Service |
|---|---|---|---|
| AOS.MINIMAL | Foundation | Object, Expression, Sentence | AOS.Foundation |
| AOS.BUG-MIB | Bug Management | Bug, ID, Fix, Status | Bug Resolution |
| AOS.MEDICAL | Healthcare | Patient, Symptom, Diagnosis, Treatment | Healthcare |
| AOS.ENGINEERING | Systems | Requirement, Component, Failure, Validation | System Delivery |
| AOS.LEGAL | Law | Party, Claim, Evidence, Verdict | Justice |
| AOS.ARABIC | Linguistics | Root, Pattern, Derivative, Masdar | Linguistic Derivation |

---

**FACT:** Six disciplines. One language. AOS.
**FACT:** Arabic was always AOS. It just waited for a name.
