class BankAccount:
    def __init__(self, balance: float, amount: float = None) -> None:
        self.balance = balance
        self.amount = amount

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f'Amount {amount} is greater than balance')

    def get_balance(self) -> float:
        return self.balance

    def __str__(self):
        self.balance = round(self.balance, 2)

