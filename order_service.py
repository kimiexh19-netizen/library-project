class OrderService:
    def __init__(self, repository):
        self.repository = repository

    def add(self, order):
        self.repository.add(order)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, order_id):
        return self.repository.get_by_id(order_id)

    def change_status(self, order_id, new_status, FileOrderRepository=None):
        order = self.repository.get_by_id(order_id)
        if order:
            order.status = new_status
            # Для файлового репозитория нужно пересохранить все заказы
            if isinstance(self.repository, FileOrderRepository):
                orders = self.repository.get_all()
                self.repository._save_orders(orders)