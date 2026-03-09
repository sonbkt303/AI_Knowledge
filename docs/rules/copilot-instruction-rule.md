Analyze the current repository and generate a concise `.github/copilot-instructions.md` file for this project.

Requirements:

1. The instructions must follow GitHub Copilot best practices:

   * Keep the file concise and focused.
   * Only include rules that cannot be easily inferred from the code.
   * Avoid repeating obvious information.

2. The instructions should contain the following sections when applicable:

   * Project Overview
   * Architecture
   * Coding Conventions
   * API Conventions (if backend)
   * UI Conventions (if frontend)
   * Error Handling
   * Testing Strategy
   * File Organization
   * Patterns for implementing new features

3. Infer as much as possible from the repository:

   * Programming language(s)
   * Frameworks (React, Spring, Express, etc.)
   * Folder structure
   * Testing tools
   * Styling frameworks
   * Common design patterns

4. Use clear rule-based bullet points that GitHub Copilot can follow when generating code.

5. The output must:

   * Be optimized for GitHub Copilot context usage.
   * Be under 200 lines.
   * Avoid long explanations.
   * Focus on actionable coding rules.

6. If the repository appears to follow a specific architecture (MVC, Clean Architecture, Hexagonal, etc.), document the rules clearly.

7. Add a "Feature Implementation Pattern" section describing the expected steps when implementing a new feature in this repository.

Return only the final markdown content of `.github/copilot-instructions.md`.
