import unittest

from models.expense import *
from models.category import *
from models.merchant import *

class TestExpense(unittest.TestCase):
    def setUp(self):
        self.merchant1 = Merchant("Tesco")
        self.category1 = Category("Groceries")
        self.expense1 = Expense("2022-04-25", self.merchant1, self.category1, 120, "Dinner with Khal Drogo")

    def test_get_date(self):
        self.assertEqual("2022-04-25", self.expense1.date)
    
    def test_get_merchant(self):
        self.assertEqual(self.merchant1, self.expense1.get_expense_merchant())

    def test_get_category(self):
        self.assertEqual(self.category1, self.expense1.get_expense_category())

    def test_get_amount(self):
        self.assertEqual(120, self.expense1.get_expense_amount())

    def test_get_description(self):
        self.assertEqual("Dinner with Khal Drogo", self.expense1.get_expense_description())

    def test_get_id(self):
        self.assertIsNone(self.expense1.get_expense_id())