---
name: "Workspace Copilot Instructions"
description: "Workspace-wide guidance for GitHub Copilot and local custom agents. Keeps AI behavior consistent for contributors."
---

# Workspace AI Instructions

Purpose: provide clear, project-specific guidance for Copilot and custom agents so outputs are safe, consistent, and actionable.

Quick start:
- Enable inline suggestions in VS Code.
- Install the GitHub Copilot extension and sign in.
- Use the `GITHUB-COPILOT-SETUP.md` checklist for onboarding.

Conventions in this workspace:
- Default language: Vietnamese for end-user-facing content unless `language=EN` is specified.
- Filenames & slugs: kebab-case, 2-digit index prefix for topic artifacts (`docs/topics/01-example-topic.md`).
- Diagrams: prefer SVG; supply a one-sentence Vietnamese caption and `alt` text for accessibility.
- Security: do not include secrets in prompts or generated code. Review AI-generated code before merging.

Known agents and skills:
- SmartLearn agent: summarized learning assistant. See [.github/agents/smartlearn.agent.md](.github/agents/smartlearn.agent.md#L1) for full behavior and prompts.

Build & test commands:
- No centralized build/test commands were detected in repository documentation. If this project has language-specific build or test steps, add them under `Tooling` in this file so agents can run them automatically.

Recommended workflow for contributors:
1. Open an issue or PR describing the desired content or task.
2. Use a short prompt and include context (file path or snippet) when asking the agent for code changes.
3. Run tests locally and add results to the PR description.

Example prompts to try with workspace agents:
- "Tóm tắt Transformer architecture cho kỹ sư ML trung cấp; mode=short; language=VN."
- "Tạo 5 ý chính từ tài liệu sau và lưu vào docs/topics/transformer/01-transformer.md."
- "Visual summary của Clean Architecture; xuất Mermaid block và gợi ý tên file." 

Suggested next customizations:
- Add `applyTo`-scoped instruction files for `docs/` and `src/` if you want different behaviors per area.
- Create a `.vscode/settings.json` workspace fragment to pin Copilot settings for the team.
- Add `Tooling` section with build/test commands so agents can run or suggest commands reliably.

Where to find more:
- Workspace Copilot setup: [GITHUB-COPILOT-SETUP.md](GITHUB-COPILOT-SETUP.md#L1)
- SmartLearn agent: [.github/agents/smartlearn.agent.md](.github/agents/smartlearn.agent.md#L1)

If you'd like, I can:
- Add a `.vscode/settings.json` snippet to enforce inline suggestions and recommended extensions.
- Add `Tooling` commands to this file if you provide the build/test steps.
