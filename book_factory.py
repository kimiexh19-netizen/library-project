from .book import FictionBook, ScienceBook, ArtBook

class BookFactory:
    @staticmethod
    def create_book(book_type, title, author):
        if book_type == 'fiction':
            return FictionBook(title, author)
        elif book_type == 'science':
            return ScienceBook(title, author)
        elif book_type == 'art':
            return ArtBook(title, author)
        else:
            raise ValueError("Неизвестный тип книги")