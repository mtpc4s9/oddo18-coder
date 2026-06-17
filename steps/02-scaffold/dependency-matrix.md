---
artifact_name: Odoo 18 Dependency Matrix
purpose: >
  Map features declared in the Addon Blueprint (01-planning/output-template.md)
  to their correct Odoo 18 module dependencies.
  Agent uses this file to populate the `depends[]` array in __manifest__.py
  without hallucinating module names.
used_by: steps/02-scaffold/SKILL.md
source_of_truth: Odoo 18 Community & Enterprise base modules (verified)
last_verified: "2024-12"
---

### 🤖 AGENT DIRECTIVE (HIDDEN FROM FINAL OUTPUT)
**How to use this matrix & handle Living Files:**
1. **Check File Existence:** Before writing code, check if `__manifest__.py` and `__init__.py` already exist.
2. **INITIALIZE Mode (If file does not exist):** 
   - Load Blueprint from `steps/01-planning/output-template.md`.
   - Generate a brand new `__manifest__.py` structure with `data: []` (empty array).
3. **UPDATE Mode (If file already exists):** 
   - Read the current content of `__manifest__.py`.
   - Cross-reference with the Dependency Matrix, and if new modules are required, **APPEND** them to the existing `depends[]` array. Do NOT overwrite or lose directories/assets declared in `data[]` or `assets` by previous steps.
4. **Deduplication:** Always remove duplicate modules in the `depends[]` array.
5. **Enterprise Alert:** Alert the user immediately if any dependency belongs to the Enterprise edition.
---

## 📦 DEPENDENCY MATRIX — ODOO 18

### TIER 1 — Always Required (base stack)

| Nếu addon có bất kỳ model nào | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Bất kỳ model mới nào (from scratch) | `base` | Community | Luôn có mặt, kể cả khi inherit module khác |
| Cần chatter / ghi log / gửi email nội bộ | `mail` | Community | Kế thừa `mail.thread` + `mail.activity.mixin` |
| Cần schedule action (cron) | `base_automation` | Community | Thêm vào nếu dùng `ir.cron` |
| Cần gửi email ra ngoài (SMTP template) | `mail` | Community | `mail.template` + `mail.compose.message` |

---

### TIER 2 — Theo Feature Type

#### 🎫 Ticketing / Helpdesk / Support

| Feature | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Kế thừa Helpdesk Ticket | `helpdesk` | **Enterprise** | ⚠️ Cần Odoo Enterprise license |
| Viết ticket system mới (không kế thừa helpdesk) | `mail`, `base` | Community | Dùng `mail.thread` để có chatter |
| SLA / deadline tracking | `helpdesk` | **Enterprise** | SLA model chỉ có trong Enterprise |
| Ticket rating / satisfaction | `helpdesk` | **Enterprise** | Hoặc tự build với `rating.mixin` từ `rating` |
| Customer-facing ticket portal | `portal`, `website` | Community | Kế thừa `portal.mixin` |

#### 📋 Project / Task Management

| Feature | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Kế thừa project.task | `project` | Community | Có sẵn Kanban, Deadline, Tags |
| Gantt view cho task | `project_enterprise` | **Enterprise** | Gantt chỉ có Enterprise |
| Milestone tracking | `project` | Community | Từ Odoo 16+ milestone có sẵn trong Community |
| Timesheet trên task | `hr_timesheet` | Community | Link task ↔ timesheet line |

#### 👥 HR / Nhân sự

| Feature | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Liên kết với nhân viên | `hr` | Community | `hr.employee` model |
| Leave / nghỉ phép | `hr_holidays` | Community | `hr.leave`, `hr.leave.type` |
| Payroll | `hr_payroll` | **Enterprise** | ⚠️ Enterprise only |
| Appraisal / đánh giá | `hr_appraisal` | **Enterprise** | ⚠️ Enterprise only |
| Recruitment pipeline | `hr_recruitment` | Community | `hr.applicant` model |

#### 💰 Sales / CRM / Invoicing

| Feature | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Liên kết với Sale Order | `sale` | Community | `sale.order`, `sale.order.line` |
| Liên kết với khách hàng (Partner) | `base` | Community | `res.partner` có sẵn trong base |
| Tạo hóa đơn từ module | `account` | Community | `account.move` model |
| Subscription / recurring | `sale_subscription` | **Enterprise** | ⚠️ Enterprise only |
| CRM Pipeline / Lead | `crm` | Community | `crm.lead` model |
| Pricelist | `product`, `sale` | Community | `product.pricelist` |

#### 📦 Inventory / Kho

| Feature | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Liên kết sản phẩm | `product` | Community | `product.template`, `product.product` |
| Quản lý kho, stock move | `stock` | Community | `stock.picking`, `stock.move` |
| Lot / Serial number | `stock` | Community | Bật tracking trên product |
| Barcode scanning | `barcodes`, `stock_barcode` | Community | Cần cả 2 module |
| Landed costs | `stock_landed_costs` | Community | |

#### 📊 Reporting / Analytics

| Feature | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| QWeb PDF Report | `web` | Community | `ir.actions.report` + QWeb template |
| Spreadsheet / pivot export | `spreadsheet` | **Enterprise** | ⚠️ Enterprise only |
| Dashboard (odoo native) | `spreadsheet_dashboard` | **Enterprise** | ⚠️ Enterprise only |
| Graph / Pivot view trong list | `base` | Community | Không cần thêm depends, built-in |

#### 🌐 Portal / Website / External Access

| Feature | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Khách hàng xem record qua portal | `portal` | Community | Kế thừa `portal.mixin` trên model |
| Trang web tĩnh hoặc form online | `website` | Community | Cần cả `website` nếu có page |
| eCommerce | `website_sale` | Community | |
| Live chat | `im_livechat` | Community | |

