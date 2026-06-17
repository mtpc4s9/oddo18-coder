---
artifact_name: Odoo 18 Asset Registry Guide
purpose: >
  Instruct the Agent on WHEN and HOW to declare OWL 2.0 frontend assets
  (JS/SCSS/XML) inside the __manifest__.py file for Odoo 18.
used_by: steps/02-scaffold/SKILL.md
---

### 🤖 AGENT DIRECTIVE (HIDDEN FROM FINAL OUTPUT)
**Asset Registration Rules in Odoo 18:**

1. **WHEN (When to register assets?):**
   - The Agent **MUST** read the YAML Frontmatter from the output file of `01-planning`.
   - **If the flag `has_owl_components: true`**: The Agent must initialize the `'assets'` block in `__manifest__.py`. Additionally, `'web'` must be added to the `'depends': []` array.
   - **If the flag `has_owl_components: false`**: The Agent must skip the `'assets'` block to keep the file clean and minimize unnecessary complexity.

2. **HOW (How to declare assets for Odoo 18?):**
   - **FORBIDDEN:** Never use the `<template id="assets_backend" inherit_id="web.assets_backend">` tag inside an XML file to load JS/CSS (this is a legacy pattern and has been removed).
   - **REQUIRED:** You must declare them directly as a dictionary inside the `__manifest__.py` file.
   - To add assets to the Backend UI, you **MUST** use the `'web.assets_backend'` key.

3. **PLACEHOLDER RULE FOR SCAFFOLD STEP:**
   - At Step 02 (Scaffold), physical JS/XML/SCSS files have not been generated yet (they will be handled in the `optional/owl-components` branch).
   - Therefore, the Agent is only allowed to insert a placeholder comment (Anchor Comment) for **Step 10-review** to identify and backfill with physical file paths.

---

### 📦 CẤU TRÚC ASSETS CHUẨN (ODOO 18 MANIFEST)

Khi cờ `has_owl_components: true` kích hoạt, Agent phải chèn khối mã sau vào cuối file `__manifest__.py` (ngay phía trên khóa `'installable': True`):

```python
    'assets': {
        'web.assets_backend': [
            # TBD in Step 10: OWL 2.0 Components (JS, SCSS, XML)
            # Example: 'your_addon_name/static/src/components/**/*.js',
            # Example: 'your_addon_name/static/src/components/**/*.xml',
            # Example: 'your_addon_name/static/src/components/**/*.scss',
        ],
    },
```
