odoo18-coder/
│
├── SKILL.md                              # [MANDATORY] System Prompt & Routing. Chỉ chứa: routing + session protocol + global constraints.
│                                         # Note: Bắt buộc AI phải quét qua thư mục references/ để nạp Odoo 18 Rules TRƯỚC KHI bắt đầu gõ dòng code đầu tiên. Ngăn chặn triệt để thói quen sinh code Odoo 15, 16 của LLM.
│
├── steps/                                # Khối 1: Quy trình thực thi tuần tự (Standard Workflow)
│   ├── 01-planning                       # Phân tích yêu cầu & Thiết kế giải pháp.
│   │                                     # Note: AI phải ưu tiên Inheritance (Kế thừa) các module core (như helpdesk, sale, account) trước khi quyết định tạo model mới hoàn toàn (from scratch).
│   ├── 02-scaffold                       # Khởi tạo Manifest & Init.
│   │                                     # Note: Phải để mảng 'data': [] trống lúc đầu. Tệp này sẽ bị vòng lặp ở bước 10 bắt quay lại để cập nhật toàn bộ đường dẫn XML/CSV.
│   ├── 03-business-logic                 # Phác thảo luồng nghiệp vụ.
│   │                                     # Folder này chứa text thuần túy giải thích luồng hoạt động (VD: Nút A bấm vào gọi hàm B, chuyển state C).
│   ├── 04-models                         # Lập trình ORM & Database Design.
│   │                                     # Note: Tối kỵ dùng def name_get. BẮT BUỘC thay bằng def _compute_display_name(self): kèm @api.depends.
│   │                                     # Note: Ưu tiên dùng search_fetch(domain, ['field']) thay cho search() để chống N+1 Queries.
│   │                                     # Pointer → references/templates/model_template.py
│   ├── 05-security                       # Thiết lập phân quyền & Record Rules.
│   │                                     # Note: Bất kỳ Model nào (kể cả TransientModel ở bước 07) cũng phải được cấp quyền trong file security/ir.model.access.csv. Chuẩn file CSV phải đủ 8 cột. Dùng check_access('read') thay cho hàm cũ.
│   │                                     # Pointer → references/templates/security_template.csv
│   ├── 06-views-and-menus                # Thiết kế Giao diện người dùng (Backend XML)
│   │                                     # CẤM: Dùng thẻ <tree>. Phải dùng thẻ <list> cho mọi danh sách, nếu không module sẽ ValueError.
│   │                                     # CẤM: Dùng attrs="{...}". Phải dùng cú pháp Python thuần trên thẻ: invisible="state == 'done'".
│   │                                     # CẤM: Dùng oe_chatter. Phải dùng <chatter/>.
│   │                                     # Pointer → references/templates/view_template.xml
│   ├── 07-wizards                        # Xử lý TransientModels (Popups)
│   │                                     # Note: Agent phải kế thừa models.TransientModel, khai báo ir.actions.act_window với target="new" và bắt buộc cấp quyền trong file access ở bước 05.
│   ├── 08-data-and-reports               # Dữ liệu mẫu, Sequences & QWeb Reports
│   │                                     # Note: File QWeb Report XML phải dùng <t t-out="..."> thay vì thẻ t-esc cũ để render dữ liệu an toàn.
│   ├── 09-testing                        # Đảm bảo code chạy đúng. AI viết Unit Test bằng TransactionCase và UI Tests.
│   └── 10-review                         # [GATEKEEPER] Kiểm duyệt chất lượng Odoo 18. Note: Ép AI thực hiện Self-Reflection. AI phải rà soát lại file Manifest để xem đã nhét đủ list views/*.xml, security/*.csv vào mảng data chưa. Quét lại xem có sót chữ <tree> nào trong XML hay không. Pointer → references/checklists/*.md
│
├── optional/                             # Khối 2: Tính năng mở rộng (Chỉ gọi khi có Explicit Request)
│   ├── api-controllers                   # Lập trình HTTP/JSON-RPC Routes
│   │                                     # Note: Luôn inherit từ http.Controller và dùng @http.route.
│   └── owl-components                    # Lập trình Web Components (OWL 2.0). Note: Không sinh code jQuery/Backbone. Bắt buộc dùng functional components OWL 2.0 (useState, useService("orm")). Code JS/SCSS phải được đăng ký vào mảng assets: {'web.assets_backend': [...]} trong __manifest__.py.
│
└── references/                           # Khối 3: Kho tri thức & Bản vẽ (RAG Database). Trigger: Được gọi bởi sub-skill SKILL.md, không tự load.
    ├── knowledge/
    │   ├── odoo18-changes.md             # Các Migration Blockers từ bản cũ
    │   ├── orm-patterns.md               # Chuẩn tối ưu truy vấn Database
    │   └── security-patterns.md          # Các mẫu phân quyền chuẩn
    ├── templates/                        # Single source of truth — Odoo 18 base. NOTE: Các sub-skill SKILL.md phải trỏ đường dẫn tường minh (explicit pointer) tới đúng folder này 
    │   ├── manifest_template.py
    │   ├── init_template.py
    │   ├── model_template.py
    │   ├── view_template.xml
    │   └── security_template.csv
    ├── examples/                         # Mã nguồn tham chiếu
    │   └── it_ticketing/                 # Mirror cấu trúc steps / để Agent dễ tra cứu
    │       ├── 04-models/
    │       ├── 05-security/
    │       ├── 06-views/
    │       └── README.md
    └── checklists/                       # Cung cấp các file .md chứa các gạch đầu dòng (Ví dụ: Chống N+1 query, đã check Access rights CSV chưa, có khai báo assets OWL không). Bước 10-review sẽ nạp checklist ở thư mục này để chấm điểm code.
        ├── pre-code-checklist.md         # Phải check trước khi gõ code
        └── pre-commit-checklist.md       # Phải check trước khi kết thúc module

** Sub-folders structure:
steps/
├── 01-planning/
│   ├── SKILL.md                        # Leader của step này
│   │                                   # Trigger thứ tự: discovery → analysis → decision
│   │
│   ├── product-discovery/              # Git clone từ repo của bạn
│   │   └── (toàn bộ nội dung repo)     # SKILL.md không sửa, chỉ customize qua wrapper
│   │
│   ├── discovery-wrapper.md            # Customize lại cho phù hợp
│   │                                   # Override/extend product-discovery cho context Odoo
│   │
│   └── output-template.md              # Chuẩn hóa output của step 01
│                                       # → Feed trực tiếp vào step 02-scaffold
│
└── 02-scaffold/
    ├── SKILL.md                        # Leader của step này
    │                                   # Định nghĩa Pre-flight checks, Decision Tree và quy tắc Living File (chờ user duyệt trước khi sang Step 03)
    │
    ├── dependency-matrix.md            # Ma trận phân tích sự phụ thuộc (Dependencies Resolution)
    │                                   # Note: Chứa Alert Protocol cảnh báo module Enterprise & Handoff skeleton
    │
    ├── data-path-rules.md              # Quy tắc đặt tên và quản lý tệp dữ liệu XML/CSV
    │                                   # Note: Phân tách rạch ròi thứ tự load của ACL CSV và View XML
    │
    └── asset-registry-guide.md         # Quy chuẩn đăng ký Web Assets cho OWL 2.0 và Backend
                                        # Note: Loại bỏ hoàn toàn cú pháp kế thừa asset kiểu cũ của Odoo 15/16