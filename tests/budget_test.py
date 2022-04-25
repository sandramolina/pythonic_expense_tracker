import unittest

from models.budget import Budget

class TestBudget(unittest.TestCase):
    def setUp(self):        
        self.budget = Budget(10000, "Yearly")

    def test_get_budget(self):
        self.assertEqual(10000, self.budget.get_total_budget())

    def test_get_periodicity(self):
        self.assertEqual("Yearly", self.budget.get_budget_periodicity())

    def test_get_id(self):
        self.assertIsNone(self.budget.get_budget_id())
    
 