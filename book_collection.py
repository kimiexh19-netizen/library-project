from .book import Book

class BookCollection(Book):
    def __init__(self, theme, books=None):
        super().__init__(title=theme, author="")
        self.theme = theme
        self.books = books if books else []

    def get_title(self):
        return self.theme

    def get_author(self):
        return "Тематическая подборка"

    def get_info(self):
        info = f'Тема: {self.theme}\nКниги:\n'
        for book in self.books:
            info += f' - {book}\n'
        return info

    def __str__(self):
        return self.get_info()
