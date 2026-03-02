# Copilot Instructions

For this repository, follow PEP 8 for all Python code.

## Project-level PEP 8 policy

- Apply PEP 8 for all Python code generated or edited in this project.
- Keep code compatible with `flake8` expectations.

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
- Use lowercase names for all new files by default.
- Allow uppercase only for `README.md`.

## Quality checks

- Ensure generated code is compatible with `flake8` PEP 8 expectations.
- Avoid unused imports, variables, and dead code.
- Keep functions focused and reasonably short.

## Global-level PEP 8 defaults (future projects)

- Reuse this PEP 8 policy as the default for future Python projects.
- Keep 4-space indentation, snake_case naming, and readable line length.
- Prefer clear naming, clean imports, and docstrings for public code.

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
## Python style defaults

- Follow PEP 8 for all Python code.
- Use 4 spaces (no tabs), snake_case naming, and readable line lengths.
- Keep generated code compatible with flake8 expectations.

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

### File naming defaults for future projects

- Use lowercase names for new files by default.
- Allow uppercase only for `README.md`.