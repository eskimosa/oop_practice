
class Book:
    def __init__(self, title: str, author: str, isbn: str, is_checked_out: bool = False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def check_out(self) -> None:
        self.is_checked_out = True

    def check_in(self) -> None:
        self.is_checked_out = False

    def __str__(self) -> str:
        return f"{self.title} - {self.author} - {self.isbn} - {self.is_checked_out}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)

    def find_book(self, isbn: str) -> Book:
        for book in self.books:
            if book.isbn == isbn:
                return book

    def list_books(self):
        for book in self.books:
            print(f"{book.title} - {book.author} - {book.isbn} - {book.is_checked_out}")

    def __str__(self):
        return f"{self.books}"









