class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Deposit manfiy bo'la olmaydi.")
            return
        self.balance += amount
        print(f"{amount} so'm qo'shildi. Yangi balans: {self.balance} so'm")

    def withdraw(self, amount):
        if amount < 0:
            print("Manfiy summa yechib bo'lmaydi.")
            return
        if amount > self.balance:
            print("Balansda yetarli mablag' mavjud emas.")
            return
        self.balance -= amount
        print(f"{amount} so'm yechildi. Yangi balans: {self.balance} so'm")


acc1 = BankAccount("Mehroj", 100000)
acc1.deposit(50000)
acc1.withdraw(30000)
acc1.withdraw(200000)
