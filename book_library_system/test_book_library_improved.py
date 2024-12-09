import unittest
from book_library_improved import Book, Library


class TestBookLibrary(unittest.TestCase):
    def test_init_case(self):
        book_1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
        self.assertEqual(book_1.title, "The Catcher in the Rye")
        book_2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")
        self.assertEqual(book_2.title, "To Kill a Mockingbird")
        self.assertEqual(book_2.author, "Harper Lee")
        book_3 = Book("War and Peace", "Leo Tolstoy", "7593280294596878")
        self.assertEqual(book_3.title, "War and Peace")
        self.assertEqual(book_3.author, "Leo Tolstoy")
        book_4 = Book("Crime and Punishment", "Fyodor Dostoevsky", "89048990t8938796y865")
        self.assertEqual(book_4.title, "Crime and Punishment")
        self.assertEqual(book_4.author, "Fyodor Dostoevsky")
        self.assertEqual(book_4.isbn, "89048990t8938796y865")

    def test_add_book(self):
        library = Library()
        book_1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
        book_2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")
        book_3 = Book("War and Peace", "Leo Tolstoy", "7593280294596878")
        book_4 = Book("Crime and Punishment", "Fyodor Dostoevsky", "89048990t8938796y865")

        library.add_book(book_1)
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0].title, "The Catcher in the Rye")
        library.add_book(book_2)
        self.assertEqual(len(library.books), 2)
        self.assertEqual(library.books[1].title, "To Kill a Mockingbird")
        library.add_book(book_3)
        self.assertEqual(len(library.books), 3)
        self.assertEqual(library.books[2].author, "Leo Tolstoy")
        library.add_book(book_4)
        self.assertEqual(len(library.books), 4)
        self.assertEqual(library.books[3].isbn, "89048990t8938796y865")

        library.list_books()
        self.assertEqual(library.books[0].title, "The Catcher in the Rye")
        self.assertEqual(len(library.books), 4)

        book_1.check_out()
        self.assertEqual(book_1.is_checked_out, True)

        book = library.find_book("9780316769488")
        self.assertEqual(book.title, "The Catcher in the Rye")

        book_1.check_in()
        self.assertEqual(book_1.is_checked_out, False)

        library.remove_book("9780316769488")
        self.assertIsNone(library.find_book("9780316769488"))

        self.assertEqual(len(library.books), 3)

    def test_find_non_existent_book(self):
        library = Library()
        book = library.find_book("1234567890")
        self.assertIsNone(book)


        
