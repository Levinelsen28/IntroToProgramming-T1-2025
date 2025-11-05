# Copilot instructions for this repository

Purpose: help an AI coding assistant be productive in this student-focused Intro to Programming repository.

Overview
- Small collection of standalone Python scripts grouped by folder:
  - `Assignments/` — assignment submissions (one script per task).
  - `Practice/` — practice exercises and short examples (often single-file scripts).
  - `Test/` and `Notes/` — ad-hoc test runners and instructor/student notes.
- There is no packaging, dependency manifest, or test framework. Most files are meant to be run directly with the system Python interpreter.

What to expect in the code
- Procedural scripts that rely on top-level `input()` and global variables (examples: `Assignments/AnimalSurvey.py`, `Practice/Dataconversion.py`).
- Minimal modularization. When adding helpers prefer to keep changes small and non-destructive.
- Inconsistent naming, typos, and occasional syntax issues — prioritize preserving original intent and variable names when editing.

Developer workflows (how to run & verify)
- Run any script from the repository root using PowerShell (Windows):
  - Example: `python .\Practice\Dataconversion.py`
  - Quote or escape filenames with spaces or special chars, e.g. `python "./Practice/3.4 Exception-Handling-&-Random.py"`
- There is no build step or CI; manual inspection and running the script is the common verification. Keep edits minimal and run the modified script locally.

Editing & patching guidance for AI agents
- Make minimal, conservative fixes: correct obvious syntax errors (only when intent is clear) and preserve variable names and user-facing prompt text.
- If adding functions or tests, place them near the modified file and keep the script runnable as `python path/to/file.py`.
- Avoid wholesale refactors across many files. Propose larger refactors as separate PRs and explain benefits.

Patterns & examples to reference
- Input-driven prompts: see `Assignments/AnimalSurvey.py` for the typical pattern of many `input()` calls and a final `summary` string.
- Type-conversion examples: see `Practice/Dataconversion.py` (watch for incorrect `input()` usage at the end).
- File naming: filenames often include spaces and punctuation — use quoted paths when running.

Common pitfalls to watch for
- Broken or malformed lines (e.g., `enter = input(input(enter ))` in `Practice/Dataconversion.py`) — fix only when intent is clear or ask the user.
- Hard-coded prints and prompts; changing prompt text may alter assignment semantics — avoid unless improving clarity.
- No test harness or linter present; run scripts manually after edits.

When to ask the user
- If a fix could change program behavior (refactor, API change, rename) ask before applying.
- If multiple plausible fixes exist for a bug, present options and recommended choice.

Files to consult for context
- `README.md` (project-level metadata)
- Representative scripts: `Assignments/AnimalSurvey.py`, `Assignments/Simple_Calculator.py`, `Practice/Dataconversion.py`, `Practice/2.6-practice.py`

If you update this file
- Merge intelligently: preserve any existing `.github/copilot-instructions.md` contents and only add or update repository-specific entries.

End of guidance.
