
class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

pr1 = Product("olma", 23, "meva", True)
pr2 = Product("Sabzi", 3, "sabzavot", False)

print(f"{pr1.name} narxi: {pr1.price} ming so'm")
print(f"{pr2.name} narxi: {pr2.price} ming so'm")