class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Initializes a Book instance with title, author, and year.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when the Book object is deleted.
        """
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book instance.

        Returns:
            str: A string in the format "(title) by (author), published in (year)".
        """
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation of the Book instance that can
        be used to recreate the object.

        Returns:
            str: A string in the format:
                 Book('title', 'author', year)
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

