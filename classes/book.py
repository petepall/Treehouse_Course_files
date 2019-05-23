class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Bookcase:
    def __init__(self, books=None):
        self.books = books

    @classmethod
    def crete_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))

        return cls(books)


bc = Bookcase.crete_bookcase(
    [('Moby-Dick', 'Herman Melville'), ('Jungle book', 'Rudyard Kipling')])

print(str(bc.books[0]))
