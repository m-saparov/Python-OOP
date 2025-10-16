
class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active
    
    def activate(self):
        self.is_active = True
        print(f"{self.username} foydalanuvchi faollashtirildi!")
    def deactivate(self):
        self.is_active = False
        print(f"{self.username} foydalanuvchi nofoallashtirildi!")

user1 = User("mehroj21", "mehroj@gmail.com", False)
user2 = User("dilshod_88", "dilshod@mail.ru", True)

user1.activate()
user2.activate()

user1.deactivate()
user2.deactivate()