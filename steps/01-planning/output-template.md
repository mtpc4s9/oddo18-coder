# Odoo 18 Addon — Planning Output

> **Agent Instructions:**
> Fill all `[INSERT:...]` fields based on the completed discovery session (Phase 1) and technical analysis (Phase 2).
> - If a value is confirmed → fill it directly
> - If a value is still unknown → write `[TBD: <reason>]`
> - Never leave a field blank
> - Present this completed template to the user for confirmation before proceeding to 02-scaffold

---

## Section 1 — Project Identity

**Addon Technical Name:** [INSERT: Short Text | snake_case, no spaces, e.g. `it_ticketing` or `hr_overtime_request`]

**Addon Display Name:** [INSERT: Short Text | Human-readable, e.g. "IT Helpdesk Ticketing" or "HR Overtime Request"]

**Odoo Version:** 18.0

**Edition:** [INSERT: Select One | Community / Enterprise]

**Category:** [INSERT: Short Text | e.g. "Human Resources", "Services", "Accounting", "Technical" — must match Odoo official category list]

**Author / Maintainer:** [INSERT: Short Text | Name or team maintaining this addon]

---

## Section 2 — Business Context

**Business Problem:**
[INSERT: Multi-line | Describe the operational pain point or business gap this addon solves. 2-4 sentences.]

**Business Objective (Measurable):**
[INSERT: Multi-line | The specific, measurable goal. Format: "Reduce X from A to B by [date]" or "Enable Y process that currently takes Z minutes to be completed in under W minutes"]

**Success Metrics / KPIs:**
[INSERT: List | One KPI per line. E.g.:
- Average ticket resolution time < 24 hours
- Zero IT support requests lost (currently: ~20% tracked via email only)
]

---

## Section 3 — Stakeholders & Access

**Key Stakeholders:**

| Role | Department | Interest / Need |
|---|---|---|
| [INSERT: Role] | [INSERT: Dept] | [INSERT: What they need from this addon] |
| [INSERT: Role] | [INSERT: Dept] | [INSERT: What they need from this addon] |

**Odoo User Group Mapping:**

| Business Role | Odoo Group | Permissions (Summary) |
|---|---|---|
| [INSERT: Role, e.g. IT Manager] | `[module].group_manager` | [INSERT: e.g. Full access: create, read, edit, delete, approve] |
| [INSERT: Role, e.g. IT Staff] | `[module].group_user` | [INSERT: e.g. Create + read own records only] |
| [INSERT: Role, e.g. Employee (requester)] | `base.group_portal` or `[module].group_requester` | [INSERT: e.g. Submit tickets + view own status] |

---

## Section 4 — Feature Inventory

> Legend: 🔴 Core (v1 must-have) | 🟡 Nice-to-have (optional, add later) | ⚫ Out-of-scope

**Core Features (🔴 — must build in Step 02–09):**

| # | Feature | Description |
|---|---|---|
| FR-01 | [INSERT: Feature Name] | [INSERT: Short description of what the system must do] |
| FR-02 | [INSERT: Feature Name] | [INSERT: Short description] |
| FR-03 | [INSERT: Feature Name] | [INSERT: Short description] |

**Nice-to-have Features (🟡 — defer to `optional/` or future sprint):**

| # | Feature | Reason deferred |
|---|---|---|
| NTH-01 | [INSERT: Feature Name] | [INSERT: e.g. Low priority, not blocking v1 delivery] |

**Out-of-scope (⚫ — explicitly excluded, do not build):**

- [INSERT: Feature or system that is explicitly excluded, e.g. "Mobile app integration — use Odoo PWA instead"]
- [INSERT: ...]

---

## Section 5 — Technical Architecture Decision

### A. Core Module Relationship

| Feature Area | Core Module Candidate | Relationship |
|---|---|---|
| [INSERT: e.g. Ticketing] | [INSERT: e.g. `helpdesk`] | [INSERT: Select One | Inherit / Standalone (new model)] |
| [INSERT: e.g. Messaging] | `mail` | Inherit via `mail.thread` mixin |
| [INSERT: e.g. Tasks] | [INSERT: e.g. `project`] | [INSERT: Select One | Inherit / Standalone] |

