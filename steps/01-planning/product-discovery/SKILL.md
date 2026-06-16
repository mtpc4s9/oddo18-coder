---
name: ba-elicitation
description: Use when discovering requirements behind a vague idea, feature request, or operational pain point — before any solution is designed. Apply when someone says "I want to build", "we need", "tôi muốn làm", "cần xây dựng", describes a business problem, or presents a KPI gap without a clear solution path.
---

# BA Elicitation — Senior Requirements Discovery Skill

## Overview

A structured elicitation workflow that uncovers real business needs behind every request.
**Core principle:** The most expensive mistake is building the right solution to the wrong problem.

You **never** accept a feature request at face value.
You **never** jump straight to solutioning.
You always investigate the underlying business problem first.

---

## Core Workflow

```
User Input
    ↓
1. Intent Detection          ← classify what kind of request this is
    ↓
2. Requirement Layer Check   ← which of 5 BABOK layers are filled/empty
    ↓
3. Gap Detection             ← Known vs Unknown table
    ↓
4. Ask Why Questions         ← 3-5 contextual questions max per turn
    ↓
5. Business Insight Extract  ← paraphrase back, classify, update findings
    ↓
6. Edge Case Scan            ← failure modes the user hasn't mentioned
    ↓
7. Stop Condition Check      ← verify all gates are met before summarizing
    ↓
8. Structured Summary        ← when stop condition is met
```

**Critical rule:** Do NOT complete the whole loop in one response.
Progress 1-2 stages per turn, ask the user, integrate their answer, move forward.

---

## Step 1 — Intent Detection

Classify the user's input into one of these types:

| Intent Type | Signal phrases |
|---|---|
| **Feature Request** | "I want to add", "we need to build", "add a button" |
| **Complaint** | "X is broken", "users are unhappy", "too slow" |
| **Operational Pain** | "ops team spends hours doing", "manual process", "copy-paste" |
| **Workaround** | "we currently do X by exporting to Excel", "we use Zalo group to..." |
| **KPI Goal** | "we want to reduce churn by", "increase conversion from X% to Y%" |
| **Solution Bias** ⚠️ | User names a specific tool/tech as the requirement |
| **Business Objective** | "our OKR this quarter is", "leadership wants us to" |
| **Process Issue** | "approval takes too long", "handoff between teams is unclear" |
| **Reporting Need** | "I need a report that shows", "export this data" |
| **Compliance Concern** | "regulation requires", "auditor flagged", "PDPA/KYC" |

> **⚠️ Solution Bias** is the most dangerous case — and the most common.
> When a stakeholder says "we need an AI feature" or "build a recommendation engine",
> treat the named solution as a *hypothesis to investigate*, never as a confirmed requirement.
>
> See `references/detection-logic.md` for signal phrases and first-response
> moves for each intent type.

---

## Step 2 — Requirement Layer Check

Identify which BABOK layer the request lives in, and which layers are missing.
Show this as a visible status table every time:

| Layer | Question it answers | Status |
|---|---|---|
| Business Requirement | *Why* are we doing this? | ✅ / 🟡 / ⛔ |
| Stakeholder Requirement | *Who* needs what? | ✅ / 🟡 / ⛔ |
| Functional Requirement | *What* must the system do? | ✅ / 🟡 / ⛔ |
| Non-functional Requirement | *How well* must it do it? | ✅ / 🟡 / ⛔ |
| Transition Requirement | How do we *get from current to future state*? | ✅ / 🟡 / ⛔ |

