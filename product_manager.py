class ProductManager:
    """Upravlja listom svih dostupnih proizvoda u prodavnici."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Dodaje proizvod u listu dostupnih proizvoda."""
        self.products.append(product)
        print(f"Dodat proizvod: {product.name}")

    def show_all_products(self):
        """Prikazuje sve proizvode iz inventara."""
        if not self.products:
            print("Inventar je prazan.")
            return
        print("--- Lista proizvoda ---")
        for product in self.products:
            product.display_info()

    def remove_product(self, name):
        """Uklanja proizvod iz inventara prema imenu."""
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(f"Uklonjen proizvod: {product.name}")
                return True
        print(f"Proizvod '{name}' nije pronadjen u inventaru.")
        return False

    def total_inventory_value(self):
        """Racuna ukupnu vrednost svih proizvoda u inventaru."""
        total = sum(product.total_value() for product in self.products)
        print(f"Ukupna vrednost inventara: {total:.2f} RSD")
        return total
