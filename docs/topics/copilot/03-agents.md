---
title: "Subagents — Tóm tắt"
slug: "copilot-subagents"
tags: [copilot, agents, subagents, orchestration]
language: VN
mode: short
---

<!-- TOC start -->
- [🤖 Subagents](#-subagents)
  - [🧩 Tổng quan (Overview)](#-tổng-quan-overview)
    - [🤔 Subagent là gì (What is a subagent)](#-subagent-là-gì-what-is-a-subagent)
    - [🗺️ Sơ đồ kiến trúc (Architecture diagram)](#️-sơ-đồ-kiến-trúc-architecture-diagram)
    - [🖼️ Minh hoạ luồng thực thi (Execution flow)](#️-minh-hoạ-luồng-thực-thi-execution-flow)
  - [⚙️ Cách hoạt động (How execution works)](#️-cách-hoạt-động-how-execution-works)
  - [🎯 Khi nào dùng subagents (Why use subagents)](#-khi-nào-dùng-subagents-why-use-subagents)
  - [🚦 Gọi subagent (Invoke a subagent)](#-gọi-subagent-invoke-a-subagent)
    - [Agent tự khởi tạo (Agent-initiated)](#agent-tự-khởi-tạo-agent-initiated)
    - [Khai báo trong prompt file](#khai-báo-trong-prompt-file)
    - [Chạy custom agent như subagent *(Experimental)*](#chạy-custom-agent-như-subagent-experimental)
  - [🔒 Kiểm soát \& hạn chế (Control \& limits)](#-kiểm-soát--hạn-chế-control--limits)
  - [🧭 Mẫu tổ chức (Orchestration patterns)](#-mẫu-tổ-chức-orchestration-patterns)
    - [Coordinator / Worker pattern](#coordinator--worker-pattern)
    - [Multi-perspective code review](#multi-perspective-code-review)
- [🏠 Local agents (Local agents)](#-local-agents-local-agents)
  - [✳️ Đặc điểm chính](#️-đặc-điểm-chính)
  - [🚀 Bắt đầu nhanh (Get started)](#-bắt-đầu-nhanh-get-started)
  - [⚠️ Lưu ý / Quyền truy cập](#️-lưu-ý--quyền-truy-cập)
  - [✅ Thực hành tốt (Best practices)](#-thực-hành-tốt-best-practices)
- [🔗 Tài nguyên (Resources)](#-tài-nguyên-resources)
<!-- TOC end -->

---

## 🤖 Subagents

> Subagents là các agent phụ độc lập, mỗi agent chạy trong **context window riêng**, được agent chính giao một subtask cụ thể (research, analysis, review) và chỉ trả kết quả tóm tắt — giúp context chính gọn, tăng hiệu suất bằng xử lý song song, và giảm chi phí token tổng thể.
> *(Subagents are independent agents with isolated context windows, delegated focused subtasks by the main agent, and return only summarized results.)*

---

### 🧩 Tổng quan (Overview)

#### 🤔 Subagent là gì (What is a subagent)

| Đặc điểm | Mô tả |
|---|---|
| **Context** | Mỗi subagent có context window độc lập — không kế thừa lịch sử hội thoại của agent chính |
| **Đầu ra** | Chỉ trả kết quả cuối cùng (summary) về agent chính, không đổ toàn bộ intermediate steps |
| **Chế độ chạy** | Đồng bộ (blocking) theo mặc định; VS Code hỗ trợ spawn nhiều subagents **song song** |
| **Model & tools** | Kế thừa từ session chính theo mặc định; có thể override qua custom agent |

> 📌 **Subagents khác session mới:** Session mới là cuộc hội thoại tách biệt hoàn toàn. Subagent vẫn nằm trong sự điều phối của agent chính và báo cáo kết quả lại.

#### 🗺️ Sơ đồ kiến trúc (Architecture diagram)

Main agent phân nhiệm sang nhiều subagents chạy trong context riêng biệt; mỗi subagent trả về bản tóm tắt kết quả cho agent chính.

#### 🖼️ Minh hoạ luồng thực thi (Execution flow)

![Subagent execution flow: agent chính phân nhiệm, subagents chạy song song trong context window riêng, trả kết quả tóm tắt về agent chính để tổng hợp.](assets/subagent-execution-flow.png)
*Hình 1: Luồng thực thi chi tiết — phân nhiệm → subagents chạy song song (context riêng) → trả tóm tắt → agent chính tổng hợp.*

---

### ⚙️ Cách hoạt động (How execution works)

1. Agent chính nhận task phức tạp từ người dùng.
2. Agent nhận diện phần cần phân tách và khởi tạo subagent qua công cụ `runSubagent`.
3. Subagent nhận **chỉ prompt của subtask** (không có conversation history).
4. Subagent thực thi tự động và trả kết quả tóm tắt.
5. Agent chính tổng hợp kết quả và tiếp tục luồng chính.

> 💡 **Tip:** Khi cần chạy song song, agent chính spawn nhiều subagents cùng lúc và chờ tất cả hoàn thành trước khi tiếp tục.

Trong Chat view, mỗi subagent hiển thị như một **tool call có thể thu gọn** — bao gồm tên agent, trạng thái tool đang chạy, toàn bộ prompt và kết quả khi mở ra.

---

### 🎯 Khi nào dùng subagents (Why use subagents)

| Tình huống | Lợi ích |
|---|---|
| Research trước khi implement | Giữ context chính tập trung vào orchestration |
| Phân tích song song nhiều khía cạnh | Tiết kiệm thời gian (security + perf + accessibility cùng lúc) |
| Thử nghiệm nhiều hướng giải quyết | Chỉ summary của hướng tốt nhất ảnh hưởng tới context chính |
| Review code đa góc nhìn | Mỗi subagent tiếp cận code độc lập, kết quả không bị ảnh hưởng lẫn nhau |
| Giảm token cost | Lịch sử subagent không tích lũy vào context chính |

---

### 🚦 Gọi subagent (Invoke a subagent)

#### Agent tự khởi tạo (Agent-initiated)

Đây là cách hoạt động chuẩn. Để cho phép agent tự dùng subagents:
- Đảm bảo công cụ `runSubagent` đang được bật trong tools picker.
- Agent chủ động phân tách task và delegate khi thấy cần; người dùng không cần gọi thủ công.

Người dùng có thể **gợi ý** agent dùng subagent bằng cách diễn đạt:
- `"Analyze security, performance, and accessibility simultaneously"`
- `"Run a subagent to research auth patterns before implementing"`

> 💡 **Tip:** Để subagent được dùng nhất quán, định nghĩa trong phần instructions của custom agent khi nào cần delegate — thay vì nhắc mỗi lần thủ công.

#### Khai báo trong prompt file

Thêm `agent` hoặc `runSubagent` vào `tools` trong frontmatter:

```markdown
---
name: document-feature
tools: ['agent', 'read', 'search', 'edit']
---
Run a subagent to research the new feature implementation details
and return only information relevant for user documentation.
Then update the docs/ folder with the new documentation.
```

#### Chạy custom agent như subagent *(Experimental)*

Custom agent khi dùng làm subagent có thể override model, tools, và instructions. Hai thuộc tính kiểm soát:

| Frontmatter | Ý nghĩa | Mặc định |
|---|---|---|
| `user-invocable: false` | Ẩn khỏi dropdown, chỉ dùng được qua subagent | `true` |
| `disable-model-invocation: true` | Chặn agent khác gọi agent này như subagent | `false` |

**Ví dụ — agent chỉ dùng được như subagent:**

```markdown
---
name: internal-helper
user-invocable: false
---
This agent can only be invoked as a subagent by other agents.
```

**Giới hạn subagents được phép dùng** — dùng `agents` frontmatter trên agent chính:

```markdown
---
name: TDD
tools: ['agent']
agents: ['Red', 'Green', 'Refactor']
---
Implement features using test-driven development via subagents:
1. Red agent: write failing tests
2. Green agent: make tests pass
3. Refactor agent: improve code quality
```

> ⚠️ Liệt kê rõ agent trong `agents` array sẽ override `disable-model-invocation: true` — nghĩa là coordinator được chỉ định vẫn có thể gọi agent đó.

---

### 🔒 Kiểm soát & hạn chế (Control & limits)

- **Model/tools mặc định:** kế thừa từ session chính — custom agent có thể chỉ định model riêng (ví dụ model nhanh/rẻ hơn cho worker agents).
- **Restrict subagents:** dùng `agents: ['A','B']` để chỉ cho phép các agent cụ thể; hoặc `agents: []` để tắt hoàn toàn.
- **`disable-model-invocation: true`:** ngăn agent bị gọi như subagent trong mọi trường hợp (trừ khi coordinator explicitly allow).
- Subagents **không tạo session mới** và **không có conversation history** — chỉ nhận task prompt.

---

### 🧭 Mẫu tổ chức (Orchestration patterns)

#### Coordinator / Worker pattern

Coordinator điều phối tổng thể; worker agents có tập tools và quyền riêng phù hợp với nhiệm vụ:

```markdown
---
name: Feature Builder
tools: ['agent', 'edit', 'search', 'read']
agents: ['Planner', 'Implementer', 'Reviewer']
---
For each feature request:
1. Planner: break down into tasks
2. Implementer: write code for each task
3. Reviewer: check implementation and flag issues
Iterate between Implementer and Reviewer until all issues are resolved.
```

**Worker agents (chỉ chạy như subagent):**

```markdown
---
name: Planner
user-invocable: false
tools: ['read', 'search']
---
Break down feature requests into prioritized implementation tasks.
```

```markdown
---
name: Reviewer
user-invocable: false
tools: ['read', 'search']
---
Review code for correctness, quality, and consistency with codebase conventions.
```

#### Multi-perspective code review

Chạy song song nhiều góc nhìn review, sau đó tổng hợp findings có ưu tiên:

```markdown
---
name: Thorough Reviewer
tools: ['agent', 'read', 'search']
---
Review code through multiple perspectives simultaneously (run as parallel subagents):
- Correctness: logic errors, edge cases, type issues
- Security: injection risks, input validation, data exposure
- Code quality: readability, naming, duplication
- Architecture: design consistency, codebase patterns

Synthesize findings into a prioritized summary after all subagents complete.
```

> 💡 Mỗi subagent tiếp cận code độc lập → kết quả không bị ảnh hưởng lẫn nhau, phát hiện lỗi khách quan hơn.

---

## 🏠 Local agents (Local agents)

> Local agents chạy trực tiếp trong Visual Studio Code trên máy của bạn, hoạt động trên workspace hiện tại và có quyền truy cập đầy đủ tới file, extension-provided tools, MCP servers và các mô hình đã cấu hình (bao gồm BYOK). Thích hợp cho tác vụ tương tác, cần ngữ cảnh dev (lint, test, stack traces) hoặc khi cần sử dụng công cụ cục bộ.

### ✳️ Đặc điểm chính

- Chạy trên máy local, có full access vào workspace và tools do extensions/MCP cung cấp.
- Giao diện chat tương tác — hỗ trợ phản hồi tức thì và gửi/queue messages trong phiên.
- Có thể sử dụng mọi model đã cấu hình trong VS Code (ví dụ BYOK hoặc các provider khác).
- Bao gồm các built-in agents: `Agent`, `Plan`, `Ask` — mỗi loại tối ưu cho workflow khác nhau.

### 🚀 Bắt đầu nhanh (Get started)

1. Mở Chat view → chọn agent từ agent picker (Agent / Plan / Ask).
2. Viết prompt cao cấp (ví dụ: "Implement a user authentication system with OAuth2 and JWT") và gửi.
3. Bật các tools cần thiết trong tools picker (read, search, edit, v.v.).
4. Review và xác nhận các code changes / tool invocations khi agent thực hiện.

> 💡 Tip: Dùng `Ask` để tra cứu trong codebase; `Plan` để chia nhỏ nhiệm vụ; `Agent` để sửa nhiều file tự động (luôn review các edits trước khi apply).

### ⚠️ Lưu ý / Quyền truy cập

- Nếu không thấy tùy chọn agent, kiểm tra setting `chat.agent.enabled` hoặc chính sách tổ chức.
- Agent có thể thay đổi file trực tiếp — luôn review các gợi ý và edits; VS Code cung cấp overlay để xem và áp dụng thay đổi có chọn lọc.
- `Edit mode` đã deprecated; dùng Agent mode cho multi-file edits.

---

### ✅ Thực hành tốt (Best practices)

- [ ] Định nghĩa rõ mục tiêu và output format mong đợi của mỗi subagent — tránh context thừa được trả về.
- [ ] Phân quyền theo vai trò: worker agents read-only (planner, reviewer), chỉ implementer có quyền edit.
- [ ] Dùng model nhanh/rẻ hơn cho worker agents có phạm vi hẹp để tối ưu chi phí.
- [ ] Khi cần audit, mở tool call của subagent trong Chat view để xem toàn bộ intermediate steps.
- [ ] Dùng `agents` frontmatter để kiểm soát chặt danh sách subagents cho các workflows quan trọng.
- [ ] Tránh truyền toàn bộ conversation history vào prompt subagent — chỉ truyền thông tin cần thiết cho subtask.

---

## 🔗 Tài nguyên (Resources)

| Chủ đề | Link |
|---|---|
| Subagents (official) | <https://code.visualstudio.com/docs/copilot/agents/subagents> |
| Custom agents | <https://code.visualstudio.com/docs/copilot/customization/custom-agents> |
| Agents overview | <https://code.visualstudio.com/docs/copilot/agents/overview> |
| Plan agent | <https://code.visualstudio.com/docs/copilot/agents/planning> |

