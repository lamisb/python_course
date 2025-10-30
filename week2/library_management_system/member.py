class Member:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self._borrowed_books_number = 0
        self._books_borrowed = []

    @property
    def member_id(self):
        return self.__member_id

    @property
    def name(self):
        return self.__name

    @member_id.setter
    def member_id(self, member_id):
        self.__member_id = member_id

    @name.setter
    def name(self, name):
        self.__name = name

    def borrow_book(self,book):
        self._borrowed_books_number += 1
        self._books_borrowed.append(book)

    def return_book(self,book):
        if book in self._books_borrowed:
            self._borrowed_books_number -= 1
            self._books_borrowed.remove(book)
        else:
            print("This book was not borrowed by the member.")
