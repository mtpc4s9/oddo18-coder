---
artifact_name: "Odoo 18 Business Logic Design"
purpose: >
  "Expand the Planning Blueprint into detailed pseudo-code and state machine logic.
  This file serves as the strict logic foundation for Model, View, and Security generation."
feeds_into: "steps/04-models/SKILL.md, steps/05-security/SKILL.md, steps/06-views-and-menus/SKILL.md"
---

### 🤖 AGENT DIRECTIVE (HIDDEN FROM FINAL OUTPUT)
**Processing Rules — MUST execute BEFORE generating the output:**
1. **NO REAL CODE:** Output ONLY plain text, pseudo-code, and structured tables. Do NOT write actual Python (`.py`) or XML (`.xml`) code.
2. **ODOO 18 NAMING CONVENTIONS:** 
   - State transition actions must use `action_xxx()`.
   - Compute methods must use `_compute_xxx()`.
   - **MANDATORY:** Always use `_compute_display_name` for display name logic. Never use `name_get`.
3. **LOGIC ID TRACEABILITY:** Every piece of logic designed in Phases A, B, C, D MUST be registered in the "0. Logic Routing Matrix" first, assigning it a unique `BL-XX` ID.
4. **ODOO 18 UI CONSTRAINTS:** When defining UI conditions, remind Step 06 to use Python syntax for domains (e.g., `[UI: invisible="state != 'draft'"]`). Do NOT use `attrs`.

---
**(START OF OUTPUT GENERATED TO USER)**
---

# 🧠 BUSINESS LOGIC DESIGN: "[INSERT: addon_technical_name]"

## 0. Logic Routing Matrix (Traceability)
*This routing matrix helps downstream steps (Models, Security, Views) identify exactly which logic they need to read and implement.*

| Logic ID | Business Description | → Feeds into (Execution Target) |
| :--- | :--- | :--- |
| `[e.g., BL-01]` | `[e.g., Constraint: end date cannot be earlier than start date]` | `[e.g., → 04-models (@api.constrains)]` |
| `[e.g., BL-02]` | `[e.g., action_close button can only be clicked by Manager group]` | `[e.g., → 05-security (ir.rule / groups)]` |
| `[e.g., BL-03]` | `[e.g., Close button is hidden when state is not draft]` | `[e.g., → 06-views (invisible attr)]` |
| `[INSERT: ID]` | `[INSERT: Description]` | `[INSERT: Target Step]` |

---

## Phase A — State Machine Detail (Drill-down from Blueprint)
*Detailed record life-cycle. The Logic ID column maps to the Routing Matrix above.*

| Logic ID | Transition (A → B) | Action Triggered | Pre-condition (Before execution) | Side-effects / Error Handling |
| :--- | :--- | :--- | :--- | :--- |
| `[BL-xx]` | `[Draft → Confirmed]` | `[action_confirm]` | `[UI: invisible="state != 'draft'"]` | `[Sets confirmed_date = today]` |

## Phase B — Computed Fields Logic
*Fields calculated automatically based on dependent fields.*

*   **Logic ID:** `[BL-xx]`
    *   **Field:** `display_name` (Mandatory Odoo 18 standard)
    *   **Depends on (`@api.depends`):** `[name, reference_code]`
    *   **Logic (`_compute_display_name`):** `[return "[reference_code] name"]`

*   **Logic ID:** `[BL-xx]`
    *   **Field:** `[field_name]`
    *   **Logic (`_compute_[field_name]`):**
        ```text
        // Pseudo-code
        IF [condition] THEN [field] = [value]
        ```

## Phase C — Validation Rules (@api.constrains)
*Data validation rules (Model Constraints).*

| Logic ID | Fields to Validate | Invalid Condition | Error Message (UserError) |
| :--- | :--- | :--- | :--- |
| `[BL-xx]` | `[start_date, end_date]` | `[end_date < start_date]` | `["End date cannot be earlier than start date!"]` |

## Phase D — Cross-model & Automation Logic
*Background actions and automated tasks.*

*   **Logic ID:** `[BL-xx]`
    *   **Automation:** `[Feature Name]`
    *   **Trigger / Target:** `[On State Change] / [Target Model]`
    *   **Action:** `[e.g., Create record / Send Email]`
    *   **Optimization:** `[e.g., [OPTIMIZATION: use search_fetch()]]`
