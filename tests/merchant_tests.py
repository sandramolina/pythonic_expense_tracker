import unittest
from models.merchant import *

class TestMerchant(unittest.TestCase):
    def setUp(self):
        self.merchant1 = Merchant("Tesco")

    def test_get_name(self):
        self.assertEqual("Tesco", self.merchant1.get_merchant_name())

    def test_get_id(self):
        self.assertIsNone(self.merchant1.get_merchant_id())