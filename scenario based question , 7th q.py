class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def category(self):
        return "Expensive" if self.price >= 1000 else "Affordable"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display(self):
        for product in self.products:
            print(product.product_id, product.name, product.price, product.category())


inventory = Inventory()

inventory.add_product(Product(101, "Laptop", 55000))
inventory.add_product(Product(102, "Mouse", 500))
inventory.add_product(Product(103, "Keyboard", 1500))

inventory.display()
