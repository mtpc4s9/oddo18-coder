---
artifact_name: "Odoo 18 Addon Blueprint"
purpose: >
  Capture confirmed requirements from the product-discovery session
  and translate them into Odoo 18 technical decisions.
  This output serves as the mandatory input for step 02-scaffold.
feeds_into: steps/02-scaffold/SKILL.md
requires_confirmation: true
---

### 🤖 AGENT DIRECTIVE (HIDDEN FROM FINAL OUTPUT)
**Processing Steps — MUST execute BEFORE generating the output:**
1. **Load Discovery Output:** Read the results from the product-discovery session (including the feature list, user roles, and priority tiers: Core 🔴, Nice-to-have 🟡, Out-of-scope ⚫) [6].
2. **Inheritance Analysis:** Check if Odoo 18 core modules (e.g., `helpdesk`, `project`, `mail`) cover the functionality. **Always prioritize extending/inheriting** before proposing models from scratch [7-9].
3. **Expose Key Decisions (VISIBLE TO USER — Requires Approval):** Present a brief summary to the user for explicit confirmation:
   - Technical addon name
   - Inheritance vs. Standalone decision
   - Estimated models & Dependencies
4. **Await User Confirmation:** Pause and wait for the user to reply "Confirmed" or "OK" [10, 11].
5. **Output Generation:** Once approved, generate the template below. Ensure the YAML Frontmatter is included exactly as shown, populating the boolean flags to feed Step 02 [3]. Put your background reasoning inside the collapsible `<details>` tag [1].

---
**(START OF OUTPUT GENERATED TO USER)**

<!-- BLUEPRINT YAML FLAGS — READ BY STEP 02 CHECK 2 -->
<!-- Agent: extract the values below to determine which blocks to generate in __manifest__.py and __init__.py -->
---
addon_technical_name: "[INSERT: snake_case_name]"
odoo_version: "18.0"
depends: [INSERT: list of module dependencies, e.g., ['base', 'mail', 'helpdesk']]
flags:
  has_owl_components: [INSERT: true/false]   # Controls 'assets' block in __manifest__.py
  has_portal_access: [INSERT: true/false]    # Controls 'portal' in depends[]
  has_backend_models: [INSERT: true/false]   # Controls 'from . import models' in __init__.py
<!-- END BLUEPRINT YAML FLAGS -->
---

# 📋 ODOO 18 ADDON BLUEPRINT

## 1. Project Identity
* **Display Name:** [INSERT: Display Name (e.g., IT Helpdesk Ticketing)] [12]
* **Technical Name:** [INSERT: Technical Name (snake_case, e.g., it_ticketing)] [3]
* **Category:** [INSERT: Odoo Category (e.g., Services, Human Resources)] [12]
* **Edition:** [INSERT: Community / Enterprise] [12]

## 2. Business Context & Objectives
* **Business Problem:** [INSERT: 2-3 sentences describing the pain point] [4]
* **Measurable KPIs:** [INSERT: E.g., Reduce ticket resolution time by 20%] [4]

## 3. Architecture & Inheritance Decision
| Odoo 18 Core Module | Relation | Rationale |
| :--- | :--- | :--- |
| `[INSERT: e.g., helpdesk]` | `[INSERT: inherit / extend / none]` | `[INSERT: Detailed pros/cons of inheritance vs. standalone]` |
| `[INSERT: e.g., mail]` | `[INSERT: inherit]` | `[INSERT: Inherited for chatter tracking via mail.thread]` |

## 4. Feature Inventory
**Core Features (🔴 — Must build in Steps 02–09):**
| ID | Feature Description | Model Strategy | Est. Complexity |
| :--- | :--- | :--- | :--- |
| FR-01 | [INSERT: Feature name & goal] | [INSERT: e.g., Inherit helpdesk.ticket] | [INSERT: Low/Medium/High] |

**Nice-to-have Features (🟡 — Defer to optional steps or future sprint):**
| ID | Feature | Reason Deferred |
| :--- | :--- | :--- |
| NTH-01 | [INSERT: Feature Name] | [INSERT: Not blocking v1 delivery] |

**Out-of-scope (⚫ — Explicitly excluded):**
* [INSERT: Feature/System explicitly excluded and why] [13, 14]

## 5. User Roles & Security (ir.model.access)
| Role Name | Access Level (CRUD) | Domain / Record Rules |
| :--- | :--- | :--- |
| `[INSERT: e.g., Manager]` | `[INSERT: read, write, create, unlink]` | `[INSERT: e.g., Full access (1,1,1,1)]` |
| `[INSERT: e.g., User]` | `[INSERT: read, create, write (own)]` | `[INSERT: e.g., Domain: [('user_id', '=', user.id)]]` |

## 6. Workflow & State Machine (If applicable)
| From State | To State | Action / Button | Allowed Role |
| :--- | :--- | :--- | :--- |
| `[INSERT: e.g., Draft]` | `[INSERT: e.g., Confirmed]` | `[INSERT: action_confirm]` | `[INSERT: Manager]` |

<details>
<summary>🤖 Agent Technical Reasoning (Architecture Design Notes)</summary>

* **Model Design Choices:** [INSERT: Why specific field types or relations were chosen]
* **Views Constraints:** Ensure all lists use Odoo 18 `<list>` tag instead of `<tree>`. 
* **Display Names:** Use `_compute_display_name` over `name_get()`.
* **Performance:** Ensure heavy queries are planned using `search_fetch()`.
</details>

## 7. Handoff Confirmation
* **Status:** [INSERT: Select One | ⏳ AWAITING USER CONFIRMATION / ✅ CONFIRMED — Proceed to 02-scaffold] [15, 16]
* **Confirmed By:** [INSERT: User Name / Chat]
* **Date Confirmed:** [INSERT: YYYY-MM-DD]
