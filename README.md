# Employee Management — Day 5 AI Coding Assistant Demo

A beginner-friendly command-line Python project for GitHub Copilot / Claude demonstrations.

## Features
- Add, list, search, update and delete employee records.
- Basic input validation.
- Data is held in memory only; it is not saved after the program exits.

## Requirements
- Python 3.9+
- VS Code or PyCharm
- GitHub Copilot and/or Claude access for AI exercises
- No third-party Python packages

## Run
```bash
python app.py
```
On Windows, use `py app.py` if `python` is not recognized.

## Run unit tests
```bash
python -m unittest -v
```

## Suggested AI exercises
1. Ask AI to explain `employee_service.py`.
2. Add a feature to list employees by department.
3. Add a validation rule that employee IDs must start with E.
4. Generate additional unit tests for empty searches and missing employees.
5. Improve the README and add function documentation.
6. Refactor repeated validation logic without changing behaviour.
7. Debug the deliberate issue described in `DEBUGGING_EXERCISE.md`.
8. Review the code as if it were a pull request.

## Limitations
This is a teaching project, not production HR software. There is no database, login, web interface or personal-data protection layer. Always review AI-generated changes and run tests.
This project is used to demonstrate Git and CI/CD. 