from product_store import Product
from customer_store import Customer
from store import Store


def start():
    # Create a Store
    store = Store()

    # Add Products to the Store
    product1 = Product("Laptop", 1500.00, 10)
    product2 = Product("Phone", 800.00, 5)
    product3 = Product("Headphones", 150.00, 0)  # Out of stock product

    store.add_product(product1)
    store.add_product(product2)
    store.add_product(product3)

    # Display products in store
    print("\nStore Products:")
    print(store)

    # Create a Customer
    customer1 = Customer("Alice", "alice@example.com", "C001")
    store.add_customer_to(customer1)

    # Customer views products in store
    print("\nCustomer views products:")
    print(customer1.view_products(store))

    # Add product to cart (valid case)
    print("\nAdding Laptop to cart:")
    print(customer1.add_product_to_cart(product1, 2))  # Adding 2 laptops
    print(customer1.add_product_to_cart(product1, 5))
    # Try adding more products than available stock
    print("\nAdding more Phones than available stock:")
    print(customer1.add_product_to_cart(product2, 6))  # Only 5 Phones available

    # Try adding an out of stock product
    print("\nAdding out of stock product:")
    print(customer1.add_product_to_cart(product3, 1))  # Headphones out of stock

    # View Customer's cart
    print("\nCustomer's shopping cart:")
    print(customer1.view_cart())

    # Remove product from cart (valid case)
    print("\nRemoving Laptop from cart:")
    print(customer1.remove_product_from_cart(product1))

    # Attempt to remove a product not in the cart
    print("\nTrying to remove a product not in the cart:")
    print(customer1.remove_product_from_cart(product2))  # Not in cart yet

    # View updated cart after removing product
    print("\nCustomer's updated shopping cart:")
    print(customer1.view_cart())

    # Add products again and proceed to checkout
    print("\nAdding Phone to cart:")
    print(customer1.add_product_to_cart(product2, 3))  # Adding 3 Phones

    print("\nProceeding to checkout:")
    customer1.proceed_to_checkout(store)

    # View store products after checkout to confirm stock is updated
    print("\nStore products after checkout:")
    print(store)

    # Customer applies a discount and checks total
    print("\nAdding Phone to cart for discount test:")
    customer1.add_product_to_cart(product2, 2)

    print("\nApplying 10% discount to cart:")
    print(f"Discounted total: {customer1.shopping_cart.apply_discount(10)}")

    # Edge Case: Applying negative discount
    print("\nApplying -5% discount (invalid case):")
    print(customer1.shopping_cart.apply_discount(-5))

    # Edge Case: Update stock with invalid value
    print("\nUpdating stock with invalid value (-20 for Laptops):")
    print(product1.update_stock(-20))

    # Edge Case: Invalid percentage for product discount
    print("\nApplying invalid percentage (-10%) for product discount:")
    print(product2.apply_discount(-10))

    # Final Cart and Store Status
    print("\nFinal Customer's Cart:")
    print(customer1.view_cart())

    print("\nFinal Store Products:")
    print(store)


if __name__ == "__main__":
    start()
