---
artifact_name: Odoo 18 Data Path Rules
purpose: >
  Define the strict loading order for the data[] array in __manifest__.py.
  Prevent FileNotFoundError during scaffolding by enforcing an initially empty array.
used_by: steps/02-scaffold/SKILL.md
---

### 🤖 AGENT DIRECTIVE (HIDDEN FROM FINAL OUTPUT)
**Rules for handling the `data[]` array in `__manifest__.py`:**

1. **INITIALIZE MODE:** 
   - The `data: []` array **MUST BE LEFT COMPLETELY EMPTY**. 
   - **Do not** hallucinate or pre-populate file paths (e.g., `views/views.xml`).

2. **WHY?** 
   - Odoo 18 checks for the physical existence of files during manifest parsing. If a file is declared in `data[]` but does not exist on disk yet (as steps 04, 05, 06 have not run), Odoo will immediately crash with a `FileNotFoundError` and block installation.

3. **RESOLUTION:** 
   - Populating the `data[]` array is delegated entirely to **Step 10-review**. In Step 10, the Agent will scan physical directories and backfill the paths into `__manifest__.py`.
   - In Step 02, the Agent must only insert comments as anchors for Step 10 to locate.

---

### 📂 ODOO 18 STRICT DATA LOADING ORDER

When Step 10 returns to populate the `data[]` array, it **MUST** follow the load order from top to bottom. Odoo loads files sequentially; if a View is loaded before Security, the system will raise an Access Rights error.

**Standard Template Anchor:**

```python
    'data': [
        # MANDATORY ORDER FOR ODOO 18:
        # 1. SECURITY AND ACLs (CSV FIRST, XML SECOND)
        # 'security/ir.model.access.csv',
        # 'security/security_rules.xml',
        
        # 2. INITIALIZATION AND CONFIGURATION DATA
        # 'data/ir_sequence_data.xml',
        # 'data/ir_cron_data.xml',
        # 'data/mail_template_data.xml',
        
        # 3. USER INTERFACE (VIEWS & MENUS)
        # 'views/my_model_views.xml', (Always use <list> tag, DO NOT use deprecated <tree> tag)
        # 'views/res_config_settings_views.xml',
        # 'views/menus.xml',
        
        # 4. WIZARDS AND POPUPS
        # 'wizard/my_wizard_views.xml',
        
        # 5. PRINTABLE QWEB REPORTS
        # 'report/my_report_templates.xml',
        # 'report/my_report_actions.xml',
    ],
```

### Golden Rules:

    CSV Files Before XML Files: The security/ir.model.access.csv file must be the first file loaded. If models do not have defined access rights, any subsequent XML Views loaded will be rejected with an Access Denied error.
    
    Menus After Actions: Files containing <menuitem> tags (usually menus.xml) must be loaded after the files containing their referenced window actions (ir.actions.act_window) to ensure references do not break.
