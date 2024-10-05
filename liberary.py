class Book:
    def __init__(self,title,writer):
        self.title=title
        self.writer=writer
        self.available=True
    def __str__(self):
        return f"'{self.title}' by {self.writer} - {'Available' if self.available else 'Not Available'}"
    def borrow(self):
        if self.available:
            self.available=False
            print(f"You have successfully borrowed '{self.title}'")
        else:
            print(f"'{self.title}' book is not available.")
    def return_book(self):
        if not self.available:
            self.available =True
            print(f"You have success fully returned '{self.title}'")
        else:
            print(f"the book is already Available")
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f"'{book.title}' by {book.writer} is added to the liberary")
    def borrow_book(self,title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"'{title}' is not available in the liberary.")
    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"'{title}' is not recognized in the liberary system .")
    def display_available_book(self):
        print("Available books in the liberary : ")
        available_books=[book for book in self.books if book.available]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available .")
liberary=Library()
book1=Book("The great Gatsby","F.Scott Fitzgerald")
book2=Book("1984","George Orwell")
book3=Book("To Kill a Mockingbird","Harper Lee")
liberary.add_book(book1)
liberary.add_book(book2)
liberary.add_book(book3)
liberary.display_available_book()
liberary.borrow_book("1984")
liberary.borrow_book("1984")
liberary.return_book("1984")
liberary.display_available_book()