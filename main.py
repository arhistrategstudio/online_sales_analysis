from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop", 89990.00, 5))
manager.add_product(Product("Mis", 2490.00, 20))
manager.add_product(Product("Tastatura", 4990.00, 12))
manager.add_product(Product("Monitor", 24990.00, 7))

manager.show_all_products()
manager.total_inventory_value()
