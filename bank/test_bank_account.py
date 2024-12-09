import unittest
from bank_account import BankAccount


class TestMainV1(unittest.TestCase):
    def test_init_case(self):
        my_account = BankAccount(100000)
        assert my_account.balance == 100000

    def test_deposit_case(self):
        my_account = BankAccount(120000)
        my_account.deposit(100000)
        assert my_account.balance == 220000

    def test_neutral_withdraw_case(self):
        my_account = BankAccount(100000)
        my_account.withdraw(100000)
        assert my_account.balance == 0

    def test_negative_withdraw_case(self):
        my_account = BankAccount(150000)
        my_account.withdraw(170000)
        assert my_account.balance == 150000
