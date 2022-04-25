import unittest

from models.budget import Budget

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget(10000, "Yearly")
        self.total_expenses1 = 8000
        self.total_expenses2 = 9999
        self.total_expenses3 = 10000
        self.total_expenses4 = 11000
    
    def test_get_budget(self):
        self.assertEqual(10000, self.budget.get_total_budget())

    def test_get_periodicity(self):
        self.assertEqual("Yearly", self.budget.get_budget_periodicity())

    def test_get_id(self):
        self.assertIsNone(self.budget.get_budget_id())
    
    def test_budget_status(self):
        budget_status = self.budget.budget_status(self.total_expenses1)
        self.assertEqual(2000, budget_status)
    
    def test_budget_alert_over10(self):
        budget_status = self.budget.budget_status(self.total_expenses1)
        alert = self.budget.budget_alert(budget_status)
        self.assertEqual("Your budget is 2000", alert)
    
    def test_budget_alert_minor10(self):
        budget_status = self.budget.budget_status(self.total_expenses2)
        alert = self.budget.budget_alert(budget_status)
        self.assertEqual("Your budget is 1 and you are running out of money", alert)
    
    def test_budget_alert_0(self):
        budget_status = self.budget.budget_status(self.total_expenses3)
        alert = self.budget.budget_alert(budget_status)
        self.assertEqual("Your budget is 0, you have run out of money", alert)

    def test_budget_alert_negative(self):
        budget_status = self.budget.budget_status(self.total_expenses4)
        alert = self.budget.budget_alert(budget_status)
        self.assertEqual("Your budget is -1000, you are overspending", alert)