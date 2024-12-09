from book_library import Book, Library


def start():
    library = Library()

    # Create books
    book_1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
    book_2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")
    book_3 = Book("War and Peace", "Leo Tolstoy", "7593280294596878")
    book_4 = Book("Crime and Punishment", "Fyodor Dostoevsky", "89048990t8938796y865")

    # Add books to library
    library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)
    library.add_book(book_4)

    # List books
    print("Listing available books in library:")
    library.list_books()

    # Check out a book
    print("Checking out a book:")
    book_1.check_out()
    print(f"{book_1.title} has been checked out: {book_1.is_checked_out}")
    print('-----------------------------------------------------------')

    # Find a book by ISBN
    print("Looking for a book with isdn: 9780316769488")
    book = library.find_book("9780316769488")
    print(f"{book.title} with isbn {book.isbn} has been found")
    print('-----------------------------------------------------------')

    print("Looking for a book with isdn: 89048990t8938796y865")
    book_2 = library.find_book("89048990t8938796y865")
    print(f"{book_2.title} with isbn {book_2.isbn} has been found")
    print('-----------------------------------------------------------')

    # Check in the book
    print("Checking in a book:")
    book_1.check_in()
    print(f"{book_1.title} has been checked in: {book_1.is_checked_out}")
    print('-----------------------------------------------------------')

    print("Checking out a book:")
    book_3.check_out()
    print(f"{book_3.title} has been checked out: {book_3.is_checked_out}")
    print('-----------------------------------------------------------')

    # Remove a book
    print("Removing a book with isdn: 9780316769488")
    library.remove_book("9780316769488")
    print("Removing a book with isdn: 9780060935467")
    library.remove_book("9780060935467")

    print("-----------------")
    print("Listing available books in library after removing books:")
    library.list_books()


if __name__ == '__main__':
    start()
