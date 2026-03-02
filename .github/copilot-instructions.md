# Copilot Instructions

For this repository, follow PEP 8 for all Python code.

## Style requirements

- Use 4 spaces for indentation (no tabs).
- Keep lines at 79 characters when practical (88 max only if readability clearly improves).
- Use `snake_case` for functions, variables, and module names.
- Use `PascalCase` for class names.
- Use `UPPER_CASE` for constants.
- Group imports as: standard library, third-party, local modules.
- Add a blank line between top-level definitions.
- Prefer explicit, readable names over abbreviations.
- Include docstrings for public modules, classes, and functions.
- Use lowercase `snake_case` for new file names when practical.
- Avoid ALL_CAPS file names unless a tooling convention requires it.

## Quality checks

- Ensure generated code is compatible with `flake8` PEP 8 expectations.
- Avoid unused imports, variables, and dead code.
- Keep functions focused and reasonably short.

## Agent mode request tracking

- Apply this tracking policy in this repository and reuse it as the
    default in future projects.
- Automatically track each Agent Mode request in `agent_request_log.md`.
- Add one entry per user request with: date, user, model, request
    summary, recap, status, and files changed.
- Keep `agent_request_log.md` entries in newest-first order.
- Update the log at the end of each completed request.
- Update and save the log automatically without prompting the user.
- If no files are changed, still add an entry and mark files as `none`.

### Entry checklist

- Include: date, user, model, request summary, recap, status,
  and files changed.
- Insert each new entry as the first row under the log table header.
- Use `Completed` for finished requests.
- Use `none` when no files changed.
- Do not ask for confirmation before writing the log entry.

## Reusable starter block (copy/paste)

Use this block in new projects:

```md
## Agent mode request tracking

- Apply this tracking policy in this repository and reuse it as the
    default in future projects.
- Automatically track each Agent Mode request in `agent_request_log.md`.
- Add one entry per user request with: date, user, model, request
    summary, recap, status, and files changed.
- Keep `agent_request_log.md` entries in newest-first order.
- Update the log at the end of each completed request.
- Update and save the log automatically without prompting the user.
- If no files are changed, still add an entry and mark files as `none`.
```