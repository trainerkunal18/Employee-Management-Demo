"""Run tests with: python -m unittest -v"""
import unittest
from employee_service import EmployeeService

class EmployeeServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = EmployeeService()

    def test_add_and_list_employee(self):
        self.service.add_employee("E101", "Asha", "Engineering")
        self.assertEqual(self.service.list_employees()[0]["name"], "Asha")

    def test_duplicate_id_is_rejected(self):
        self.service.add_employee("E101", "Asha", "Engineering")
        with self.assertRaises(ValueError):
            self.service.add_employee("E101", "Ravi", "Finance")

    def test_search_is_case_insensitive(self):
        self.service.add_employee("E101", "Asha Sharma", "Engineering")
        self.assertEqual(len(self.service.search_employees("asha")), 1)

    def test_list_by_department_is_case_insensitive(self):
        self.service.add_employee("E101", "Asha", "Engineering")
        self.service.add_employee("E102", "Ravi", "Finance")
        employees = self.service.list_by_department("engineering")
        self.assertEqual([employee["employee_id"] for employee in employees], ["E101"])

    def test_list_by_department_returns_empty_for_non_matching_department(self):
        self.service.add_employee("E101", "Asha", "Engineering")
        self.assertEqual(self.service.list_by_department("Finance"), [])

    def test_update_department(self):
        self.service.add_employee("E101", "Asha", "Engineering")
        updated = self.service.update_department("E101", "Platform")
        self.assertEqual(updated["department"], "Platform")

    def test_delete_employee(self):
        self.service.add_employee("E101", "Asha", "Engineering")
        self.assertTrue(self.service.delete_employee("E101"))
        self.assertEqual(self.service.list_employees(), [])

    def test_blank_name_is_rejected(self):
        with self.assertRaises(ValueError):
            self.service.add_employee("E102", " ", "Finance")

if __name__ == "__main__":
    unittest.main()
