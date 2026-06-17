# -*- coding: utf-8 -*-
# Template: Odoo 18 Custom Addon — __manifest__.py
# READ-ONLY reference for Step 02-Scaffold. Do not modify this file.
# Agent populates values from the confirmed Blueprint (01-planning/output-template.md).

{
    # ─── IDENTITY ────────────────────────────────────────────────────────────────
    'name': 'Your Addon Display Name',
    # Source: Blueprint → Section 1 → Display Name

    'version': '18.0.1.0.0',
    # FIXED FORMAT — Never change. Convention: <odoo_ver>.<major>.<minor>.<patch>

    'category': 'Services',
    # Source: Blueprint → Section 1 → Category
    # Must match Odoo's official category list (e.g. 'Services', 'Human Resources',
    # 'Accounting', 'Sales', 'Inventory', 'Technical', 'Hidden')

    'summary': 'One-line description of what this addon does.',
    # Source: Blueprint → Section 2 → Business Problem (condensed to 1 line)

    'description': """
        Detailed multi-line description.
        Explain the module's purpose and key features.
    """,

    'author': 'Your Name or Company',
    # Source: Blueprint → Section 1 → Author

    'license': 'LGPL-3',
    # Source: Blueprint → Section 1 → License
    # Common choices: 'LGPL-3' (open), 'OPL-1' (proprietary), 'AGPL-3' (copyleft)

    'website': '',

    # ─── DEPENDENCIES ────────────────────────────────────────────────────────────
    # Resolved using: steps/02-scaffold/dependency-matrix.md
    # Ordering rules (strict):
    #   1. 'base'  — always first if listed explicitly
    #   2. 'mail'  — core technical infra (chatter, activities)
    #   3. 'web'   — only if has_owl_components = true or has_api_controller = true
    #   4. Business modules (alphabetical within group): account, hr, project, sale, stock
    #   5. Extension modules (must come after their parents): helpdesk, hr_timesheet
    #   6. 'portal', 'website' — always last if present
    'depends': [
        'base',
        'mail',
        # [INSERT: Other resolved dependencies from dependency-matrix.md]
    ],

    # ─── DATA ARRAY (LIVING FILE — ALWAYS EMPTY AT STEP 02) ──────────────────────
    # DO NOT add any paths here at scaffold time.
    # Reason: Odoo 18 checks physical file existence during manifest parsing.
    # Adding a path before the file exists on disk will cause FileNotFoundError
    # and prevent module installation entirely.
    #
    # This array is backfilled by Step 10 (Gatekeeper) in this mandatory order:
    #   1. 'security/ir.model.access.csv'    ← CSV always first (ACL before views)
    #   2. 'security/security_rules.xml'
    #   3. 'data/ir_sequence_data.xml'
    #   4. 'data/ir_cron_data.xml'
    #   5. 'data/mail_template_data.xml'
    #   6. 'views/your_model_views.xml'      ← ALWAYS use <list>, NEVER <tree>
    #   7. 'views/res_config_settings_views.xml'
    #   8. 'views/menus.xml'                 ← After action declarations
    #   9. 'wizard/your_wizard_views.xml'
    #  10. 'report/your_report_templates.xml'
    #  11. 'report/your_report_actions.xml'
    'data': [],

    # ─── ASSETS (CONDITIONAL) ────────────────────────────────────────────────────
    # INCLUDE this block ONLY if has_owl_components = true (from Blueprint flags).
    # OMIT this block entirely if has_owl_components = false. Do not add as placeholder.
    # Populated at: optional/owl-components step
    #
    # 'assets': {
    #     'web.assets_backend': [
    #         # TBD at optional/owl-components step:
    #         # 'your_addon/static/src/components/**/*.js',
    #         # 'your_addon/static/src/components/**/*.xml',
    #         # 'your_addon/static/src/components/**/*.scss',
    #     ],
    # },

    # ─── INSTALL FLAGS ───────────────────────────────────────────────────────────
    'installable': True,

    'application': False,
    # Set True ONLY if this addon introduces a top-level menu item (app icon on home screen)

    'auto_install': False,
    # Always False for custom addons. True is reserved for Odoo core glue modules.
}
