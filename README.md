# 🚀 Odoo 18 Coder — AI Agent Skill System

> **Thiết kế bởi:** Phan Châu Minh Trường (Senior IT Business Analyst & Solution Architect)
> **Phát triển & Tối ưu:** Antigravity AI (Google DeepMind Agentic Coding)

`odoo18-coder` là hệ thống Skill bán tự động (Semi-Auto AI Agent Skill) được thiết kế riêng cho **Google Antigravity IDE (Gemini)** nhằm tối ưu hóa quy trình phát triển các custom addon chất lượng cao, chuẩn hóa trên nền tảng **Odoo 18**.

Hệ thống này chia nhỏ quy trình phát triển Odoo thành 10 bước nghiêm ngặt, đảm bảo chất lượng đầu ra, hạn chế tối đa việc LLM sinh code lỗi thời (Odoo v15/v16/v17) hoặc không tuân thủ các quy tắc tối ưu hiệu năng và bảo mật.

---

## 🗺️ Bản đồ Kiến trúc (Architecture Map)

Kiến trúc thư mục được thiết kế theo mô hình Modular & RAG-On-Demand:

```text
odoo18-coder/
├── SKILL.md                              # [MANDATORY] System Prompt & Routing chính
├── README.md                             # Tài liệu hướng dẫn sử dụng repo
├── ARCHITECTURE.md                       # Bản vẽ kỹ thuật & Quy chuẩn chi tiết
├── steps/                                # KHỐI 1: Quy trình thực thi tuần tự
│   ├── 01-planning                       # Phân tích yêu cầu, Gap & Inheritance analysis
│   ├── 02-scaffold                       # Khởi tạo Manifest & Module structure
│   ├── 03-business-logic                 # Đặc tả luồng nghiệp vụ (Text-only)
│   ├── 04-models                         # Database ORM, _compute_display_name, search_fetch
│   ├── 05-security                       # Phân quyền ir.model.access.csv (đủ 8 cột) & Record Rules
│   ├── 06-views-and-menus                # UI XML (Chỉ dùng <list>, <chatter/>, invisible thuần Python)
│   ├── 07-wizards                        # Xử lý TransientModels & Popups
│   ├── 08-data-and-reports               # Sequence, Demo data & QWeb Report (<t t-out="...">)
│   ├── 09-testing                        # Unit Test (TransactionCase) & Tour UI Test
│   └── 10-review                         # [GATEKEEPER] Rà soát lại Manifest, kiểm định chất lượng
│
├── optional/                             # KHỐI 2: Tính năng nâng cao (Khi có yêu cầu)
│   ├── api-controllers                   # Lập trình HTTP/JSON-RPC (http.Controller)
│   └── owl-components                    # Component giao diện OWL 2.0 (useState, assets)
│
└── references/                           # KHỐI 3: Tri thức & Bản vẽ mẫu (RAG Database)
    ├── knowledge/                        # Kinh nghiệm migration & tối ưu hóa Odoo 18
    ├── templates/                        # Code mẫu chuẩn Odoo 18 (Manifest, Model, View, Security)
    ├── examples/                         # Addon mẫu hoàn chỉnh (ví dụ: IT Ticketing)
    └── checklists/                       # Danh sách kiểm tra chất lượng code (Pre-code, Pre-commit)
```

---

## 🛠️ Quy trình Triển khai 10 Bước (The 10-Step Workflow)

| Bước | Tên Bước | Nhiệm vụ Trọng tâm | Quy chuẩn Odoo 18 |
|---|---|---|---|
| **01** | **Planning** | Phân tích yêu cầu, thiết kế giải pháp & Gap Analysis | Ưu tiên Kế thừa (Inheritance) các core module hơn là viết mới |
| **02** | **Scaffold** | Khởi tạo khung module, file `__manifest__.py` và `__init__.py` | Để trống mảng `'data': []` ban đầu, cập nhật dần ở các bước sau |
| **03** | **Business Logic** | Viết mô tả chi tiết luồng nghiệp vụ | Dùng text mô tả nghiệp vụ thô, chưa gõ code |
| **04** | **Models** | Khai báo các Model, Fields & ORM methods | Cấm `name_get`, dùng `_compute_display_name`. Dùng `search_fetch` chống N+1 |
| **05** | **Security** | Thiết lập bảo mật nhóm người dùng & Record Rules | Bắt buộc khai báo CSV đủ 8 cột cho mọi model (kể cả TransientModel) |
| **06** | **Views & Menus** | Tạo Giao diện Backend XML | Cấm thẻ `<tree>` (thay bằng `<list>`), cấm `attrs` (dùng `invisible=""`), cấm `oe_chatter` |
| **07** | **Wizards** | Tạo các màn hình hội thoại popup tương tác nhanh | Dùng `TransientModel` và Window Action với `target="new"` |
| **08** | **Data & Reports** | Tạo QWeb PDF Reports & Dữ liệu ban đầu | Dùng `<t t-out="...">` thay thế `<t t-esc="...">` lỗi thời |
| **09** | **Testing** | Lập trình các kịch bản kiểm thử | Viết Unit Test kế thừa `TransactionCase` |
| **10** | **Review** | Chạy checklist tự đánh giá chất lượng (Gatekeeper) | Tự đối chiếu với checklist, cập nhật hoàn thiện Manifest `data` |

---

## 🚦 Quy tắc Bắt buộc dành cho AI Agent (LLM Guardrails)

Khi khởi động và sử dụng Skill này trong Antigravity IDE, Agent bắt buộc phải tuân thủ:

1. **Nạp Tri thức Trước:** Phải quét qua thư mục `references/` để hiểu rõ sự khác biệt của Odoo 18 trước khi thực thi bất kỳ dòng code nào.
2. **Ngăn chặn Code Lỗi thời:** Tuyệt đối không sử dụng cú pháp cũ (như `attrs`, `name_get`, thẻ `<tree>` của view list, hay `<t t-esc>`).
3. **Cổng Kiểm Soát Nghiêm Ngặt:** Cuối mỗi bước đều có một **Stop Condition Gate**. Agent không được tự ý nhảy sang bước tiếp theo khi User chưa phê duyệt (`✅ CONFIRMED`).

---

## 💻 Cách sử dụng trong IDE

1. Sao chép thư mục `odoo18-coder` vào thư mục `.agent/skills/` của workspace hoặc thư mục global skill.
2. Khi ra lệnh cho Agent thực hiện một addon mới, hãy nhắc Agent kích hoạt skill này:
   > *"Sử dụng skill odoo18-coder để giúp tôi lập kế hoạch viết module IT Ticketing cho Odoo 18."*
3. Đi theo trình tự từ **Step 01** đến **Step 10** dưới sự kiểm soát của bạn.

---
*Chúc Chàng kiến tạo nên những phân hệ Odoo 18 thật xuất sắc!* 🥂
