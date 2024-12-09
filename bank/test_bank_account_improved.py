import unittest
from bank_account_improved import BankAccount


class TestBankAccountImproved(unittest.TestCase):
    def test_init_case(self):
        my_account = BankAccount(100000)
        self.assertEqual(my_account.balance, 100000)

    def test_deposit_case(self):
        my_account = BankAccount(120000)
        my_account.deposit(100000)
        self.assertEqual(my_account.balance, 220000)

    def test_neutral_withdrawal_case(self):
        my_account = BankAccount(100000)
        my_account.withdraw(100000)
        self.assertEqual(my_account.balance, 0)

    def test_negative_withdrawal_case(self):
        my_account = BankAccount(150000)
        with self.assertRaises(ValueError):
            my_account.withdraw(170000)
        self.assertEqual(my_account.balance, 150000)

    def test_withdrawal_positive_check(self):
        my_account = BankAccount(100)
        with self.assertRaises(ValueError):
            my_account.withdraw(-50)

    if __name__ == '__main__':
        unittest.main()
