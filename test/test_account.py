import unittest

from openbiz.account import Account

class TestAccount(unittest.TestCase):

    def test_movements(self):
        account = Account()
        account.deposit(110)
        self.assertEqual(110, account.get_balance())
        account.withdraw(10)
        self.assertEqual(100, account.get_balance())

    def test_withdraw_exception(self):
        with self.assertRaises(ValueError):
            account = Account()
            account.withdraw(10)

if __name__ == '__main__':
    unittest.main()