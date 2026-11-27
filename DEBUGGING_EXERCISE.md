# Day 5 — Debugging Exercise

1. Open `employee_service.py`.
2. In `search_employees()`, change `term in employee["name"].lower()` to `term in employee["name"]`.
3. Run `python -m unittest -v`.
4. Observe the case-insensitive search test failure.
5. Ask Copilot or Claude to explain the failure and identify the smallest correction.
6. Apply the correction and run the tests again.

Lesson: AI can help diagnose a problem, but the developer confirms the fix by running tests.
