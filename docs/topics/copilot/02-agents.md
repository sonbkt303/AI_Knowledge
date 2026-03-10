---
title: "Copilot Agents — Tóm tắt"
slug: "copilot-agents-overview"
tags: [copilot, agents, overview]
language: VN
mode: short
---


<!-- TOC start -->
- [🧩 Tổng quan (Overview)](#-tổng-quan-overview)
  - [🤖 Agent là gì (What is an agent)](#-agent-là-gì-what-is-an-agent)
  - [🧭 Các loại agent (Types of agents)](#-các-loại-agent-types-of-agents)
  - [📋 Quản lý phiên (Session management)](#-quản-lý-phiên-session-management)
  - [⚠️ Lưu ý quan trọng (Key notes)](#️-lưu-ý-quan-trọng-key-notes)
  - [🔗 Tài nguyên (Resources)](#-tài-nguyên-resources)
- [🚀 Lập kế hoạch (Planning / Plan agent)](#-lập-kế-hoạch-planning--plan-agent)
  - [🎯 Cách khởi động (How to start)](#-cách-khởi-động-how-to-start)
  - [🔄 Quy trình 4 pha (4-phase workflow)](#-quy-trình-4-pha-4-phase-workflow)
  - [💾 Ghi nhớ phiên (Session memory)](#-ghi-nhớ-phiên-session-memory)
  - [⚙️ Tùy chỉnh \& cài đặt (Customization \& settings)](#️-tùy-chỉnh--cài-đặt-customization--settings)
  - [💡 Ví dụ thực tế (Actionable example)](#-ví-dụ-thực-tế-actionable-example)
  - [🔗 Tài nguyên (Resources)](#-tài-nguyên-resources-1)
<!-- TOC end -->

---

## 🧩 Tổng quan (Overview)

> Agents là tác nhân AI trong VS Code thực hiện tác vụ lập trình nhiều bước — phân tích lỗi, sửa code, chạy test và tạo PR — hoàn toàn tự động theo vòng lặp **hiểu → thực thi → kiểm tra**.

### 🤖 Agent là gì (What is an agent)

| Khía cạnh | Mô tả (VN) | Description (EN) |
|---|---|---|
| **Định nghĩa** | Tiến trình/phiên AI tự động hoá workflow lập trình nhiều bước | A session that automates a multi-step coding workflow |
| **Khả năng** | Đọc tệp, sửa mã, chạy lệnh terminal, truy vấn web, tạo diff/PR | Read files, edit code, run commands, query web, produce diffs/PRs |
| **Kiểm soát** | Tự động nhưng cần approval cho thay đổi quan trọng | Automated but requires human approval for significant changes |

### 🧭 Các loại agent (Types of agents)

| Loại (Type) | Môi trường | Dùng khi (When to use) |
|---|---|---|
| **Local** | VS Code, trên máy | Tương tác, brainstorming, debug, truy cập workspace đầy đủ |
| **Background** | Máy cục bộ, không tương tác (Copilot CLI + Git worktree) | Tác vụ đã xác định rõ, chạy nền |
| **Cloud** | Hạ tầng từ xa, tích hợp GitHub | Hợp tác nhóm, tạo PR tự động |
| **Third‑party** | Local hoặc cloud (Anthropic, OpenAI…) | Cần năng lực mô hình từ nhà cung cấp cụ thể |



### 📋 Quản lý phiên (Session management)

**Danh sách phiên (Sessions list)**
- Chat view hiển thị danh sách phiên, trạng thái (chưa đọc / đang chạy), chế độ compact / side-by-side.
- Mỗi phiên độc lập (context riêng); có thể chạy song song.

**Tạo phiên mới (Create a session)**
→ Hướng dẫn chi tiết: [Tạo một phiên agent](https://code.visualstudio.com/docs/copilot/agents/overview#_create-an-agent-session)

**Chuyển phiên (Hand off)**
- Chuyển giữa các loại agent (Plan → Background → Cloud), lịch sử hội thoại được chuyển theo.
- Dùng `/delegate` để ủy quyền từ background → cloud.

**Xem & áp dụng thay đổi (Review & apply)**
- Mở chi tiết phiên để xem diff và thống kê file.
- Local: áp dụng trực tiếp vào workspace. Cloud: checkout nhánh/PR để review rồi merge.

**Lưu trữ & xóa phiên (Archive & delete)**
- Archive: dọn danh sách nhưng không mất dữ liệu, có thể phục hồi.
- Delete: xóa vĩnh viễn — background sessions có thể kèm worktree bị xóa cùng.

### ⚠️ Lưu ý quan trọng (Key notes)

- ❌ **Không thử nghiệm trực tiếp trên nhánh chính** — luôn dùng nhánh riêng.
- ⚠️ **Quản lý ngữ cảnh** — compaction/memory để tránh mất context hoặc tràn context window.
- 🔒 **Bảo mật** — cẩn trọng với quyền truy cập web và secrets; luôn review thay đổi do agent tạo.

### 🔗 Tài nguyên (Resources)

- Trang chính thức — Agents overview & tutorial: <https://code.visualstudio.com/docs/copilot/agents/overview>


## 🚀 Lập kế hoạch (Planning / Plan agent)

> Plan agent **nghiên cứu yêu cầu và tạo kế hoạch triển khai có cấu trúc** trước khi thực thi bất kỳ thay đổi mã nào — đảm bảo yêu cầu, ràng buộc và rủi ro được xem xét kỹ lưỡng từ đầu.
> *(Researches requirements and produces a structured implementation plan before any code changes are made.)*

---

### 🎯 Cách khởi động (How to start)

| Cách | Hướng dẫn |
|---|---|
| **Qua Chat UI** | Mở Chat (`Ctrl+Alt+I`) → chọn chế độ **Plan** từ menu agent |
| **Qua lệnh nhanh** | Gõ `/plan <mô tả nhiệm vụ>` trực tiếp trong Chat |

> **Lưu ý:** Plan agent sẽ đặt câu hỏi làm rõ trước khi tạo kế hoạch — trả lời đầy đủ để kế hoạch chính xác hơn.

---

### 🔄 Quy trình 4 pha (4-phase workflow)

| # | Pha | Mô tả (VN) | Description (EN) |
|---|---|---|---|
| 1 | **Discovery** | Nghiên cứu yêu cầu, đọc codebase, thu thập ngữ cảnh | Research requirements, read codebase, gather context |
| 2 | **Alignment** | Đặt câu hỏi làm rõ để tránh giả định sai | Ask clarifying questions to avoid wrong assumptions |
| 3 | **Design** | Phác thảo các bước triển khai chi tiết, có thứ tự ưu tiên | Draft prioritized, actionable implementation steps |
| 4 | **Refinement** | Lặp và hoàn thiện kế hoạch cho đến khi đáp ứng yêu cầu | Iterate until the plan fully meets requirements |

**Luồng:** `Discovery` → `Alignment` → `Design` → `Refinement` → *(triển khai hoặc hand off)*

---

### 💾 Ghi nhớ phiên (Session memory)

- Kế hoạch được lưu tự động vào **`/memories/session/plan.md`** trong suốt phiên làm việc.
- Xem file bằng lệnh: *Chat: Show Memory Files*.
- ⚠️ Session memory **bị xóa** khi kết thúc cuộc trò chuyện — xuất kế hoạch ra file dự án nếu cần lưu lâu dài.

---

### ⚙️ Tùy chỉnh & cài đặt (Customization & settings)

| Cài đặt | Mục đích |
|---|---|
| `chat.planAgent.defaultModel` | Model mặc định cho Plan agent |
| `github.copilot.chat.implementAgent.model` | Model dùng khi chuyển sang triển khai |
| `github.copilot.chat.planAgent.additionalTools` *(experimental)* | Thêm MCP tools để truy cập dữ liệu nội bộ |

- Tạo **custom planning agent** để áp dụng quy trình và tiêu chuẩn nội bộ của nhóm.

---

### 💡 Ví dụ thực tế (Actionable example)

**Prompt gửi cho agent:**
```
/plan Implement API pagination and tests
```

**Kế hoạch mẫu agent có thể tạo ra:**
1. Kiểm tra các endpoint hiện có và cấu trúc dữ liệu hiện tại
2. Xác định hợp đồng phân trang (query params, cấu trúc metadata trong response)
3. Triển khai logic phân trang phía server + unit tests
4. Cập nhật tài liệu API và chạy QA

**Checklist kiểm tra trước khi triển khai:**
- [ ] Tất cả endpoints trả về metadata phân trang (`page`, `limit`, `total`)
- [ ] Tests bao phủ edge cases (offset âm, limit = 0, tập kết quả rỗng)
- [ ] Tài liệu API cập nhật với ví dụ request/response

---

### 🔗 Tài nguyên (Resources)

| Chủ đề | Link |
|---|---|
| Planning guide (official) | <https://code.visualstudio.com/docs/copilot/agents/planning> |
| Session memory | <https://code.visualstudio.com/docs/copilot/agents/memory> |
| Custom agents | <https://code.visualstudio.com/docs/copilot/customization/custom-agents> |
