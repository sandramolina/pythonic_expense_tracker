import unittest
from models.category import *

class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category1 = Category("Groceries")

    def test_get_name(self):
        self.assertEqual("Groceries", self.category1.get_category_name())

    def test_get_id(self):
        self.assertIsNone(self.category1.get_category_id())
