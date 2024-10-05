class Book:
    def __init__(self, title, writer):
        self.title = title
        self.writer = writer
        self.available = True

    def __str__(self):
        return f"'{self.title}' by {self.writer} - {'Available' if self.available else 'Not Available'}"

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have successfully borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is not available.")

    def return_book(self):
        if not self.available:  # Corrected the logic
            self.available = True
            print(f"'{self.title}' has been successfully returned.")
        else:
            print(f"'{self.title}' is already available.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' by {book.writer} has been added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"'{title}' is not available in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"'{title}' is not recognized in the library system.")

    def display_available_books(self):
        print("Available books in the library:")
        available_books = [book for book in self.books if book.available]
        if available_books:
            for book in available_books:
                print(book)
        else:  # Moved the else block out of the loop
            print("No books are currently available.")

# Example Usage
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_available_books()

library.borrow_book("1984")
library.borrow_book("1984")  # Trying to borrow again to see "not available" message

library.return_book("1984")

library.display_available_books()
