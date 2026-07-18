# online_sales_analysis

Sistem za analizu prodajnih podataka u online prodavnici, napisan u Pythonu uz primenu
OOP koncepata i upravljanje verzijama kroz Git/GitHub.

## Struktura projekta

| Datoteka | Opis |
|---|---|
| `product.py` | Klasa `Product` - model jednog proizvoda |
| `product_manager.py` | Klasa `ProductManager` - upravljanje inventarom |
| `cart.py` | Klasa `Cart` - korpa kupca |
| `main.py` | Demonstracija rada celog sistema |
| `.gitignore` | Ignorisanje poverljivih podataka i snimaka ekrana |

## Klase i funkcionalnosti

### Product
Atributi: `name`, `price`, `quantity`.

- `display_info()` - prikazuje ime, cenu i kolicinu proizvoda
- `update_quantity(new_quantity)` - azurira kolicinu na zalihama
- `total_value()` - vraca ukupnu vrednost proizvoda (cena x kolicina)

### ProductManager
Atribut: `products` - lista svih dostupnih proizvoda.

- `add_product(product)` - dodaje proizvod u inventar
- `show_all_products()` - prikazuje sve proizvode
- `remove_product(name)` - uklanja proizvod prema imenu
- `total_inventory_value()` - racuna ukupnu vrednost inventara

### Cart
Atribut: `cart_items` - lista proizvoda u korpi.

- `add_to_cart(product)` - dodaje proizvod u korpu
- `total_price()` - racuna iznos za naplatu
- `show_cart()` - prikazuje sadrzaj korpe i ukupan iznos

## Pokretanje

```bash
python main.py
```

## Rad sa granama

- `main` - glavna grana
- `add-product-removal` - dodat metod za uklanjanje proizvoda (spojena u `main`)
- `add-cart-functionality` - dodata klasa `Cart` (spojena u `main`, konflikt u `main.py` resen rucno)

## Sigurnost podataka

Datoteka `config.json` sadrzi API kljuc i pristupne podatke za bazu i navedena je u
`.gitignore`, pa se ne prati sistemom za verzionisanje. Isto vazi i za sve snimke ekrana.
