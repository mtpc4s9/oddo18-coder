# Discovery Wrapper — Odoo 18 Context

> **Purpose:** This file constrains and extends `./product-discovery/SKILL.md` for Odoo addon development.
> Read this file BEFORE starting the product-discovery session.
> Do NOT modify `./product-discovery/SKILL.md` — customize via this wrapper only.

---

## Fixed Context (Never Ask About These)

The following are pre-determined for all Odoo addon projects. Skip any discovery question that targets these topics:

| Fixed Parameter | Value |
|---|---|
| Platform / Tech Stack | **Odoo 18** (Community or Enterprise — ask only if Enterprise features like Sign, VoIP are mentioned) |
| Programming Language | Python (backend), XML (views), OWL 2.0 (frontend components if needed) |
| Database | PostgreSQL (managed by Odoo ORM — never talk about raw SQL design) |
| Deployment target | On-premise Odoo server or Odoo.sh |

---

## Step 1 Override — Intent Type Extensions

Add the following Odoo-specific intent types to the standard detection table:

| Intent Type | Signal phrases |
|---|---|
| **Odoo Module Gap** | "Odoo không có tính năng...", "module mặc định không đủ...", "cần custom thêm vào Odoo" |
| **Odoo Integration** | "muốn kết nối với...", "cần sync data sang...", "API từ hệ thống ngoài" |
| **Odoo UI Customization** | "muốn thêm nút...", "muốn đổi layout...", "thêm field vào form có sẵn" |
| **Odoo Report** | "cần báo cáo...", "export PDF...", "QWeb template" |

> **⚠️ Common Odoo Solution Bias:** User says "tôi cần tạo module mới".
> Always investigate first — 80% of the time, `_inherit` from a core module is sufficient.

---

## Step 2 Override — Stakeholder → Odoo User Groups Mapping

When asking about "who needs this", always map answers to **Odoo user groups**:

| Business Role | Odoo User Group |
|---|---|
| System Admin / IT | `base.group_system` |
| Manager / Department Head | `[module].group_manager` (create custom) |
| Regular Staff / Employee | `[module].group_user` (create custom) |
| External Customer / Vendor | `base.group_portal` |
| Read-only Observer | `base.group_public` or custom readonly group |

**Action:** When user says "Manager can approve, Staff can only submit" — translate this immediately into:
- `group_manager`: approve + edit + delete
- `group_user`: create + read own records only

Note these mappings — they will directly populate Step 05-security.

---

## Step 3 Extension — Odoo-Specific Gap Dimensions

In addition to the standard gap detection, also scan for:

| Dimension | Questions to ask internally (not necessarily to user) |
|---|---|
| **Core Module Overlap** | Does Odoo 18 already have a module covering 50%+ of this? (`helpdesk`, `project`, `hr_expense`...) |
| **Chatter / Mail needed?** | Does this model need messaging, followers, logging? → `mail.thread` mixin |
| **Activity needed?** | Does this model need reminders, scheduled actions? → `mail.activity.mixin` |
| **Sequence needed?** | Does each record need a unique reference code (e.g., TICKET-001)? → `ir.sequence` |
| **Portal access needed?** | Can external users (customers/vendors) view/submit records? → website portal |
| **Report needed?** | Is a PDF output expected? → QWeb report |
| **Scheduled automation?** | Does anything need to run on a timer/cron? → `ir.cron` |

---

## Step 4 Extension — Odoo-Specific Question Library

When the standard `question-library.json` doesn't cover the case, use these Odoo-specific questions:

**For any Odoo feature request:**
1. "Trong Odoo hiện tại, người dùng đang giải quyết vấn đề này như thế nào? (email thủ công, Excel, Zalo?)"
2. "Có module Odoo nào khác đang được dùng liên quan không? (Helpdesk, Project, HR...)"
3. "Khi một record được tạo ra, ai sẽ được thông báo? Thông qua kênh nào? (chatter, email, SMS?)"
4. "Có cần phê duyệt nhiều cấp không? Nếu có, quy trình phê duyệt như thế nào?"
5. "Có cần cổng thông tin bên ngoài (portal) để khách hàng/nhà cung cấp tự tra cứu không?"

**For approval/workflow features:**
1. "State machine: các trạng thái (states) của một record là gì? (Draft → Confirmed → Done / Cancelled)"
2. "Ai được phép chuyển từ state này sang state kia?"
3. "Khi cancel/reject, có cần lý do ghi chú lại không?"

**For reporting needs:**
1. "Báo cáo cần export dạng gì? PDF (QWeb) hay Excel (xlsx)?"
2. "Tần suất chạy báo cáo: on-demand hay scheduled?"
3. "Ai được phép xem báo cáo? Chỉ Manager hay tất cả users?"

---

## Feature Classification Rules

When the user confirms feature requirements, **immediately classify** each feature into:

| Tier | Label | Meaning | Maps to |
|---|---|---|---|
| 🔴 Core | Must-have v1 | Cannot deliver value without this | `steps/` (main workflow) |
| 🟡 Nice-to-have | Optional, add later | Useful but not blocking | `optional/` in addon |
| ⚫ Out-of-scope | Explicitly excluded | Agreed not to build | Document in output-template Constraints |

**Rule:** If user says "that would be nice to have eventually" → immediately classify as 🟡 Nice-to-have.
**Rule:** If user says "not needed for now / out of scope" → immediately classify as ⚫ Out-of-scope.
**Rule:** Never leave a feature unclassified in the summary.

---

## Stop Condition Addendum

In addition to the standard stop condition in `product-discovery/SKILL.md` Step 7,
the Odoo discovery session must also confirm:

- [ ] Module technical name candidate identified (snake_case, unique, `<company>_<feature>` format preferred)
- [ ] At least one Odoo core module relationship identified (inherit or "standalone")
- [ ] All 🔴 Core features are listed with enough detail for a developer to understand scope
- [ ] User groups / access roles are mapped (even roughly)
- [ ] State machine defined (if any approval/workflow flow exists)

Only when all checkboxes above are ticked → discovery session is complete.

---

## Tone & Language

- Match the user's language (Vietnamese or English)
- Maintain senior BA professionalism — decisive, not overly formal
- Do NOT use marketing language or oversell the solution
- Do NOT say "Great question!" or similar filler phrases
