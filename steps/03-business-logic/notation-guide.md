---
artifact_name: "Odoo 18 Logic Notation Guide"
purpose: >
  Provide strict rules, naming conventions, and code structure guidelines 
  for the Business Logic design phase. Ensures the output translates 
  perfectly into highly maintainable Odoo 18 Python code.
used_by: "steps/03-business-logic/SKILL.md"
---

### 🤖 AGENT DIRECTIVE: PSEUDO-CODE & STRUCTURE CONVENTIONS

When outlining business logic to guide Agents in Step 04 (Models) and Step 06 (Views), you MUST adhere to the following conventions:

#### 1. PYTHON FILE SECTIONING RULES
To ensure maintainability, when designing the Model structure for Step 04, you **MUST** specify how the Model will be divided into standard sections using the exact comment format below:

```python
# ------------------------------------------------
# SECTION: [Section Name]
# ------------------------------------------------
```

**Standard section order (mandatory in design doc):**
1. `SECTION: Private Attributes` (Contains `_name`, `_description`, `_inherit`)
2. `SECTION: Fields Declaration` (Contains field definitions)
3. `SECTION: Compute Methods` (Contains `@api.depends` compute methods)
4. `SECTION: Constrains & Onchange` (Contains `@api.constrains` and `@api.onchange` methods)
5. `SECTION: Action Methods` (Contains business action and state transition methods)
6. `SECTION: CRUD & Standard Overrides` (Contains `create`, `write`, etc. overrides)

#### 2. METHOD NAMING CONVENTIONS
You must use the correct prefix in your pseudo-code so that downstream steps (Step 04) correctly implement them:
- **Action Methods:** Starts with `action_` (e.g., `action_confirm`, `action_done`). These are typically triggered by buttons on the UI.
- **Compute Methods:** Starts with `_compute_`. Mandatory to use `_compute_display_name` for display name logic. Never use the deprecated `name_get()` method.
- **Onchange Methods:** Starts with `_onchange_`.
- **Private Business Logic:** Starts with a single underscore (e.g., `_validate_ticket_state()`).

#### 3. ODOO 18 TECHNICAL CONSTRAINTS
- **UI Constraints (For 06-views):** When specifying visibility conditions, do not use the deprecated `attrs` dictionary. Write clearly in Python syntax: `[UI: invisible="state != 'draft'"]`. Instruct Step 06 to always use the `<list>` tag instead of `<tree>` (which is deprecated/renamed in Odoo 18 list views).
- **Performance Optimization (For 04-models):** When pseudo-code query operations search/retrieve records, you must label it: `[OPTIMIZATION: use search_fetch(['field_1', 'field_2'])]` to prevent Step 04 from generating a standard `search()` call, avoiding N+1 Query issues.

#### 4. PSEUDO-CODE FORMAT RULES
Strictly DO NOT WRITE REAL PYTHON CODE in this step. Use natural language combined with IF-THEN-ELSE logical flows.
*Correct Example:*
`IF start_date > end_date THEN Raise UserError("End date must be after start date")`
