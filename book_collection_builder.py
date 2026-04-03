
from .book_collection import BookCollection

class BookCollectionBuilder:
    def __init__(self):
        self.theme = None
        self.books = []

    def set_theme(self, theme):
        self.theme = theme
        return self

    def add_book(self, book):
        self.books.append(book)
        return self

    def build(self):
        if not self.theme:
            raise ValueError("Тема не задана")
        return BookCollection(self.theme, self.books)