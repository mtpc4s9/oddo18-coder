---
artifact_name: Odoo Addon Planning Output
purpose: >
  Capture confirmed requirements from the product-discovery session
  and translate them into Odoo 18 technical decisions.
  This output serves as the mandatory input for step 02-scaffold.
feeds_into: steps/02-scaffold/SKILL.md
requires_confirmation: true
---

### 🤖 AGENT DIRECTIVE

**Processing Steps — MUST execute BEFORE generating the output:**

1. **Load Discovery Output:** Read the results from the product-discovery session (including the feature list, user roles, and priority tiers: Core 🔴, Nice-to-have 🟡, Out-of-scope ⚫).
2. **Inheritance Analysis:** For each Core feature, check if Odoo 18 has existing core modules (e.g., `helpdesk`, `project`, `sale`, `account`, `mail`) that cover all or part of the functionality. Always prioritize extending/inheriting Odoo core modules before proposing custom models from scratch.
3. **Expose Key Decisions (VISIBLE TO USER — Requires Approval):**
   Before generating the final output, present a summary of the following decisions to the user for explicit confirmation:
   - Technical addon name (e.g., `addon_technical_name`)
   - Inheritance vs. Standalone (from scratch) decisions with detailed reasoning
   - Expected technical dependencies (the `depends[]` list)
   - Estimated number of custom models to be created
4. **Await User Confirmation:** Pause and wait for the user to confirm the exposed decisions before proceeding to fill out the Technical Specification sections below.
5. **Output Generation:** Once the user approves the key decisions, populate the Planning Output template below in full. Keep any background reasoning in a collapsible `<details><summary>Agent Reasoning</summary>...</details>` section to keep the main output clean.

---

## 📋 PLANNING OUTPUT

### 1. Addon Identity
- **Display Name:** [INSERT: Display Name (e.g., IT Helpdesk Ticketing)]
- **Technical Name:** [INSERT: Technical Name (snake_case, e.g., `it_ticketing`)]
- **Version:** 18.0.1.0.0
- **Author / License:** [INSERT: Author Name / License (e.g., LGPL-3)]
- **Odoo Edition & Category:** [INSERT: Select One | Community / Enterprise] — Category: [INSERT: Short Text | e.g. "Services", "Human Resources"]

### 2. Inheritance Decision
| Module Odoo 18 | Relation | Rationale |
|----------------|----------|-----------|
| [INSERT: Module Name (e.g., `helpdesk`)] | [INSERT: inherit / extend / none] | [INSERT: Detailed pros/cons of inheritance vs. standalone] |
| [INSERT: Module Name (e.g., `mail`)] | [INSERT: inherit / extend / none] | [INSERT: e.g., Inherited for chatter tracking via mail.thread] |

### 3. Core Features (confirmed)
| Feature ID | Feature Description | Model Strategy | Est. Complexity |
|------------|---------------------|----------------|-----------------|
| FR-01 | [INSERT: Feature name & goal] | [INSERT: e.g., Inherit helpdesk.ticket / New it.ticket] | [INSERT: Low / Medium / High] |
| FR-02 | [INSERT: Feature name & goal] | [INSERT: e.g., Inherit helpdesk.ticket / New it.ticket] | [INSERT: Low / Medium / High] |

### 4. User Roles & Permissions
| Role Name | Access Level | Domain / Constraints |
|-----------|--------------|----------------------|
| [INSERT: e.g., IT Manager] | [INSERT: read/write/create/delete] | [INSERT: e.g., Full access to all tickets] |
| [INSERT: e.g., Employee] | [INSERT: read/create/write (own)] | [INSERT: e.g., Can only see/edit tickets they created] |

### 5. Technical Dependencies (expected)
```python
# Agent will finalize this list after using 02-scaffold/dependency-matrix.md
depends = [
    'base',
    'mail',
    # [INSERT: Other dependent modules, e.g., 'helpdesk', 'project']
]
```

### 6. Out-of-scope (explicitly excluded)
- **Feature/System:** [INSERT: E.g., Mobile app integration]
  - *Reason for exclusion:* [INSERT: E.g., Out of scope for v1, Odoo web client is mobile responsive]
- **Feature/System:** [INSERT: ...]
  - *Reason for exclusion:* [INSERT: ...]

---

<details>
<summary>🔍 Agent Reasoning</summary>

[INSERT: Detailed technical notes, gap analysis, and system flow explanation for the developer's review. This section does not form part of the final addon code but documents the LLM's architecture design thoughts.]

</details>

---

## 🚦 Handoff Confirmation
- **Status:** [INSERT: Select One | ⏳ AWAITING USER CONFIRMATION / ✅ CONFIRMED — Proceed to 02-scaffold]
- **Confirmed By:** [INSERT: User Name / Chat Confirmation]
- **Date Confirmed:** [INSERT: YYYY-MM-DD]
