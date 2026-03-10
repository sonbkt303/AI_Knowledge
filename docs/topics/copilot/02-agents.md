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
- [🧠 Bộ nhớ (Memory)](#-bộ-nhớ-memory)
  - [📊 Hai hệ thống nhớ (Two memory systems)](#-hai-hệ-thống-nhớ-two-memory-systems)
  - [🗂️ Phạm vi bộ nhớ (Memory scopes)](#️-phạm-vi-bộ-nhớ-memory-scopes)
  - [💬 Lưu trữ \& truy xuất (Store \& retrieve)](#-lưu-trữ--truy-xuất-store--retrieve)
  - [🗃️ Quản lý file nhớ (Manage memory files)](#️-quản-lý-file-nhớ-manage-memory-files)
  - [☁️ Copilot Memory (GitHub-hosted)](#️-copilot-memory-github-hosted)
  - [✅ Thực hành tốt (Best practices)](#-thực-hành-tốt-best-practices)
  - [🔗 Tài nguyên (Resources)](#-tài-nguyên-resources-2)
- [⚙️ Công cụ (Tools)](#️-công-cụ-tools)
  - [🔧 Loại công cụ (Types of tools)](#-loại-công-cụ-types-of-tools)
  - [⚡ Kích hoạt \& giới hạn (Enable \& limits)](#-kích-hoạt--giới-hạn-enable--limits)
  - [📝 Gọi công cụ trong prompt (Invoke tools)](#-gọi-công-cụ-trong-prompt-invoke-tools)
  - [🗂️ Nhóm công cụ (Tool sets)](#️-nhóm-công-cụ-tool-sets)
  - [🔐 Cấp quyền phiên (Permission levels)](#-cấp-quyền-phiên-permission-levels)
  - [✅ Phê duyệt công cụ (Tool approval)](#-phê-duyệt-công-cụ-tool-approval)
  - [✏️ Chỉnh sửa tham số trước khi chạy (Edit parameters)](#️-chỉnh-sửa-tham-số-trước-khi-chạy-edit-parameters)
  - [🖥️ Terminal commands](#️-terminal-commands)
  - [🛡️ Bảo mật \& sandbox (Security \& sandboxing)](#️-bảo-mật--sandbox-security--sandboxing)
  - [✅ Thực hành tốt (Best practices)](#-thực-hành-tốt-best-practices-1)
  - [🔗 Tài nguyên (Resources)](#-tài-nguyên-resources-3)
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
 
---

## 🧠 Bộ nhớ (Memory)

> Agents trong VS Code sử dụng bộ nhớ để **lưu giữ ngữ cảnh xuyên suốt các phiên làm việc** — không phải bắt đầu lại từ đầu mỗi phiên. VS Code hỗ trợ hai hệ thống nhớ bổ trợ nhau: **Memory tool** (cục bộ, mặc định bật) và **Copilot Memory** (GitHub-hosted, opt‑in).
> *(Agents use memory to retain context across sessions — remembering preferences, applying lessons from past tasks, and accumulating codebase knowledge over time.)*

---

### 📊 Hai hệ thống nhớ (Two memory systems)

| Tiêu chí | Memory tool | Copilot Memory |
|---|---|---|
| **Nơi lưu trữ** | Trên máy (local) | GitHub-hosted (remote) |
| **Phạm vi** | User, repository, session | Repository only |
| **Chia sẻ giữa surfaces** | Không (chỉ VS Code) | Có (coding agent, review, CLI) |
| **Tạo bởi** | Bạn hoặc agent trong chat | Copilot agents tự động |
| **Bật mặc định** | ✅ Có | ❌ Không (opt‑in) |
| **Hết hạn** | Quản lý thủ công | Tự động (~28 ngày) |

---

### 🗂️ Phạm vi bộ nhớ (Memory scopes)

| Phạm vi | Đường dẫn | Tồn tại xuyên phiên | Khi nào dùng |
|---|---|---|---|
| **User** | `/memories/` | ✅ Mọi workspace | Sở thích cá nhân, code style |
| **Repository** | `/memories/repo/` | ✅ Trong workspace | Kiến trúc, convention, lệnh build |
| **Session** | `/memories/session/` | ❌ Xóa khi kết thúc phiên | Ghi chú tạm thời, kế hoạch đang thực hiện |

> **Lưu ý:** 200 dòng đầu của **User memory** tự động được nạp vào context khi mở mỗi phiên làm việc.

---

### 💬 Lưu trữ & truy xuất (Store & retrieve)

**Lưu bộ nhớ** — yêu cầu agent ghi nhớ bằng ngôn ngữ tự nhiên:
```
Remember that our team uses conventional commits for all commit messages
```
Agent tự xác định phạm vi phù hợp và tạo/cập nhật file memory tương ứng.

**Truy xuất bộ nhớ** — hỏi agent trong phiên mới:
```
What are our commit message conventions?
```
Agent tự kiểm tra file memory và trả lời với thông tin đã lưu.

> References đến memory files trong phản hồi của agent là liên kết clickable — nhấn để mở trực tiếp nội dung file.

---

### 🗃️ Quản lý file nhớ (Manage memory files)

| Lệnh | Chức năng |
|---|---|
| `Chat: Show Memory Files` | Liệt kê và mở tất cả file memory theo từng scope |
| `Chat: Clear All Memory Files` | Xóa toàn bộ memory cục bộ |

> ⚠️ Xóa file memory riêng lẻ chưa được hỗ trợ. Để xóa một mục cụ thể, hãy yêu cầu agent cập nhật file đó hoặc dùng `Clear All`.

---

### ☁️ Copilot Memory (GitHub-hosted)

Copilot Memory là hệ thống bộ nhớ GitHub-hosted cho phép Copilot **học và lưu giữ insights về repository** theo thời gian, chia sẻ kiến thức giữa các Copilot agents.

**Đặc điểm nổi bật:**
- 🔗 **Repository-scoped:** memories gắn với repo cụ thể; chỉ contributors có quyền write mới có thể tạo.
- 🤝 **Cross-agent sharing:** insight từ Copilot code review có thể hướng dẫn Copilot coding agent và ngược lại.
- ✅ **Được xác minh trước khi dùng:** agents kiểm tra memories so với codebase hiện tại để tránh thông tin lỗi thời.
- ⏳ **Tự động hết hạn:** memories bị xóa sau ~28 ngày.

**Kích hoạt:**
1. Bật Copilot Memory trong [GitHub Copilot settings](https://github.com/settings/copilot).
2. Bật tích hợp trong VS Code: `github.copilot.chat.copilotMemory.enabled = true`.
3. Repository owners có thể xem/quản lý memories tại *Repository Settings → Copilot → Memory*.

---

### ✅ Thực hành tốt (Best practices)

| Tình huống | Dùng scope nào |
|---|---|
| Sở thích cá nhân, code style | **User** |
| Kiến trúc, convention, lệnh build dự án | **Repository** |
| Kế hoạch / ghi chú đang thực hiện | **Session** |
| Chia sẻ kiến thức giữa Copilot agents | **Copilot Memory** |

- 📤 **Xuất kết quả quan trọng:** Session memory bị xóa sau phiên — lưu kế hoạch vào file dự án nếu cần giữ lâu dài.
- 🔍 **Verify trước khi áp dụng:** luôn review thay đổi do agent tạo ra dựa trên memory.
- 🔒 **Bảo mật:** không lưu secrets hoặc dữ liệu nhạy cảm vào memory; Copilot Memory chia sẻ rộng hơn và cần bật có chủ ý.

---

### 🔗 Tài nguyên (Resources)

| Chủ đề | Link |
|---|---|
| Memory (official) | <https://code.visualstudio.com/docs/copilot/agents/memory> |
| Copilot Memory (GitHub) | <https://docs.github.com/copilot/how-tos/use-copilot-agents/copilot-memory> |
| Planning with agents | <https://code.visualstudio.com/docs/copilot/agents/planning> |

---

## ⚙️ Công cụ (Tools)

> Tools là các thành phần mở rộng mà agent dùng để thực hiện tác vụ chuyên biệt: tìm kiếm mã, lấy nội dung web, chạy lệnh terminal, hoặc gọi API bên ngoài. Mỗi tool đều đi kèm cơ chế phê duyệt để bảo vệ môi trường làm việc.
> *(Tools extend agents with specialized capabilities — code search, web fetches, terminal execution, API calls — each protected by an approval mechanism.)*

---

### 🔧 Loại công cụ (Types of tools)

| Loại | Nguồn gốc | Ví dụ điển hình |
|---|---|---|
| **Built-in** | VS Code tích hợp sẵn | `search`, `changes`, `problems`, `terminal`, `fetch` |
| **MCP tools** | MCP server (nội bộ hoặc bên thứ ba) | Truy vấn database nội bộ, gọi internal APIs |
| **Extension tools** | VS Code extension đóng góp qua Language Model Tools API | `#githubRepo`, công cụ CI/CD, JIRA, v.v. |

> **Tip:** Gõ `#` trong chat input để xem danh sách tất cả công cụ đang khả dụng.

---

### ⚡ Kích hoạt & giới hạn (Enable & limits)

- Bật/tắt công cụ cho từng request bằng **Configure Tools** trong Chat view.
- Để cấu hình cố định, chỉ định công cụ trong file `prompt` hoặc custom agent (xem [custom agents docs](https://code.visualstudio.com/docs/copilot/customization/custom-agents)).
- ⚠️ Giới hạn: **128 tools tối đa** trên một request. Nếu vượt, giảm bớt tools đang bật hoặc bật virtual tools threshold (`github.copilot.chat.virtualTools.threshold`).

---

### 📝 Gọi công cụ trong prompt (Invoke tools)

Agent tự chọn công cụ phù hợp dựa trên ngữ cảnh. Để chỉ định rõ ràng, dùng cú pháp `#toolName`:

| Prompt mẫu | Công cụ được gọi |
|---|---|
| `Summarize #fetch https://code.visualstudio.com/updates` | `fetch` — lấy nội dung URL |
| `Analyze security risks #githubRepo microsoft/vscode` | `githubRepo` — truy vấn repo |
| `Investigate #problems in the workspace` | `problems` — liệt kê lỗi hiện tại |
| `Analyze the codebase for patterns #reader` | `reader` (tool set) — nhóm công cụ đọc |

---

### 🗂️ Nhóm công cụ (Tool sets)

Tool sets giúp gom các công cụ liên quan thành một nhóm duy nhất, dễ tham chiếu với `#setName`.

**Tạo tool set** — chạy `Chat: Configure Tool Sets` → tạo file `.jsonc`:

```jsonc
{
  "reader": {
    "tools": ["changes", "codebase", "problems", "usages"],
    "description": "Tools for reading and gathering context",
    "icon": "book"
  },
  "search": {
    "tools": ["codebase", "fetch", "githubRepo"],
    "description": "Tools for deep research and code search",
    "icon": "search"
  }
}
```

---

### 🔐 Cấp quyền phiên (Permission levels)

| Cấp độ | Hành vi | Khi nào dùng |
|---|---|---|
| **Default Approvals** | Hiển thị hộp thoại theo cài đặt mặc định | Môi trường làm việc bình thường |
| **Bypass Approvals** | Tự động approves tất cả tool calls | Tác vụ đã kiểm tra kỹ, không rủi ro |
| **Autopilot** *(Preview)* | Auto-approve + auto-retry + auto-respond; agent chạy liên tục đến khi xong | Luồng tự động hoàn toàn (cẩn trọng) |

> 🔒 **Cảnh báo:** `Bypass Approvals` và `Autopilot` bỏ qua mọi confirmation — kể cả file edits, terminal commands, và external calls. Chỉ dùng khi hiểu rõ rủi ro.

---

### ✅ Phê duyệt công cụ (Tool approval)

Khi tool cần phê duyệt, hộp thoại xuất hiện với chi tiết tool và các lựa chọn:

| Lựa chọn | Hiệu lực |
|---|---|
| Approve once | Chỉ lần này |
| Approve for session | Trong suốt phiên làm việc hiện tại |
| Approve for workspace | Luôn approve trong workspace này |
| Always approve | Luôn approve trên mọi workspace |

**URL approval — 2 bước bảo vệ:**
1. **Pre-approval**: xác nhận gọi tới domain/URL (ngăn dữ liệu nhạy cảm bị gửi tới site không tin cậy).
2. **Post-approval**: duyệt nội dung response trước khi đưa vào chat (ngăn prompt injection từ nội dung bên ngoài).

Cấu hình auto-approve URL theo pattern:

```jsonc
"chat.tools.urls.autoApprove": {
  "https://*.internal.company.com/*": true,
  "https://api.github.com/*": true,
  "https://untrusted-site.io": false
}
```

> Dùng `Chat: Reset Tool Confirmations` để xóa toàn bộ phê duyệt đã lưu.

---

### ✏️ Chỉnh sửa tham số trước khi chạy (Edit parameters)

- Khi hộp thoại phê duyệt xuất hiện, mở rộng chevron cạnh tên tool.
- Chỉnh input parameters theo nhu cầu, rồi chọn **Allow**.

---

### 🖥️ Terminal commands

Agent chạy lệnh trong integrated terminal của VS Code. Những điểm quan trọng:

- **Background execution:** khi lệnh chạy lâu (build server, watch mode), chọn **Continue in Background** để agent tiếp tục tác vụ khác.
- **Timeout:** agent tự đặt timeout; dùng `chat.tools.terminal.enforceTimeoutFromModel` để kiểm soát.
- **Auto-approve terminal commands** qua `chat.tools.terminal.autoApprove`:

```jsonc
{
  "mkdir": true,
  "/^git (status|show\\b.*)$/": true,
  "/^npm (install|run)\\b/": true,
  "del": false,
  "/rm\\s+-rf/": false
}
```

- **Sandbox** *(Preview — macOS/Linux)*: giới hạn file/network access cho lệnh terminal. Trên Windows không có hiệu lực; dùng PowerShell (không dùng `cmd.exe` vì thiếu shell integration).

---

### 🛡️ Bảo mật & sandbox (Security & sandboxing)

- Bật sandbox: `chat.tools.terminal.sandbox.enabled = true` — terminal chạy trong môi trường kiểm soát, không cần confirm thủ công.
- Giới hạn file/network:

```jsonc
"chat.tools.terminal.sandbox.macFileSystem": {
  "allowWrite": ["."],
  "denyWrite": ["./secrets/", ".env"],
  "denyRead": ["/etc/passwd"]
},
"chat.tools.terminal.sandbox.network": {
  "allowedDomains": ["api.github.com", "*.npmjs.org"],
  "allowTrustedDomains": true
}
```

- Nếu có khả năng prompt injection hoặc môi trường rủi ro cao: ưu tiên dùng **container** hoặc **dev sandbox** thay vì máy cục bộ.

---

### ✅ Thực hành tốt (Best practices)

- [ ] Chỉ bật tools thực sự cần cho tác vụ hiện tại — giảm bề mặt tấn công và cải thiện chất lượng kết quả.
- [ ] Luôn review tham số tool trước khi approve, đặc biệt với tools thay đổi file hoặc gọi external service.
- [ ] Không lưu secrets, token hoặc dữ liệu nhạy cảm trong prompt; kiểm tra kỹ trước khi gọi `#fetch` tới URL nội bộ.
- [ ] Ưu tiên **session-level approval** thay vì global auto-approve trừ khi có yêu cầu đặc biệt.
- [ ] Bật sandbox/container trong môi trường CI hoặc khi tác vụ đòi hỏi quyền cao.

---

### 🔗 Tài nguyên (Resources)

| Chủ đề | Link |
|---|---|
| Agent tools (official) | <https://code.visualstudio.com/docs/copilot/agents/agent-tools> |
| Chat tools reference | <https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features#_chat-tools> |
| Agent hooks | <https://code.visualstudio.com/docs/copilot/customization/hooks> |
| Security considerations | <https://code.visualstudio.com/docs/copilot/security> |
| MCP servers | <https://code.visualstudio.com/docs/copilot/customization/mcp-servers> |

