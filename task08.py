
class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self):
        have_product = "tugagan ❌"
        if self.in_stock:
            have_product = "mavjud ✅"

        print(f"{self.name} omborda {have_product}")

pr1 = Product("AirPods", 99, "Elektronika", True)
pr2 = Product("Iphone 13", 550, "telefon", False)

pr1.check_stock()
pr2.check_stock()