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
    
    def show_balance(self):
        print(f"Balansingiz: {self.balance} so'm")


acc1 = BankAccount("Account-1", 50000)
acc2 = BankAccount("Account-2", 120000)
acc3 = BankAccount("Account-3", 80000)

print("\n#1")
acc1.show_balance()
acc1.deposit(5000)
acc1.withdraw(33000)
acc1.show_balance()

print("\n#2")
acc2.show_balance()
acc2.withdraw(20000)
acc2.deposit(10000)
acc2.show_balance()

print("\n#3")
acc3.show_balance()
acc3.deposit(15000)
acc3.withdraw(90000)
acc3.show_balance()
