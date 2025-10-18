class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"{self.name} - {self.price}$")


p1 = Product("Olma", 3, "Meva")
p2 = Product("Telefon", 450, "Elektronika")
p3 = Product("Daftar", 2.5, "Kantselyariya")
p4 = Product("Kompyuter", 800, "Elektronika")
p5 = Product("Kiyim", 120, "Moda")
p6 = Product("Televizor", 600, "Elektronika")

products = [p1, p2, p3, p4, p5, p6]

most_expensive = max(products, key=lambda p: p.price)

print("Eng qimmat mahsulot:")
most_expensive.info()
