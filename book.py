from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_author(self):
        pass

    def __str__(self):
        return f'"{self.title}" ({self.author})'

class FictionBook(Book):
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

class ScienceBook(Book):
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

class ArtBook(Book):
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author