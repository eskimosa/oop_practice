from typing import Union, Any
from product import Product


class Inventory:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product_name: str) -> None:
        for product in self.products:
            if product.name == product_name:
                return self.products.remove(product)
        else:
            print(f"{product_name} not found in inventory")

    def list_products(self) -> str:
        if len(self.products) == 0:
            print("No products found in inventory")
        return "\n".join(str(product) for product in self.products)

    def find_product(self, product_name: str) -> Union[str, Any]:
        for product in self.products:
            if product.name == product_name:
                return product
        else:
            return f"{product_name} not found in inventory"

    def total_inventory_value(self) -> str:
        total = 0
        for product in self.products:
            inv_value = product.quantity * product.price
            total += inv_value
        return f"{total:.2f}"

    def __str__(self) -> str:
        return "\n".join(str(product) for product in self.products)

