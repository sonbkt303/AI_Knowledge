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