#### 🔔 Approval / Workflow

| Feature | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Multi-level approval workflow | `approvals` | **Enterprise** | ⚠️ Enterprise only |
| Approval đơn giản (2 bước, tự build) | `mail` | Community | Dùng state machine + chatter thủ công |
| Sign / chữ ký số | `sign` | **Enterprise** | ⚠️ Enterprise only |

#### 📅 Calendar / Scheduling

| Feature | `depends[]` | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Liên kết với Calendar event | `calendar` | Community | `calendar.event` model |
| Resource scheduling (Gantt) | `resource` | Community | Base resource model |
| Appointment booking | `appointment` | Community | Từ Odoo 16+ |

#### 🔧 Technical / Infrastructure

| Feature | depends[] | Edition | Ghi chú |
| :--- | :--- | :--- | :--- |
| Cần tạo màn hình cấu hình (Settings) / Kế thừa res.config.settings | `base_setup` | Community | Menu Settings sẽ nằm trong Configuration |
| Viết UI Tests (Tour testing) bằng Javascript | `web_tour` | Community | Cần cho step 09 nếu có yêu cầu test giao diện |
| OWL frontend component | `web` | Community | Bắt buộc khai báo trong web.assets_backend |
| HTTP Controller / JSON-RPC | `web` | Community | `from odoo import http` |
| Sequence (auto-numbering) | `base` | Community | `ir.sequence` có sẵn trong base |
| Geo / Map view | `base_geolocalize` | Community | |
| Multi-company | `base` | Community | `company_id` field + `res.company` |
| Multi-currency | `base`, `account` | Community | Cần `account` nếu có monetary field |
| Discuss / real-time chat | `mail`, `bus` | Community | `bus` cho real-time polling |

---

## ⚠️ ENTERPRISE DEPENDENCY ALERT PROTOCOL
If the Blueprint from `01-planning` requires any **Enterprise** module in the table above, the Agent **MUST** pause and display the following warning to the user before proceeding:

```
⚠️ ENTERPRISE MODULE DETECTED
Feature "[feature name]" requires Odoo Enterprise module: `[module name]`

Options:
  A) Confirm Enterprise usage — proceed scaffolding with this dependency
  B) Replace with Community alternative — Agent will suggest a workaround
  C) Shift this feature to Nice-to-have 🟡 and defer in v1

→ Which option do you choose?
```

---

## 📐 DEPENDENCY ORDERING RULES

Once the `depends[]` list is determined, sort it according to the following order (Odoo parses from top to bottom):

```python
depends = [
    # 1. Luôn đứng đầu nếu có
    'base',

    # 2. Core technical infra
    'mail',
    'web',

    # 3. Business modules (alphabetical trong nhóm)
    'account',
    'hr',
    'project',
    'sale',
    'stock',

    # 4. Extension modules (phụ thuộc vào module ở trên)
    'helpdesk',
    'hr_timesheet',
    'sale_subscription',

    # 5. Portal / Website (luôn cuối cùng nếu có)
    'portal',
    'website',
]
```

**Quy tắc cứng:**
- `base` luôn đứng đầu nếu được liệt kê tường minh
- Module A phụ thuộc module B → B phải đứng trước A
- `portal` và `website` luôn đứng cuối
- Không thêm `web` nếu addon không có OWL component hoặc HTTP controller

---

#### 🔗 HANDOFF TO SCAFFOLD

Sau khi resolve xong `depends[]`, Agent sinh ra 2 file thực tế của addon theo cơ chế **Living Files (Tệp sống)**:

**🤖 AGENT DIRECTIVE (LIVING FILES PROTOCOL):**
1. **If file DOES NOT exist (INITIALIZE Mode):** Generate a brand new file according to the template below.
2. **If file ALREADY exists (UPDATE Mode):** Only **APPEND** to the `depends[]` array. Do NOT overwrite or lose files/assets declared in `data[]` or `assets`.

---

**OUTPUT FILE 1: `your_addon/__init__.py`**

This will be updated automatically in Step 04 (Models) and Step 07 (Wizards). In Step 02, keep it empty with a comment header:

```python
# -*- coding: utf-8 -*-
# Scaffold version — Step 02
# This file will be updated at: Step 04 (models), Step 07 (wizards)
# from . import models    # Uncommented at Step 04
# from . import wizards   # Uncommented at Step 07
```

> See detailed rules at: `references/templates/init_template.py`

---

**OUTPUT FILE 2: `your_addon/__manifest__.py`**

Generate a new file with the skeleton structure below. You must retain the comment lines in the `data[]` array as anchors for Step 10:

```python
# -*- coding: utf-8 -*-
{
    'name': '[INSERT: Display Name from Blueprint]',
    'version': '18.0.1.0.0',
    'category': '[INSERT: Category from Blueprint]',
    'summary': '[INSERT: Business Problem from Blueprint]',
    'description': """
        [INSERT: Feature Inventory from Blueprint]
    """,
    'depends': [
        'base',
        # [INSERT: Other dependencies from the matrix above]
    ],
    'data': [
        # MANDATORY ORDER FOR ODOO 18:
        # 1. security/ir.model.access.csv (Always load first to avoid ACL errors)
        # 2. security/security_rules.xml
        # 3. data/*.xml (Sequences, Crons, Default Data)
        # 4. views/*.xml (Always use the <list> tag, DO NOT use the deprecated <tree> tag)
        # 5. wizard/*.xml
        # 6. report/*.xml
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
```

> See more rules on `data[]` ordering at: `steps/02-scaffold/data-path-rules.md`
> See full template with comments at: `references/templates/manifest_template.py`
