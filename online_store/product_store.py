class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_stock(self, amount: int):
        try:
            if amount < 0 and (self.quantity + amount) < 0:
                raise ValueError(f'Not enough stock for {self.name}, current stock is {self.quantity}')
            self.quantity += amount
            return f'Updated stock: {self.quantity}'
        except ValueError as e:
            return e

    def apply_discount(self, percentage: float):
        try:
            if percentage < 0:
                raise ValueError(f'Percentage should be positive number.')
            discount = (self.price * percentage) / 100
            self.price -= discount
            return f'Discounted price: {self.price}'
        except ValueError as e:
            return e

    def __str__(self) -> str:
        return f'{self.name}, {self.price}, {self.quantity}'

