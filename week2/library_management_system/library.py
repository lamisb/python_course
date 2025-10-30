from abc import ABC, abstractmethod

class Library(ABC):

    @abstractmethod
    def add_book(self,book):
        pass

    @abstractmethod
    def borrow_book(self,member, book):
        pass

    @abstractmethod
    def return_book(self,member, book):
        pass
