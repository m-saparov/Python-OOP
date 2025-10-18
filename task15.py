class Product:
    def __init__(self, name, price, is_stock):
        self.name = name
        self.price = price
        self.is_stock = is_stock


p1 = Product("olma", 23, True)
p2 = Product("olcha", 17, False)
p3 = Product("sabzi", 3.5, True)
p4 = Product("daftar", 4.5, False)
p5 = Product("ruchka", 1.5, True)

products = [p1, p2, p3, p4, p5]

true_p = list(filter(lambda p: p.is_stock, products))

summa_t = sum(p.price for p in true_p)
print(summa_t)
