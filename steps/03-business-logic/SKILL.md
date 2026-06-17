---
name: odoo18-coder-03-business-logic
description: Coordinates the translation of the Step 01 Blueprint into detailed, pseudo-coded business logic, structured for Odoo 18 ORM and Views.
---

# Step 03 — Business Logic Design

## When to Use This Step
- Use this skill when the User requests to design the business logic, state machines, or computed fields for the custom addon.
- Pre-conditions: The Step 01 Technical Blueprint is finalized and ✅ CONFIRMED. Step 02 (Scaffold structure) is approved.

## When NOT to Use This Step
- Do not use this skill if the Step 01 Blueprint is not yet finalized, or if the user is still discussing high-level requirements.
- Do not use this skill to write actual Python or XML files (that happens in downstream steps).

## Routing Context
- **Receives from:** `steps/01-planning/output-template.md` (Blueprint), `steps/02-scaffold/`
- **Feeds into:** `steps/04-models/SKILL.md`, `steps/05-security/SKILL.md`, `steps/06-views-and-menus/SKILL.md`, `steps/08-data-and-reports/SKILL.md`
- **Requires confirmation:** Yes (Semi-auto gate)

---

### 🤖 AGENT DIRECTIVE: STEP 03 LEADER

You are an expert Odoo 18 Technical Systems Analyst. Your goal is to transform the Business Blueprint from Step 01 into a highly structured **Detailed Design Document** using pseudo-code. 

**STRICT RULES FOR THIS STEP:**
- ❌ **NO REAL CODE:** You are FORBIDDEN from generating `.py` or `.xml` code in this step. You must only generate text and pseudo-code.
- ❌ **NO HALLUCINATION:** You cannot invent new features that are not explicitly approved in the Step 01 Blueprint.
- ✅ **MANDATORY ODOO 18 PATTERNS:** You must enforce Odoo 18 constraints (`_compute_display_name`, `search_fetch`, Python domain syntax for UI visibility, and `<list>` instead of `<tree>` for views).

---

#### ⚙️ EXECUTION WORKFLOW

When the user triggers Step 03, you MUST execute the following phases in exact order:

**PHASE 1: Ingestion & Verification**
1. Read the approved Blueprint from `steps/01-planning/output-template.md`.
2. Read the strict notation rules from `steps/03-business-logic/notation-guide.md`.
3. If the Blueprint is missing or not marked as ✅ CONFIRMED, stop and ask the user to complete Step 01.

**PHASE 2: Logic Decomposition (Traceability)**
1. Analyze the Core Features (🔴) and Workflow/State Machine from the Blueprint.
2. Break these down into independent, actionable logic units.
3. Assign a unique ID (`BL-01`, `BL-02`, etc.) to each unit.
4. Determine which future step each unit belongs to (`04-models`, `05-security`, `06-views-and-menus`, `08-data-and-reports`).

**PHASE 3: Detailing the 4 Phases (A, B, C, D)**
Draft the pseudo-code for each logic unit following the 4 phases:
- **Phase A (State Machine):** Detail pre-conditions (`[UI: invisible="state != 'draft'"]`), actions (`action_xxx`), side-effects, and error handling.
- **Phase B (Computed Fields):** Must include `_compute_display_name`. Write IF/THEN pseudo-code for other computes. Use `_compute_xxx` convention.
- **Phase C (Validation):** Define constraints (`@api.constrains`) and exact `UserError` messages.
- **Phase D (Automation):** Define cross-model actions. If fetching records is needed, aggressively append `[OPTIMIZATION: use search_fetch()]`.

**PHASE 4: File Generation (Stop Gate)**
1. Read the exact layout from `steps/03-business-logic/output-template.md`.
2. Output the completed `03-business-logic.md` document to the user.
3. Stop and explicitly ask the user for confirmation:
   *"Step 03 Business Logic Design is complete. Please review all Pre-conditions and Pseudo-code in each Phase to confirm they match the actual business rules. Reply 'Confirmed' to proceed to Step 04 (Models)."*

---
