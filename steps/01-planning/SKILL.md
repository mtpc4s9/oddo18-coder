---
name: odoo18-coder-01-planning
description: Use when starting any new Odoo 18 custom addon — from a vague idea, feature request, or operational pain point — before any scaffold or code is written. Triggers when user says "tôi muốn làm module", "cần xây dựng addon", "có ý tưởng về odoo", "cần tính năng X trong odoo", or describes a business problem that Odoo doesn't yet solve.
---

# Step 01 — Planning & Discovery

## When to Use This Step
- Use this skill when starting a brand new Odoo 18 custom addon development process.
- Triggers when the user expresses a new idea, feature request, or describes a business problem requiring Odoo customization.

## When NOT to Use This Step
- Do not use this skill if the high-level Technical Blueprint is already finalized and confirmed.
- Do not use this skill for downstream phases (scaffolding, database design, view creation, security rules) without a confirmed design.

## Routing Context
- **Receives from:** Initial User request
- **Feeds into:** `steps/02-scaffold/SKILL.md`, `steps/03-business-logic/SKILL.md`
- **Requires confirmation:** Yes (Semi-auto gate)

---

## Phase 1 — Discovery (Delegate to Sub-Skill)

### Action

Open an **AI-to-User interview session**. Announce this explicitly:

> *"I will open a requirement discovery interview session. Please present your idea, and I will ask questions step-by-step to clarify."*

### Loading Instructions

**REQUIRED — Read in this order:**
1. Read `./discovery-wrapper.md` FIRST — defines which questions to skip, which to rephrase, and how to classify features in Odoo context
2. Then follow `./product-discovery/SKILL.md` workflow (Steps 1 → 8)
3. Apply all constraints from `./discovery-wrapper.md` throughout the entire session

### Interview Protocol

- Conduct the interview turn-by-turn (1-2 steps per response, then ask)
- Do NOT rush through all 8 steps in one response
- Vietnamese or English — match the user's language

### Stop Gate 1 ✅

Discovery session is complete when ALL of the following BABOK layers are at minimum 🟡:

| Layer | Minimum Gate |
|---|---|
| Business Requirement (Why?) | 🟡 Partially confirmed |
| Stakeholder Requirement (Who?) | 🟡 Key users identified |
| Functional Requirement (What?) | 🟡 Feature list drafted |

Once Stop Gate 1 is reached → proceed to Phase 2.

---

## Phase 2 — Odoo Technical Analysis (Local)

### Action

After Phase 1, perform **internal analysis** WITHOUT asking the user more questions.
Present findings as a structured brief at the end of this phase.

### A. Core Module Mapping

Scan Odoo 18 core modules for feature overlap:

| Core Module | Covers |
|---|---|
| `helpdesk` | Ticketing, SLA, team assignment, portal submission |
| `project` | Task management, milestones, kanban, timesheets |
| `mail` | Chatter (`mail.thread`), followers, activity scheduling |
| `hr` | Employee, department, job position |
| `sale` | Customer, quotation, order |
| `account` | Invoice, payment, journal entries |
| `website` | Public portal, e-commerce, contact form |
| `purchase` | Vendor, RFQ, PO |
| `stock` | Inventory, warehouse, picking |
| `mrp` | Manufacturing, BoM, work orders |

### B. Inheritance Decision

For **each identified feature area**, analyze:

**Option A — Inherit existing model**
```python
# Example: extend helpdesk.ticket
_inherit = 'helpdesk.ticket'
```
| Pros | Cons |
|---|---|
| Minimal code, leverages native Odoo features | Requires core module to be installed |
| Inherits chatter, followers, activity, portal automatically | Upgrade path tied to core module |
| Native integration with Reports, Search, Filters | Cannot easily override deeply nested business logic |
| Faster to build, less security setup needed | May carry unwanted fields from parent model |

**Option B — New model from scratch**
```python
# Example: brand new model
_name = 'it_ticketing.ticket'
_inherit = ['mail.thread', 'mail.activity.mixin']
```
| Pros | Cons |
|---|---|
| Full control over fields, logic, UX | Must rebuild everything (sequence, chatter, security) |
| No dependency on installing another core module | More code = more maintenance surface |
| Domain is clean, no "inherited noise" | More security setup required (ir.model.access.csv) |

**Decision Rule:**
- Default to **Inherit** when the feature domain closely matches an existing module (e.g., IT ticketing → extend `helpdesk`)
- Choose **New Model** only when the domain is fundamentally different and no core module is even partially relevant

### C. Rough Estimation

After the analysis, estimate:
- Number of new `models.Model` (regular models)
- Number of new `models.TransientModel` (wizards/popups)
- Number of main views (list + form minimum per model)
- OWL component needed? → flags `optional/owl-components` for later
- API controller needed? → flags `optional/api-controllers` for later

### Stop Gate 2 ✅

Before proceeding to Phase 3, present the technical analysis summary to the user:
> *"Here is the technical analysis summary. Please review and provide any feedback before the output template is filled."*

---

## Phase 3 — Output & Handoff

### Action

Fill `./output-template.md` completely using all findings from Phases 1 and 2.

### Rules
1. Every `[INSERT:...]` field must be filled — if genuinely unknown, write `[TBD: <reason why unknown>]`
2. Present the completed template to user for review
3. **User must explicitly confirm** (e.g., "Confirmed", "OK", "Đồng ý") before this step is complete
4. Do NOT generate any code, scaffold, or file structure in this step

### Handoff

The completed `output-template.md` is the **single input artifact** for `02-scaffold`.
Attach it to the handoff message:
> *"Step 01 complete. The confirmed Blueprint is ready. Trigger Step 02 whenever ready."*

---

## Constraints (Global for this step)

- ❌ Never generate Python, XML, or CSV code in this step
- ❌ Never assume or guess the module name without user input
- ❌ Never skip user confirmation at Phase 3
- ❌ Never proceed to 02-scaffold without a confirmed output-template
- ✅ Always present inheritance pros & cons — never just recommend without reasoning
- ✅ Always match user's language (Vietnamese / English)
