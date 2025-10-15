from library_system import Book, EBook, PrintBook, Library

def main():
    library = Library()

    # Creating books with matching details
    book1 = Book("Pride and Prejudice", "Jane Austen")
    ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)  # 500KB
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Adding books to the library
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)

    # Listing books (expected format)
    library.list_books()

if __name__ == "__main__":
    main()
