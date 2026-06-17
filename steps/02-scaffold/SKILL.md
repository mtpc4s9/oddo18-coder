---
name: odoo18-coder-02-scaffold
description: >
  Use when the Addon Blueprint from Step 01 has been confirmed (Handoff Confirmation
  status shows ✅ CONFIRMED) and you need to generate the two foundational living files
  of the addon: __manifest__.py and __init__.py. Triggers when the user says
  "bắt đầu step 02", "scaffold module", "tạo manifest", "khởi tạo addon",
  or after receiving a confirmed Blueprint output from Step 01.
---

# Step 02 — Scaffold

## Routing Context

| Field | Value |
| :--- | :--- |
| **Receives from** | `steps/01-planning/output-template.md` (Blueprint YAML must be ✅ CONFIRMED) |
| **Feeds into** | `steps/04-models/SKILL.md` — `__init__.py` updated when `models/` added |
| **Feeds into** | `steps/07-wizards/SKILL.md` — `__init__.py` updated when `wizards/` added |
| **Feeds into** | `steps/10-review/SKILL.md` — `__manifest__.py` `data[]` finalized here |
| **Requires confirmation** | Yes — user must approve Scaffold Summary before proceeding to Step 03 |

---

## 🤖 AGENT DIRECTIVE

---

## ⚙️ PRE-FLIGHT: Mandatory Checks Before Any Code

Before generating a single line of code, execute these checks in order:

**CHECK 1 — Blueprint status:**
Read `steps/01-planning/output-template.md`.
Look for Section 7 Handoff Confirmation. The `Status` field MUST be:
`✅ CONFIRMED — Proceed to 02-scaffold`

→ If status is `⏳ AWAITING USER CONFIRMATION`: **STOP.**
Inform user: *"Blueprint chưa được confirm ở Step 01. Vui lòng quay lại
và xác nhận Blueprint trước khi scaffold."* Do not proceed.

**CHECK 2 — Extract YAML flags from Blueprint:**
From the Blueprint YAML Frontmatter, read and store locally:
```
addon_technical_name  →  [snake_case]
odoo_version          →  "18.0"
depends               →  [list from Blueprint]
flags.has_owl_components   →  true / false
flags.has_portal_access    →  true / false
flags.has_backend_models   →  true / false
```

**CHECK 3 — Resolve final dependencies:**
Load `steps/02-scaffold/dependency-matrix.md`.
Cross-check Blueprint Section 4 (Feature Inventory) against the matrix.
Merge with the `depends[]` already listed in Blueprint YAML.
Deduplicate. Apply ordering rules from the matrix.
→ If any **Enterprise** module is detected: trigger the Alert Protocol
defined in `dependency-matrix.md` and **await user choice** before continuing.

---

## 🔀 DECISION TREE — What to Generate

After all pre-flight checks pass:

```
has_backend_models = true?
  YES → include 'from . import models' in __init__.py
  NO  → __init__.py body is empty (just the import stub)

has_owl_components = true?
  YES → READ asset-registry-guide.md (see Handle Assets section below)
        inject 'assets' block into __manifest__.py
        ensure 'web' is in depends[]
  NO  → omit 'assets' block entirely from __manifest__.py

has_portal_access = true?
  YES → ensure 'portal' is appended last in depends[]
  NO  → omit
```

---

## 📦 PHASE 1 — Generate `__manifest__.py`

**Template reference (READ-ONLY):**
`references/templates/manifest_template.py`

**Populate with:**

| Field | Source |
| :--- | :--- |
| `name` | Blueprint → Section 1 → Display Name |
| `version` | `"18.0.1.0.0"` (fixed format, never change) |
| `category` | Blueprint → Section 1 → Category |
| `summary` | Blueprint → Section 2 → Business Problem (condensed, 1 line) |
| `author` | Blueprint → Section 1 → Author |
| `license` | Blueprint → Section 1 → License (default: `'LGPL-3'`) |
| `depends` | Resolved in CHECK 3 above |
| `data` | **ALWAYS `[]` — leave empty. See Living File Rules below.** |
| `installable` | `True` |
| `application` | `True` if this is a top-level menu app, else `False` |
| `auto_install` | `False` (default) |

