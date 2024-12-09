from typing import Union, Any
from product_O1 import Product


class Inventory:
    def __init__(self) -> None:
        self.products = {}

    def add_product(self, product: Product) -> None:
        self.products[product.name] = product

    def remove_product(self, product_name: str) -> str:
        if product_name in self.products:
            del self.products[product_name]
            return f'Product {product_name} has been removed from inventory'
        else:
            return f"{product_name} not found in inventory"

    def list_products(self) -> str:
        if len(self.products) == 0:
            print("No products found in inventory")
        return "\n".join(f'(Key: {name}, Value: {product})' for name, product in self.products.items())

    def find_product(self, product_name: str) -> Union[str, Any]:
        if product_name in self.products:
            return self.products.get(product_name)
        else:
            return f"{product_name} not found in inventory"

    def total_inventory_value(self) -> str:
        total = 0
        for product in self.products.values():
            inv_value = product.quantity * product.price
            total += inv_value
        return f"{total:.2f}"

    def __str__(self) -> str:
        return "\n".join(f'{name}: {product}' for name, product in self.products.items())

