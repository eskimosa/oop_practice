from typing import Union


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount: int) -> Union[str, int]:
        if amount < 0 and self.quantity == 0:
            print("There is no product available")
        elif (self.quantity + amount) < 0:
            print("Requested amount is higher than the product available.")
        else:
            self.quantity += amount
            return self.quantity

    def apply_discount(self, percentage: float) -> float:
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
        return self.price

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}'