### B. Final Inheritance Decision

**Decision:** [INSERT: Select One | Inherit from `<module_name>` / Build Standalone / Mixed (specify below)]

**Rationale:**
[INSERT: Multi-line | Explain why. Reference the pros/cons analysis from Phase 2. E.g.:
"Inherit from `helpdesk` because: (1) SLA & team assignment logic already built, (2) portal submission is native, (3) reduces development from ~15 models to ~3 extensions.
Cons accepted: requires Helpdesk module installed, but this is acceptable since client already uses it."]

### C. Estimated Scope

| Component | Count | Notes |
|---|---|---|
| `models.Model` (regular) | [INSERT: Number] | [INSERT: List model names if known] |
| `models.TransientModel` (wizards) | [INSERT: Number] | [INSERT: e.g. "Reject Reason popup"] |
| Main List Views | [INSERT: Number] | [INSERT: One per model minimum] |
| Main Form Views | [INSERT: Number] | [INSERT: One per model minimum] |
| OWL Components needed? | [INSERT: Select One | Yes → flag optional/owl-components / No] | [INSERT: Brief reason] |
| API Controller needed? | [INSERT: Select One | Yes → flag optional/api-controllers / No] | [INSERT: Brief reason] |

---

## Section 6 — Workflow & State Machine

> Fill this section ONLY if the addon has an approval flow or lifecycle states.

**State Machine:**

```
[INSERT: ASCII state diagram or text. Example:
Draft → [Submit] → Pending Approval → [Approve] → In Progress → [Resolve] → Done
                                    → [Reject]  → Rejected (end)
                 → [Cancel]         → Cancelled (end)
]
```

**Transition Rules:**

| From State | To State | Action | Who Can Trigger |
|---|---|---|---|
| [INSERT: State] | [INSERT: State] | [INSERT: Button/action name] | [INSERT: User group] |
| [INSERT: State] | [INSERT: State] | [INSERT: Button/action name] | [INSERT: User group] |

---

## Section 7 — Non-Functional Requirements

| NFR | Requirement |
|---|---|
| Performance | [INSERT: e.g. "List view must load < 2s for up to 10,000 records"] |
| Security | [INSERT: e.g. "Users can only see their own tickets; Managers see all"] |
| Availability | [INSERT: e.g. "Same as core Odoo uptime SLA"] |
| Data Retention | [INSERT: e.g. "Closed tickets archived after 2 years"] |
| Localization | [INSERT: e.g. "Vietnamese + English UI labels required"] |

---

## Section 8 — Open Questions & Assumptions

**Open Questions (must resolve before coding):**

| # | Question | Owner | Deadline |
|---|---|---|---|
| Q-01 | [INSERT: Unresolved question] | [INSERT: Person responsible to answer] | [INSERT: ISO Date or "Before 02-scaffold"] |
| Q-02 | [INSERT: Unresolved question] | [INSERT: Owner] | [INSERT: Deadline] |

**Assumptions Made:**

- [INSERT: Assumption confirmed without explicit user statement. E.g. "Assumed Enterprise edition — client mentioned Odoo Sign"]
- [INSERT: ...]

---

## Section 9 — Constraints

- [INSERT: Known constraint. E.g. "Must not add dependencies to modules not already installed on client server"]
- [INSERT: E.g. "Must follow company's existing security groups naming convention: `<addon>_group_<role>`"]
- [INSERT: ...]

---

## Section 10 — Handoff Confirmation

**User Confirmation Status:** [INSERT: Select One | ⏳ PENDING USER REVIEW / ✅ CONFIRMED — proceed to 02-scaffold]

**Confirmed by:** [INSERT: Short Text | User name or "User (chat)"]

**Date Confirmed:** [INSERT: ISO Date | YYYY-MM-DD]

> **Agent Note:** Do NOT proceed to `02-scaffold` until this field shows `✅ CONFIRMED`.
