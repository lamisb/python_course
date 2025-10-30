from week2.library_management_system.member import Member
from week2.library_management_system.book import Book
from week2.library_management_system.library import Library

class LibraryManager(Library):
    def __init__(self):
        self.__book_repository = []
        self.__members = []

    def add_book(self,book):
        print(f"Adding book: {book.title}")
        self.__book_repository.append(book)
        self.__book_repository.sort(key=lambda b: b.title)

    def print_books(self):
        print("Books in the library:")
        for book in self.__book_repository:
            print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")

    def add_member(self,member):
        print(f"Adding member:  {member.name}")
        self.__members.append(member)

    def borrow_book(self,member, book):
        if(member in self.__members) and (book in self.__book_repository):
            print(f"Member {member.name} is borrowing book {book.title}")
            member.borrow_book(book)
            self.__book_repository.remove(book)
        else:
            print("Either member is not registered or book is not available.")

    def return_book(self,member, book):
        member.return_book(book)
        self.__book_repository.append(book)

print(__name__)
if __name__ == "__main__":
    # Example usage
    library_manager = LibraryManager()

    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455")
    book4 = Book("Strong Ground", "Brene Braun", "6677889900")

    library_manager.add_book(book1)
    library_manager.add_book(book2)
    library_manager.add_book(book3)
    library_manager.add_book(book4)

    library_manager.print_books()

    member1 = Member(1, "Alice")
    member2 = Member(2, "Bob")

    library_manager.add_member(member1)
    library_manager.add_member(member2)

    library_manager.borrow_book(member1, book1)
    library_manager.return_book(member1, book1)