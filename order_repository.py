import json
import os

class OrderRepository:
    def add(self, order): pass
    def get_all(self): pass
    def get_by_id(self, order_id): pass

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = []

    def add(self, order):
        self.orders.append(order)

    def get_all(self):
        return self.orders

    def get_by_id(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None
class FileOrderRepository(OrderRepository):
    FILENAME = 'orders.json'

    def __init__(self):
        if not os.path.exists(self.FILENAME):
            with open(self.FILENAME, 'w') as f:
                json.dump([], f)

    def _load_orders(self, Order=None):
        with open(self.FILENAME, 'r') as f:
            data = json.load(f)
            orders = []
            for item in data:
                # Для простоты сериализации/десериализации храним только базовые данные
                order = Order(item['reader_id'], item['books'])
                order.order_id = item['order_id']
                order.status = item['status']
                orders.append(order)
            return orders

    def _save_orders(self, orders):
        data = []
        for order in orders:
            data.append({
                'order_id': order.order_id,
                'reader_id': order.reader_id,
                'books': [str(book) for book in order.books],
                'status': order.status,
            })
        with open(self.FILENAME, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add(self, order):
        orders = self._load_orders()
        orders.append(order)
        self._save_orders(orders)

    def get_all(self):
        return self._load_orders()

    def get_by_id(self, order_id):
        for order in self.get_all():
            if order.order_id == order_id:
                return order
        return None
