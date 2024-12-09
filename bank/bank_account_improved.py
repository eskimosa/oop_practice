class BankAccount:
    def __init__(self, balance: float = 0.0) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        elif amount > self.balance:
            raise ValueError(f'Amount {amount} is greater than balance')
        else:
            self.balance -= amount

    def get_balance(self) -> float:
        return round(self.balance, 2)

    def __str__(self) -> str:
        return f"BankAccount balance: {self.get_balance()}"

