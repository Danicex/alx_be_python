class Book:
    """
    Represents a book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initialize a book with its title, author, and availability status.
        :param title: Title of the book.
        :param author: Author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned and available.
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is available for checkout.
        :return: True if the book is available, False otherwise.
        """
        return not self._is_checked_out


class Library:
    """
    Represents a library that manages a collection of books.
    """
    def __init__(self):
        """
        Initialize the library with an empty collection of books.
        """
        self._books = []  # Private list to store book instances

    def add_book(self, book):
        """
        Adds a new book to the library's collection.
        :param book: Instance of the Book class to add to the library.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by title if it's available.
        :param title: Title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is either not available or does not exist in the library.")

    def return_book(self, title):
        """
        Returns a book by title to the library's collection.
        :param title: Title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' is either not checked out or does not exist in the library.")

    def list_available_books(self):
        """
        Lists all available books in the library's collection.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")

