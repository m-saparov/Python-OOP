class Book:
    def __init__(self, title, author, is_read):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print(f"'{self.title}' nomli kitob o'qilgan deb belgilandi.")

    def status(self):
        if self.is_read:
            print("O'qilgan")
        else:
            print("O'qilmagan")


book1 = Book("1984", "George Orwell", False)
book2 = Book("Harry Potter", "J.K. Rowling", True)

book1.status()
book1.mark_as_read()
book1.status()

book2.status()
