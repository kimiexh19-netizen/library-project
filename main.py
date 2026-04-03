from book_factory import BookFactory
from book_collection_builder import BookCollectionBuilder
from order import Order
from order_repository import InMemoryOrderRepository, FileOrderRepository
from order_service import OrderService


def main():
    print("Выберите тип репозитория:")
    print("1 — In-memory")
    print("2 — Файловый (JSON)")
    choice = input("Ваш выбор: ")

    if choice == '1':
        repo = InMemoryOrderRepository()
        print("Используется in-memory репозиторий.")
    elif choice == '2':
        repo = FileOrderRepository()
        print("Используется файловый репозиторий.")
    else:
        print("Неверный выбор.")
        return

    service = OrderService(repo)

    # Фабрика книг
    factory = BookFactory()

    book1 = factory.create_book('fiction', '1984', 'Джордж Оруэлл')
    book2 = factory.create_book('science', 'Краткая история времени', 'Стивен Хокинг')

    # Строитель подборки
    builder = BookCollectionBuilder()
    collection = builder.set_theme('Фантастика').add_book(book1).build()

    # Оформление заказа (смешиваем книги и подборки)
    reader_id = input("Введите номер читателя: ")
    order_books = [book2, collection]

    order = Order(reader_id, order_books)

    # Сохранение заказа через сервис (репозиторий подменяется без изменений логики)
    service.add(order)

    print("\nИстория заказов:")
    for o in service.get_all():
        print(o)
        print("-" * 20)

    # Получение заказа по ID и изменение статуса (демонстрация работы сервиса)
    try:
        oid = int(input("\\nВведите ID заказа для изменения статуса: "))
        found_order = service.get_by_id(oid)
        if found_order:
            # Этот print должен быть внутри блока if
            print(found_order)
            new_status = input("Введите новый статус: ")
            service.change_status(oid, new_status)
            print("Статус изменён!")
        else:
            print("Заказ не найден.")
    except ValueError:
        print("Некорректный ID.")

    if __name__ == "__main__":
        main()