**Handle Assets (conditional):**
IF `has_owl_components = true`:
→ Load `steps/02-scaffold/asset-registry-guide.md`
→ Follow its HOW section to inject the `assets` dictionary block
→ Place block above `'installable': True`
→ Ensure `'web'` is present in `depends[]`
IF `has_owl_components = false`:
→ Omit `assets` block entirely. Do not add placeholder.

---

## 📦 PHASE 2 — Generate `__init__.py`

**Template reference (READ-ONLY):**
`references/templates/init_template.py`

**Rules:**

```python
# Scaffold version — Step 02
# This file will be updated at: Step 04 (models), Step 07 (wizards)

from . import models      # include ONLY if has_backend_models = true
```

If `has_backend_models = false`, generate an empty `__init__.py` with
only the comment header. Do NOT add `from . import models` speculatively.

---

## ✅ PHASE 3 — Confirmation Gate

After generating both files, present the following summary to the user
**before closing the step**:

```
📋 SCAFFOLD SUMMARY — Awaiting Confirmation

__manifest__.py
  name        : [value]
  version     : 18.0.1.0.0
  depends     : [final resolved list]
  assets      : [injected / omitted]
  data[]      : [] ← intentionally empty until Step 10

__init__.py
  imports     : [from . import models / empty]

⚠️  Living File Reminder:
  - __manifest__.py → data[] will be backfilled at Step 10
  - __init__.py     → will be updated at Steps 04 and 07

✅ Confirm? Reply "OK" to finalize and proceed to Step 03.
```

Do NOT auto-advance to Step 03. Wait for explicit user confirmation.

---

## 📐 LIVING FILE RULES (Critical — Read Before Every Phase)

These files are NOT completed at Step 02. They evolve:

| File | Updated at | What changes |
| :--- | :--- | :--- |
| `__manifest__.py` | Step 02 | Initial scaffold (this step) |
| `__manifest__.py` | Step 10 | `data[]` backfilled in correct load order |
| `__init__.py` | Step 02 | Initial scaffold (this step) |
| `__init__.py` | Step 04 | `from . import models` confirmed/added |
| `__init__.py` | Step 07 | `from . import wizards` added if wizard exists |

**`data[]` load order (for Step 10 reference — do NOT fill now):**
```python
'data': [
    # 1. CSV first — security rules must load before any XML record
    'security/ir.model.access.csv',

    # 2. Base data (sequences, mail templates, cron jobs)
    'data/sequences.xml',
    'data/mail_templates.xml',

    # 3. Views last
    'views/your_model_views.xml',
    'views/menus.xml',

    # 4. Demo data (only if demo=True scope)
    # 'demo/demo_data.xml',
],
```

---

## 🔗 REFERENCE FILES USED IN THIS STEP

| File | Purpose | Action |
| :--- | :--- | :--- |
| `steps/01-planning/output-template.md` | Source of truth for all values | READ — extract Blueprint data |
| `steps/02-scaffold/dependency-matrix.md` | Resolve & order `depends[]` | READ — apply matrix logic |
| `steps/02-scaffold/asset-registry-guide.md` | OWL asset injection rules | READ **only if** `has_owl_components = true` |
| `references/templates/manifest_template.py` | Odoo 18 manifest syntax | READ-ONLY — never modify |
| `references/templates/init_template.py` | Odoo 18 init syntax | READ-ONLY — never modify |

---

## 🚫 ANTI-PATTERNS — Never Do This

```python
# ❌ WRONG — filling data[] at scaffold time
'data': [
    'security/ir.model.access.csv',
    'views/views.xml',
],

# ✅ CORRECT — always empty at Step 02
'data': [],
```

```python
# ❌ WRONG — adding 'web' speculatively
'depends': ['base', 'mail', 'web'],   # web added "just in case"

# ✅ CORRECT — 'web' only if has_owl_components = true
'depends': ['base', 'mail'],
```

```python
# ❌ WRONG — version format
'version': '1.0',
'version': '18.1.0',

# ✅ CORRECT — Odoo convention
'version': '18.0.1.0.0',
```

```xml
<!-- ❌ WRONG — legacy asset declaration in XML (Odoo 15 pattern) -->
<template id="assets_backend" inherit_id="web.assets_backend">

<!-- ✅ CORRECT — declared in __manifest__.py 'assets' dict only -->
```
