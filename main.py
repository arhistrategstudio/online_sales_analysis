import random

from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

manager.add_product(Product("Gaming laptop", 89990.00, 3))
manager.add_product(Product("Bezicni mis", 2490.00, 25))
manager.add_product(Product("Mehanicka tastatura", 4990.00, 10))
manager.add_product(Product("Monitor 27 inch", 24990.00, 4))

cart = Cart()
for product in random.sample(manager.products, 3):
    cart.add_to_cart(product)

cart.show_cart()
