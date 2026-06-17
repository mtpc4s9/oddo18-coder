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
1. **Check File Existence:** Trước khi viết code, kiểm tra xem `__manifest__.py` và `__init__.py` đã tồn tại chưa.
2. **Mode INITIALIZE (Nếu file chưa tồn tại):** 
   - Load Blueprint từ `steps/01-planning/output-template.md`.
   - Sinh mới hoàn toàn cấu trúc `__manifest__.py` với `data: []` (bỏ trống).
3. **Mode UPDATE (Nếu file đã tồn tại):** 
   - Đọc nội dung hiện tại của `__manifest__.py`.
   - Đối chiếu với Dependency Matrix, nếu có module mới cần thêm, hãy **APPEND (thêm vào)** mảng `depends[]` hiện tại. Tuyệt đối không ghi đè (overwrite) làm mất các thư mục trong mảng `data[]` hoặc `assets` đã được khai báo ở các bước trước.
4. **Deduplication:** Luôn loại bỏ các module trùng lặp trong mảng `depends[]`.
5. **Enterprise Alert:** Cảnh báo user ngay lập tức nếu phát hiện dependency thuộc bản Enterprise.
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

Nếu Blueprint từ `01-planning` yêu cầu bất kỳ module **Enterprise** nào trong bảng trên, Agent **PHẢI** dừng lại và hiển thị cảnh báo sau cho user trước khi tiếp tục:

```
⚠️ ENTERPRISE MODULE DETECTED
Tính năng "[tên feature]" yêu cầu module Odoo Enterprise: `[tên module]`

Lựa chọn:
  A) Xác nhận dùng Enterprise — tiếp tục scaffold với dependency này
  B) Thay thế bằng Community alternative — Agent sẽ gợi ý workaround
  C) Chuyển feature này sang Nice-to-have 🟡 và bỏ qua ở v1

→ User chọn phương án nào?
```

---

## 📐 DEPENDENCY ORDERING RULES

Khi đã có danh sách `depends[]`, sắp xếp theo thứ tự sau (Odoo parse từ trên xuống):

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
1. **Nếu file CHƯA tồn tại (Mode INITIALIZE):** Sinh mới hoàn toàn theo cấu trúc mẫu bên dưới.
2. **Nếu file ĐÃ tồn tại (Mode UPDATE):** Chỉ **APPEND (thêm vào)** mảng `depends[]`. Tuyệt đối không ghi đè làm mất các file trong mảng `data[]` hoặc `assets` đã được khai báo.

---

**OUTPUT FILE 1: `your_addon/__init__.py`**

Sẽ được cập nhật tự động ở Step 04 (Models) và Step 07 (Wizards). Tại Step 02, chỉ để trống với comment header:

```python
# -*- coding: utf-8 -*-
# Scaffold version — Step 02
# This file will be updated at: Step 04 (models), Step 07 (wizards)
# from . import models    # Uncommented at Step 04
# from . import wizards   # Uncommented at Step 07
```

> Xem chi tiết quy tắc tại: `references/templates/init_template.py`

---

**OUTPUT FILE 2: `your_addon/__manifest__.py`**

Sinh mới với cấu trúc xương sống dưới đây. Bắt buộc giữ nguyên các dòng comments trong mảng `data[]` để làm điểm neo (anchor) cho Step 10:

```python
# -*- coding: utf-8 -*-
{
    'name': '[INSERT: Display Name từ Blueprint]',
    'version': '18.0.1.0.0',
    'category': '[INSERT: Category từ Blueprint]',
    'summary': '[INSERT: Business Problem từ Blueprint]',
    'description': """
        [INSERT: Feature Inventory từ Blueprint]
    """,
    'depends': [
        'base',
        # [INSERT: Các dependencies khác lấy từ ma trận phía trên]
    ],
    'data': [
        # BẮT BUỘC THEO THỨ TỰ ODOO 18:
        # 1. security/ir.model.access.csv (Luôn nạp đầu tiên để tránh lỗi ACL)
        # 2. security/security_rules.xml
        # 3. data/*.xml (Sequences, Crons, Default Data)
        # 4. views/*.xml (Luôn dùng thẻ <list>, KHÔNG dùng thẻ <tree> cũ)
        # 5. wizard/*.xml
        # 6. report/*.xml
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
```

> Xem thêm rules về `data[]` ordering tại: `steps/02-scaffold/data-path-rules.md`
> Xem template đầy đủ với mọi comment giải thích tại: `references/templates/manifest_template.py`