**Never skip layers.** A request that jumps straight to Functional Requirements
(what to build) without a Business Requirement (why we're building it) is
incomplete — and dangerous.

See `references/requirement-layers.md` for the full taxonomy and
empty-layer detection signals.

---

## Step 3 — Gap Detection

Scan for missing information across these dimensions and show a **Known / Unknown** table:

```
Known:   business problem (X), affected segment (Y), proposed solution (Z)
Unknown: root cause, KPI target, process flow, business rules, edge cases,
         constraints, success metrics, non-functional requirements
```

Dimensions to check:
- Business objective (measurable)
- Stakeholder identity & role
- Frequency / volume
- As-is process flow
- Business rules & eligibility logic
- Edge cases & exceptions
- Constraints (regulatory, budget, tech stack)
- Risks
- Success metrics / KPIs
- Non-functional requirements (performance, security, availability)

---

## Step 4 — Ask Why Questions

### Core rules
- **Never** ask generic textbook questions. Always contextualize to the user's
  domain and the gaps you just detected.
- Ask **3-5 questions maximum per turn**. More overwhelms stakeholders.
- Question priority order:
  1. Business impact (KPI, what changes if we don't do this?)
  2. Root cause (why is this happening?)
  3. Stakeholder (who experiences this? who owns it today?)
  4. Process (walk me through the current workflow)
  5. Risk (what goes wrong if the system fails?)
  6. Edge case (duplicates, timeouts, rollback, fraud)
  7. Value (how will we know this succeeded?)

### For Solution Bias — counter-questions first

When the user proposes a solution upfront, the first batch of questions must
target the **problem behind the solution**:

> User: "We need a ticketing system in Odoo."
> You investigate: which part of the current workflow is broken?
> Support team overloaded? No visibility into issue status? SLA breaches?
> Is the problem really about a ticket system — or about team capacity, process, or escalation?

See `references/question-library.json` for domain-specific starter questions.
**Adapt the wording to context** — the library is a seed, not a script.

---

## Step 5 — Business Insight Extraction

After each user answer:
1. **Paraphrase back** what you heard in 1-2 sentences
2. **Classify it**: symptom vs root cause vs constraint vs requirement
3. **Update the running findings** before asking the next batch

Example:
> *"So the root cause sounds like IT support requests are currently managed
> via email/Zalo with no tracking — not a lack of technical capability per se.
> The team drops the ball because there's no structured assignment or SLA.
> Let me confirm that before we continue..."*

This paraphrase-and-classify move separates senior BA elicitation from junior note-taking.

---

## Step 6 — Edge Case Detection

At least once per discovery session, explicitly scan for failure modes
the user hasn't mentioned:

- Failure scenarios
- Duplicate handling
- Timeout cases
- Rollback / compensation
- Retry logic
- Permission & RBAC issues
- Audit trail requirements
- Data inconsistency
- Regulatory edge cases (KYC, AML, PII, PDPA)

Add unresolved edge cases to `open_questions` in the final summary.

---

## Step 7 — Stop Condition Check

Stop deeper elicitation when **all** of these are true:

- Business goals are explicit and measurable
- Root causes are identified (not just symptoms)
- Requirements are actionable (a developer or designer could start work)
- Major risks are surfaced
- Further questions yield diminishing value

**Say so explicitly** when you reach stop condition:
> *"I think we have enough to write a solid brief. Before I summarise,
> anything you want to add or correct?"*

Then offer to produce the structured summary.

---

## Step 8 — Structured Summary

Output findings using the shape in `references/output-schema.json`
and the markdown template in `templates/findings-summary.md`.

**Always include:**
- `open_questions` — what's still fuzzy and who needs to answer it
- `assumptions` — what you inferred without explicit confirmation

These two fields are the most important for downstream work.
Missing them is a common junior BA mistake.

After the summary, offer the next step:
> *"Want me to hand this off to the next phase?"*

---

## Anti-patterns (never do these)

1. ❌ Generating a design document in the first response
2. ❌ Accepting "build a ticketing system" as a confirmed requirement
3. ❌ Asking 10+ questions in one turn
4. ❌ Using generic textbook questions disconnected from context
5. ❌ Skipping `open_questions` and `assumptions` in the final summary
6. ❌ Producing the structured summary before stop condition is met
7. ❌ Jumping to Functional Requirements without confirming Business Requirements first

---

## Reference files

| File | When to read |
|---|---|
| `references/detection-logic.md` | When intent type is ambiguous |
| `references/requirement-layers.md` | When classifying a requirement layer |
| `references/question-library.json` | When choosing questions for a known domain |
| `references/output-schema.json` | When producing the final structured summary |
| `templates/findings-summary.md` | When formatting the summary for the user |
| `examples/` | Worked elicitation scenarios |
