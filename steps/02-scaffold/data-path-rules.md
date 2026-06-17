---
artifact_name: Odoo 18 Data Path Rules
purpose: >
  Define the strict loading order for the data[] array in __manifest__.py.
  Prevent FileNotFoundError during scaffolding by enforcing an initially empty array.
used_by: steps/02-scaffold/SKILL.md
---

### 🤖 AGENT DIRECTIVE (HIDDEN FROM FINAL OUTPUT)
**Luật xử lý mảng `data[]` trong `__manifest__.py`:**

1. **TRẠNG THÁI KHỞI TẠO (INITIALIZE MODE):** 
   - Mảng `data: []` **BẮT BUỘC PHẢI ĐỂ TRỐNG** hoàn toàn. 
   - **Tuyệt đối không** tự bịa (hallucinate) hoặc điền trước các đường dẫn file (VD: `views/views.xml`).

2. **LÝ DO (WHY?):** 
   - Kiến trúc Odoo 18 kiểm tra sự tồn tại vật lý của file ngay lúc parse Manifest. Nếu một file được khai báo trong `data[]` nhưng chưa được tạo ra trên ổ cứng (vì các step 04, 05, 06 chưa chạy tới), Odoo sẽ crash ngay lập tức với lỗi `FileNotFoundError` và chặn toàn bộ quá trình cài đặt.

3. **QUY TRÌNH XỬ LÝ (RESOLUTION):** 
   - Việc điền đường dẫn vào mảng `data[]` được ủy quyền hoàn toàn cho **Step 10-review**. Ở bước 10, Agent sẽ quét lại toàn bộ thư mục vật lý và điền ngược lại (Backfill) vào file `__manifest__.py`.
   - Ở Step 02 này, Agent chỉ được phép đặt một dòng Comment làm điểm neo (Anchor) để Step 10 nhận diện.

---

### 📂 ODOO 18 STRICT DATA LOADING ORDER

Khi Step 10 quay lại để điền mảng `data[]`, nó **BẮT BUỘC** phải tuân thủ thứ tự nạp (load order) từ trên xuống dưới như sau. Odoo đọc file tuần tự, nếu nạp View trước khi nạp Security, hệ thống sẽ báo lỗi Access Rights.

**Thứ tự chuẩn (Template Anchor):**

```python
    'data': [
        # BẮT BUỘC THEO THỨ TỰ ODOO 18:
        # 1. QUẢN TRỊ BẢO MẬT (CSV TRƯỚC, XML SAU)
        # 'security/ir.model.access.csv',
        # 'security/security_rules.xml',
        
        # 2. DỮ LIỆU KHỞI TẠO VÀ CẤU HÌNH
        # 'data/ir_sequence_data.xml',
        # 'data/ir_cron_data.xml',
        # 'data/mail_template_data.xml',
        
        # 3. GIAO DIỆN NGƯỜI DÙNG (VIEWS & MENUS)
        # 'views/my_model_views.xml', (Luôn dùng thẻ <list>, KHÔNG dùng thẻ <tree>)
        # 'views/res_config_settings_views.xml',
        # 'views/menus.xml',
        
        # 4. GIAO DIỆN WIZARD (POPUP)
        # 'wizard/my_wizard_views.xml',
        
        # 5. BÁO CÁO IN ẤN (QWEB REPORTS)
        # 'report/my_report_templates.xml',
        # 'report/my_report_actions.xml',
    ],
```

### Quy tắc bất di bất dịch:

    File CSV luôn đi trước File XML: File security/ir.model.access.csv phải là file đầu tiên trong danh sách. Nếu Model chưa có quyền truy cập, các file XML View nạp phía sau sẽ bị từ chối (Access Denied).
    
    Menu nạp sau Action: File chứa thẻ <menuitem> (thường là menus.xml) nên được đặt sau các file chứa ir.actions.act_window để đảm bảo Action đã tồn tại khi Menu tham chiếu tới.
