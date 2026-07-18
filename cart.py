class Cart:
    """Predstavlja korpu kupca."""

    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        """Dodaje proizvod u korpu."""
        self.cart_items.append(product)
        print(f"U korpu dodat: {product.name}")

    def total_price(self):
        """Racuna ukupan iznos za naplatu."""
        return sum(product.price for product in self.cart_items)

    def show_cart(self):
        """Prikazuje sadrzaj korpe."""
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        print("--- Sadrzaj korpe ---")
        for product in self.cart_items:
            print(f"{product.name} - {product.price:.2f} RSD")
        print(f"Za naplatu: {self.total_price():.2f} RSD")
