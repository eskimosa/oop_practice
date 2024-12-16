from product_store import Product


class ShoppingCart:
    def __init__(self):
        self.cart_items = {}

    def add_product(self, product: Product, quantity: int):
        try:
            if product in self.cart_items:
                total_quantity = self.cart_items[product] + quantity
                if total_quantity <= product.quantity:
                    self.cart_items[product] = total_quantity
                else:
                    raise ValueError(f'Not enough stock for {product.name}')
            else:
                if quantity <= product.quantity:
                    self.cart_items[product] = quantity
                else:
                    raise ValueError(f'Not enough stock for {product.name}')
        except ValueError as e:
            return e

    def remove_product(self, product):
        try:
            if product in self.cart_items:
                del self.cart_items[product]
            return ValueError(f'{product.name} is not in the cart')
        except ValueError as e:
            return e

    def calculate_total(self):
        return sum(product.price * product.quantity for product, quantity in self.cart_items.items())

    def apply_discount(self, percentage: float):
        try:
            total = self.calculate_total()
            if percentage < 0:
                raise ValueError(f'Percentage {percentage} should be positive')
            discount = (total * percentage) / 100
            discounted_total = total - discount
            return discounted_total
        except ValueError as e:
            return e

    def empty_cart(self):
        self.cart_items.clear()

    def __str__(self):
        return "\n".join(f"{product.name}: {quantity}" for product, quantity in self.cart_items.items())
