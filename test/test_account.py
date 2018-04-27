import unittest

from src.account import Account

class TestAccount(unittest.TestCase):

    def test_movements(self):
        a = Account()
        a.deposit(110)
        self.assertEqual(110, a.get_balance())
        a.withdraw(10)
        self.assertEqual(100, a.get_balance())

    def test_withdraw_exception(self):
        with self.assertRaises(ValueError):
            a = Account()
            a.withdraw(10)

if __name__ == '__main__':
    unittest.main()