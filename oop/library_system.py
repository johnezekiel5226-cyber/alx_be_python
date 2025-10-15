# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: {self.title} by {self.author}"

    def __str__(self):
        return self.get_details()


# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def get_details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}MB"

    def __str__(self):
        return self.get_details()


# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.page_count}"

    def __str__(self):
        return self.get_details()


# Library class using composition
class Library:
    def __init__(self):
        self.books = []  # Stores instances of Book, EBook, or PrintBook

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added.")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")  # Uses __str__ method
