class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @title.setter
    def title(self, title):
        self.__title = title

    @author.setter
    def author(self, author):
        self.__author = author

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn