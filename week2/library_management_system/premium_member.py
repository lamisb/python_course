from week2.library_management_system.member import Member

class PremiumMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)

    def borrow_book(self,book):
        if self._borrowed_books_number < 5:
           super().borrow_book(book)
        else:
            print("Premium members can borrow a maximum of 5 books.")