import datetime

class Order:
    _id_counter = 1

    def __init__(self, reader_id, books):
        self.order_id = Order._id_counter
        Order._id_counter += 1
        self.reader_id = reader_id
        self.date_issued = datetime.datetime.now()
        self.books = books
        self.status = "Выдан"

    def __str__(self):
        books_str = "\n".join([f" - {book}" for book in self.books])
        return (f"Заказ №{self.order_id}\n"
                f"Читатель: {self.reader_id}\n"
                f"Дата: {self.date_issued}\n"
                f"Книги:\n{books_str}\n"
                f"Статус: {self.status}")