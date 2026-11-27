"""Simple business logic for employee records."""
class EmployeeService:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee_id, name, department):
        if not employee_id.strip():
            raise ValueError("Employee ID is required.")
        if not name.strip():
            raise ValueError("Employee name is required.")
        if not department.strip():
            raise ValueError("Department is required.")
        if self._find_by_id(employee_id):
            raise ValueError("An employee with this ID already exists.")
        employee = {
            "employee_id": employee_id.strip(),
            "name": name.strip(),
            "department": department.strip()
        }
        self._employees.append(employee)
        return employee.copy()

    def list_employees(self):
        return [employee.copy() for employee in self._employees]

    def list_by_department(self, department):
        department = department.strip().lower()
        return [
            employee.copy() for employee in self._employees
            if employee["department"].lower() == department
        ]

    def search_employees(self, term):
        term = term.strip().lower()
        if not term:
            return []
        return [
            employee.copy() for employee in self._employees
            if term in employee["employee_id"].lower()
            or term in employee["name"].lower()
        ]

    def update_department(self, employee_id, department):
        if not department.strip():
            raise ValueError("Department is required.")
        employee = self._find_by_id(employee_id)
        if employee is None:
            raise ValueError("Employee not found.")
        employee["department"] = department.strip()
        return employee.copy()

    def delete_employee(self, employee_id):
        employee = self._find_by_id(employee_id)
        if employee is None:
            return False
        self._employees.remove(employee)
        return True

    def _find_by_id(self, employee_id):
        for employee in self._employees:
            if employee["employee_id"].lower() == employee_id.strip().lower():
                return employee
        return None
