import os
from datetime import datetime


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def __str__(self):
        return f"ID: {self.member_id} | Name: {self.name}"


class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.loan_date = datetime.now()

    def __str__(self):
        return (
            f"Book: {self.book.title} | "
            f"Borrowed By: {self.member.name} | "
            f"Date: {self.loan_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )


class LibraryManagementSystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = []

    
    def add_book(self):
        print("\n===== Add Book =====")
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")

        book = Book(book_id, title, author)
        self.books[book_id] = book

        print(f"Book added: {title}")

    def view_books(self):
        print("\n===== Book List =====")

        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            print(book)

    
    def register_member(self):
        print("\n===== Register Member =====")
        member_id = input("Enter Member ID: ")

        if member_id in self.members:
            print("Member ID already exists!")
            return

        name = input("Enter Member Name: ")

        member = Member(member_id, name)
        self.members[member_id] = member

        print(f"Member registered: {name}")

    def view_members(self):
        print("\n===== Member List =====")

        if not self.members:
            print("No members registered.")
            return

        for member in self.members.values():
            print(member)

   
    def borrow_book(self):
        print("\n===== Borrow Book =====")

        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        if member_id not in self.members:
            print("Member not found!")
            return

        book = self.books[book_id]

        if not book.available:
            print("Book is already borrowed!")
            return

        member = self.members[member_id]

        loan = Loan(book, member)
        self.loans.append(loan)

        book.available = False

        print(f"{member.name} borrowed '{book.title}'")

    def return_book(self):
        print("\n===== Return Book =====")
        book_id = input("Enter Book ID: ")

        for loan in self.loans:
            if loan.book.book_id == book_id:
                loan.book.available = True
                self.loans.remove(loan)

                print(f"Book returned: {loan.book.title}")
                return

        print("Loan record not found!")

    def view_loans(self):
        print("\n===== Loan Records =====")

        if not self.loans:
            print("No active loans.")
            return

        for loan in self.loans:
            print(loan)

    
    def display_menu(self):
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Loans")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.register_member()

            elif choice == "3":
                self.borrow_book()

            elif choice == "4":
                self.return_book()

            elif choice == "5":
                self.view_books()

            elif choice == "6":
                self.view_members()

            elif choice == "7":
                self.view_loans()

            elif choice == "8":
                print("Exiting system...")
                break

            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    system = LibraryManagementSystem()

    
    system.books["0009"] = Book("0009", "Programming 1", "jay Cris ")
    system.books["1002"] = Book("1232", "Data Structures", "Rhandie Guan")

    system.members["Aldred Valdez"] = Member("M541", "James")
    system.members["aloha"] = Member("M392", " Trixie ")

    system.run()