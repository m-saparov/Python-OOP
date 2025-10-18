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
            print(f"{self.title} - O'qilgan")
        else:
            print(f"{self.title} - O'qilmagan")



book_1 = Book("Book-1", "Muallif A", False)
book_2 = Book("Book-2", "Muallif B", False)
book_3 = Book("Book-3", "Muallif C", True)
book_4 = Book("Book-4", "Muallif D", False)

# o'qildi qilamiz 1 va 2 kitoblarni
book_1.mark_as_read()
book_2.mark_as_read()

print("\nKitoblar holati:")
book_1.status()
book_2.status()
book_3.status()
book_4.status()