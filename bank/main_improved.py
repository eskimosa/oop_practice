from bank_account_improved import BankAccount


def start():
    my_account = BankAccount(100000)
    print(my_account)

    my_account.deposit(10000)
    print("After depositing 10,000:")
    print(my_account)

    my_account.withdraw(10000)
    print("After withdrawing 10,000:")
    print(my_account)

    my_account.withdraw(110000)
    print("Attempted to withdraw 110,000:")
    print(my_account)

    my_account.withdraw(100000)
    print("After withdrawing 100,000:")
    print(my_account)


if __name__ == '__main__':
    start()
