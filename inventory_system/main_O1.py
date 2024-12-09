from inventory_O1 import Inventory
from product_O1 import Product
from typing import List


def create_products():
    product_1 = Product('Apple', 100, 100)
    product_2 = Product('Banana', 0.30, 50)
    product_3 = Product('Orange', 0.75, 30)
    return [product_1, product_2, product_3]


def add_products_to_inventory(inventory: Inventory, products: List[Product]):
    for product in products:
        inventory.add_product(product)


def remove_products_from_inventory(inventory, products_name):
    print(f'Removing product {products_name} from inventory:')
    result = inventory.remove_product(products_name)
    print(f'Removed {result} from inventory.')


def update_product_quantity(product, quantity):
    print(f'Updating quantity of {product.name} by {quantity}:')
    product.update_quantity(quantity)


def list_products_in_inventory(inventory):
    print('Listing products in inventory...')
    print(inventory.list_products())


def find_products_in_inventory(inventory, product_name):
    print(f'Looking for {product_name} in inventory...')
    print(inventory.find_product(product_name))


def apply_discount(product, discount):
    print(f'Applying discount {discount} to {product.name}')
    new_price = product.apply_discount(discount)
    print(f'Updated price: {new_price}')


def total_inventory(inventory):
    print('Printing Total inventory value:')
    print(inventory.total_inventory_value())


def start():
    inventory = Inventory()
    products = create_products()

    add_products_to_inventory(inventory, products)

    list_products_in_inventory(inventory)
    remove_products_from_inventory(inventory, 'Banana')
    update_product_quantity(products[0], -10)
    apply_discount(products[0], 0.75)

    list_products_in_inventory(inventory)
    update_product_quantity(products[0], -91)
    list_products_in_inventory(inventory)
    update_product_quantity(products[0], -90)
    update_product_quantity(products[0], -10)
    find_products_in_inventory(inventory, products[2].name)
    find_products_in_inventory(inventory, 'Apple')
    find_products_in_inventory(inventory, 'Banana')
    list_products_in_inventory(inventory)

    total_inventory(inventory)


if __name__ == '__main__':
    start()

