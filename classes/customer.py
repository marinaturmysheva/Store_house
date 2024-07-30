class Customer:
    """
    Класс Customer

    Этот класс представляет клиента в интернет-магазине.

    Метод init:
        Конструктор инициализирует объект Customer с атрибутами name (имя клиента) и orders (список заказов клиента).
        Пример: customer1 = Customer("Alice", []) создаст клиента с именем "Alice" и пустым списком заказов.

    Метод str:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(customer1) выведет Customer(name=Alice, orders=[]).
    """

   

    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    @property
    def total_orders(self):
        return len(self.orders)

    @property
    def total_order_amount(self):
        return round(sum(order.amount for order in self.orders), 2)

    def __str__(self):
        return f"Customer(name={self.name}, orders={self.orders})"

    def __repr__(self):
        return f"Customer({self.name})"

