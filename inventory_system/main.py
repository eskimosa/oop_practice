from inventory import Inventory
from product import Product


def create_products():
    product_1 = Product('Apple', 100, 100)
    product_2 = Product('Banana', 0.30, 50)
    product_3 = Product('Orange', 0.75, 30)
    return [product_1, product_2, product_3]


def add_products_to_inventory(inventory, products):
    for product in products:
        inventory.add_product(product)


def remove_products_from_inventory(inventory, products_name):
    print('Removing product from inventory:')
    inventory.remove_product(products_name)
    print(f'Removed {products_name} from inventory.')


def update_product_quantity(product, quantity):
    print(f'Updating quantity of {product.name} by {quantity}:')
    product.update_quantity(quantity)


def list_products_in_inventory(inventory):
    print('Listing products in inventory...')
    print(inventory.list_products())


def find_products_in_inventory(inventory, product):
    print(f'Looking for {product} in inventory...')
    print(inventory.find_product(product))


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
    remove_products_from_inventory(inventory, products[1].name)
    list_products_in_inventory(inventory)
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

