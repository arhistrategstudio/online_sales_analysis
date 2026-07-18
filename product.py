class Product:
    """Predstavlja jedan proizvod u online prodavnici."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Prikazuje osnovne informacije o proizvodu."""
        print(f"Proizvod: {self.name} | Cena: {self.price:.2f} RSD | Kolicina: {self.quantity}")

    def update_quantity(self, new_quantity):
        """Azurira kolicinu proizvoda na zalihama."""
        if new_quantity < 0:
            print("Kolicina ne moze biti negativna.")
            return
        self.quantity = new_quantity
        print(f"Nova kolicina za '{self.name}': {self.quantity}")

    def total_value(self):
        """Vraca ukupnu vrednost ovog proizvoda (cena * kolicina)."""
        return self.price * self.quantity
