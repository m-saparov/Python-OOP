class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        print(f"{self.title} - {'O\'qilgan' if self.is_read else 'O\'qilmagan'}")

b1 = Book("book-1", "author-1")
b2 = Book("book-2", "author-2")
b3 = Book("book-3", "author-3")
b4 = Book("book-4", "author-4")
b5 = Book("book-5", "author-5")

books = [b1, b2, b3, b4, b5]

b2.mark_as_read()
b4.mark_as_read()

for book in books:
    book.status()

print("\nO‘qilgan kitoblar:")
for book in books:
    if book.is_read:
        print(book.title)
