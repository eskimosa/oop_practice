from typing import Union


class Book:
    def __init__(self, title: str, author: str, isbn: str, is_checked_out: bool = False) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
        else:
            print(f"{self.title} is already checked out.")

    def check_in(self):
        if self.is_checked_out:
            self.is_checked_out = False
        else:
            print(f"{self.title} is already checked in.")

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, isbn: str) -> None:
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)

    def find_book(self, isbn: str) -> Union[Book, None]:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None  # Explicitly return None if the book isn't found

    def list_books(self) -> None:
        for book in self.books:
            print(f"{book.title} - {book.author} - {book.isbn} - {book.is_checked_out}")

    def __str__(self) -> str:
        return "\n".join(str(book) for book in self.books)











