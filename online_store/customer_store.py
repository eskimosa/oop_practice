from shopping_cart import ShoppingCart
from store import Store
from product_store import Product


class Customer:
    def __init__(self, name: str, email: str, customer_id: str) -> None:
        self.name = name
        self.email = email
        self.customer_id = customer_id
        self.shopping_cart = ShoppingCart()

    def view_products(self, store: Store):
        return store.list_products()

    def add_product_to_cart(self, product: Product, quantity: int):
        if product.quantity >= quantity:
            self.shopping_cart.add_product(product, quantity)
            return f"{quantity} of {product.name} added to cart"
        return f'Not enough product in stock'

    def remove_product_from_cart(self, product: Product):
        self.shopping_cart.remove_product(product)
        return f"{product.name} removed from cart"

    def view_cart(self):
        return self.shopping_cart

    def proceed_to_checkout(self, store: Store):
        store.process_purchase(self)

    def __str__(self):
        return f"Customer: {self.name}, Email: {self.email}, Cart: {self.view_cart()}"
