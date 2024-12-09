from book_library import Book, Library


def create_books():
    book_1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
    book_2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")
    book_3 = Book("War and Peace", "Leo Tolstoy", "7593280294596878")
    book_4 = Book("Crime and Punishment", "Fyodor Dostoevsky", "89048990t8938796y865")
    return [book_1, book_2, book_3, book_4]


def add_books_to_library(library, books):
    for book in books:
        library.add_book(book)


def check_out_book(book):
    book.check_out()
    print(f"{book.title} has been checked out: {book.is_checked_out}")


def check_in_book(book):
    book.check_in()
    print(f"{book.title} has been checked in: {book.is_checked_out}")


def remove_books(library, books):
    for book in books:
        library.remove_book(book.isbn)


def list_books_in_library(library):
    print("Listing available books in library:")
    library.list_books()


def start():
    library = Library()
    books = create_books()

    add_books_to_library(library, books)
    list_books_in_library(library)

    print("Checking out a book:")
    check_out_book(books[0])

    print("Checking in a book:")
    check_in_book(books[0])

    print("Removing books:")
    remove_books(library, books[:2])
    list_books_in_library(library)


if __name__ == '__main__':
    start()
