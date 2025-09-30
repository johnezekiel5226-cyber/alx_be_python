class Book:
    def __init__(self, title, author):
        self.title = title               # Public attribute
        self.author = author             # Public attribute
        self._is_checked_out = False     # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []   # Private list holding Book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f'"{title}" has been checked out.'
                else:
                    return f'"{title}" is already checked out.'
        return f'Book titled "{title}" not found in the library.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f'"{title}" has been returned.'
                else:
                    return f'"{title}" was not checked out.'
        return f'Book titled "{title}" not found in the library.'

    def list_available_books(self):
        available = [
            f'{book.title} by {book.author}'
            for book in self._books if book.is_available()
        ]
        return available if available else ["No books available."]
