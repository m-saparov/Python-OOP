class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} hisobida: {self.balance}$")

    def get_balance(self):
        return self.balance

a1 = BankAccount("user-1", 1200)
a2 = BankAccount("user-2", 850)
a3 = BankAccount("user-3", 600)
a4 = BankAccount("user-4", 2400)
a5 = BankAccount("user-5", 1500)

accounts = [a1, a2, a3, a4, a5]

total = sum(acc.get_balance() for acc in accounts)
print(f"Jami balans: {total}$")
