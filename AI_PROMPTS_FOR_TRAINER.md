# Day 5 — Ready-to-use prompts for Copilot / Claude

## 1. Explain the code
Explain `employee_service.py` to a beginner. Describe each method, its inputs, outputs and purpose. Do not modify the code.

## 2. Generate a feature
Add `list_by_department(department)` to EmployeeService. It should return employees in that department, ignoring case. Keep the current style and add unit tests for matching and non-matching departments.

## 3. Generate documentation
Improve README.md with project purpose, features, setup, run instructions, test instructions and limitations. Do not claim this application uses a database.

## 4. Generate tests
Add tests for empty search, updating a missing employee and rejecting an empty department. Use Python's built-in unittest.

## 5. Refactor
Suggest a small refactoring that preserves behaviour. Explain the change before applying it. Run tests afterwards.

## 6. Debug
The search feature does not find a name when the user enters different capitalization. Find the root cause and suggest the smallest safe fix. Do not change unrelated methods.

## 7. Pull request review
Review this project as a pull request. Report actionable findings only. Include severity, file/method, issue, impact and suggested fix. Do not invent issues.

## 8. Agent-style task
Implement the department-filter feature across the service and unit tests. First explain which files will change. Make the smallest change, run tests and summarize the changes.

Trainer note: code completion, chat and agent-style features depend on the selected product, IDE and account permissions. Review diffs and test results before accepting changes.
This project is used to demonstrate Git and CI/CD.