from product_store import Product


class Store:
    def __init__(self):
        self.products = {}
        self.customers = {}

    def add_product(self, product: Product):
        if product.name not in self.products:
            self.products[product.name] = product

    def list_products(self):
        if self.products:
            return '\n'.join(f'({product}' for product in self.products.values())
        return f'There are no products in Store.'

    def search_product_by_name(self, name: str):
        return self.products.get(name, 'Product not found')

    def add_customer_to(self, customer):
        # Move the import inside the method to avoid circular import
        from customer_store import Customer
        if isinstance(customer, Customer):
            if customer.customer_id not in self.customers:
                self.customers[customer.customer_id] = customer
                return f'Customer {customer.name} added to Store.'
        return f'Customer is already in the Store.'

    def process_purchase(self, customer):
        # Move the import inside the method to avoid circular import
        from customer_store import Customer
        if isinstance(customer, Customer):
            try:
                for product, quantity in customer.shopping_cart.cart_items.items():
                    if product.quantity >= quantity:
                        product.update_stock(-quantity)
                    else:
                        raise ValueError(f"Not enough stock for {product.name}")
                total_spent = customer.shopping_cart.calculate_total()
                print(f"Total spent by {customer.name}: ${total_spent:.2f}")
                customer.shopping_cart.empty_cart()
            except ValueError as e:
                raise e

    def __str__(self) -> str:
        return f'Store Products:\n{self.list_products()}'
