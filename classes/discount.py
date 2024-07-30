class Discount:
    """
    Класс Discount

    Этот класс представляет скидку в интернет-магазине.

    Метод init:
        Конструктор инициализирует объект Discount с атрибутами description (описание скидки) и discount_percent (процент скидки).
        Пример: discount1 = Discount("10% off", 10) создаст скидку с описанием "10% off" и скидкой в 10 процентов.

    Метод str:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(discount1) выведет Discount(description=10% off, discount_percent=10).
    """


    def __init__(self, description: str, discount_percent: int):
        self.description = description
        self.discount_percent = discount_percent

    def __str__(self):
        return f"Discount(description={self.description}, discount_percent={self.discount_percent})"

    @staticmethod
    def apply_discount(price: float, discount_percent: int) -> float:
        return round(price * (1 - discount_percent / 100), 2)
