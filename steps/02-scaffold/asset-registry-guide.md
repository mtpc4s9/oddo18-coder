---
artifact_name: Odoo 18 Asset Registry Guide
purpose: >
  Instruct the Agent on WHEN and HOW to declare OWL 2.0 frontend assets
  (JS/SCSS/XML) inside the __manifest__.py file for Odoo 18.
used_by: steps/02-scaffold/SKILL.md
---

### 🤖 AGENT DIRECTIVE (HIDDEN FROM FINAL OUTPUT)
**Luật khai báo tài nguyên (Asset Registration Rules) trong Odoo 18:**

1. **WHEN (Khi nào cần khai báo?):**
   - Agent **BẮT BUỘC** phải đọc YAML Frontmatter từ file output của `01-planning`.
   - **Nếu cờ `has_owl_components: true`**: Agent phải khởi tạo khối (block) `'assets'` trong `__manifest__.py`. Đồng thời, bắt buộc thêm `'web'` vào mảng `'depends': []`.
   - **Nếu cờ `has_owl_components: false`**: Agent bỏ qua khối `'assets'` để giữ file gọn gàng, giảm thiểu độ phức tạp không cần thiết.

2. **HOW (Khai báo như thế nào cho chuẩn Odoo 18?):**
   - **CẤM (FORBIDDEN):** Tuyệt đối không dùng thẻ `<template id="assets_backend" inherit_id="web.assets_backend">` bên trong một file XML để load JS/CSS (Đây là legacy pattern đã bị loại bỏ).
   - **BẮT BUỘC (REQUIRED):** Phải khai báo trực tiếp dưới dạng một Dictionary (từ điển) bên trong tệp `__manifest__.py`.
   - Để thêm tài nguyên vào giao diện quản trị (Backend UI), BẮT BUỘC phải dùng từ khóa (key) `'web.assets_backend'`.

3. **QUY TẮC GIỮ CHỖ (PLACEHOLDER RULE DÀNH CHO BƯỚC SCAFFOLD):**
   - Tại Step 02 (Scaffold), các tệp JS/XML/SCSS vật lý chưa được sinh ra (chúng sẽ được xử lý độc lập tại nhánh `optional/owl-components`).
   - Do đó, Agent chỉ được phép đặt một dòng chú thích giữ chỗ (Anchor Comment) để **Step 10-review** nhận diện và tự động điền (Backfill) đường dẫn thực tế.

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
