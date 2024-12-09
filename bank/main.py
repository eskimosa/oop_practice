from bank_account import BankAccount


def start():
    my_account = BankAccount(100000)
    print(my_account.get_balance())
    my_account.deposit(10000)
    print(my_account.get_balance())
    my_account.withdraw(10000)
    print(my_account.get_balance())
    my_account.withdraw(110000)
    print(my_account.get_balance())
    my_account.withdraw(100000)
    print(my_account.get_balance())


if __name__ == '__main__':
    start()
