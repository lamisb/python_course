from week2.library_management_system.member import Member

class RegularMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)

    def borrow_book(self, book):
        if self._borrowed_books_number <3:
            super.borrow_book(book)
        else:
            print("Regular members can borrow a maximum of 3 books.")