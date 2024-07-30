# Пример использования статических методов и методов класса в интернет-магазине
# Предположим, у нас есть интернет-магазин с классом Product, который представляет товар, и классом Order, который представляет заказ. 
# Мы будем использовать статические методы для расчета скидок и методы класса для подсчета общего количества заказов.
from classes.order import Order
from classes.product import Product
from classes.customer import Customer
from classes.discount import Discount  # импортируем класс Discount


# Создаем продукты
product1 = Product("Laptop", 100000)
product2 = Product("Smartphone", 50000)
product3 = Product("Tablet", 30000)
product4 = Product("Headphones", 10000)
product5 = Product("Smartwatch", 20000)

# Рассчитываем цены с учетом скидок на сайте
discount_percent = 5
discounted_price1 = Discount.apply_discount(product1.price, discount_percent)
discounted_price2 = Discount.apply_discount(product2.price, discount_percent)
discounted_price3 = Discount.apply_discount(product3.price, discount_percent)
discounted_price4 = Discount.apply_discount(product4.price, discount_percent)
discounted_price5 = Discount.apply_discount(product5.price, discount_percent)

# Выводим сниженные цены на товары на сайте
print(f"Сниженная цена на {product1.name}: {discounted_price1}")  # Вывод: Сниженная цена на Laptop: 95000.0
print(f"Сниженная цена на {product2.name}: {discounted_price2}")  # Вывод: Сниженная цена на Smartphone: 47500.0
print(f"Сниженная цена на {product3.name}: {discounted_price3}")  # Вывод: Сниженная цена на Tablet: 28500.0
print(f"Сниженная цена на {product4.name}: {discounted_price4}")  # Вывод: Сниженная цена на Headphones: 9500.0
print(f"Сниженная цена на {product5.name}: {discounted_price5}")  # Вывод: Сниженная цена на Smartwatch: 19000.0


# Создаем клиентов
customer1 = Customer("Tatiana")
customer2 = Customer("Michael")
customer3 = Customer("Olga")
customer4 = Customer("Svetlana")
customer5 = Customer("Alexander")

# Создаем скидки
discount_5 = Discount("Скидка на сайте 5%", 5)
discount_10 = Discount("Скидка по карте", 10)
discount_seasonal = Discount("Сезонная скидка", 15)
discount_promo = Discount("Промокод", 20)

# Создаем заказы с применением скидок
order1 = Order([product1], discount=discount_10)  #10% скидка по карте
order2 = Order([product2, product1], discount=discount_seasonal) #15% сезонная скидка
order3 = Order([product3, product4, product5], discount=discount_promo) #20% скидка по промокоду
order4 = Order([product1, product2, product3])
order5 = Order([product4, product5])
order6 = Order([product3], discount=discount_seasonal)  #15% сезонная скидка
order7 = Order([product2, product5], discount=discount_10) #10% скидка по карте
order8 = Order([product1], discount=discount_promo) #20% скидка по промокоду
order9 = Order([product4, product3])
order10 = Order([product2], discount=discount_promo) #20% скидка по промокоду
order11 = Order([product1, product2], discount=discount_5)  # 5% скидка с сайта
order12 = Order([product3, product5], discount=discount_5)  # 5% скидка с сайта

# Добавляем заказы клиентам
customer1.add_order(order1)
customer1.add_order(order2)
customer2.add_order(order3)
customer2.add_order(order4)
customer3.add_order(order5)
customer3.add_order(order6)
customer4.add_order(order7)
customer4.add_order(order8)
customer5.add_order(order9)
customer5.add_order(order10)
customer1.add_order(order11)
customer2.add_order(order12)

# Выводим общую информацию по каждому клиенту
for customer in [customer1, customer2, customer3, customer4, customer5]:
    print(f"Общее количество заказов для {customer.name}: {customer.total_orders}")
    print(f"Общая сумма заказов для {customer.name}: {customer.total_order_amount}")

# Подсчитываем общее количество заказов и общую сумму всех заказов для всех клиентов
total_orders = Order.total_orders()
total_amount = Order.total_amount()
print(f"\nИтого общее количество заказов для всех клиентов: {total_orders}")
print(f"Итого общая сумма всех заказов для всех клиентов: {total_amount}")

# Отчеты
orders = [order1, order2, order3, order4, order5, order6, order7, order8, order9, order10, order11, order12]
customers = [customer1, customer2, customer3, customer4, customer5]

def sales_report(orders):
    sales_data = {}
    for order in orders:
        for product in order.products:
            if product.name in sales_data:
                sales_data[product.name]['quantity'] += 1
                sales_data[product.name]['total'] += product.price
            else:
                sales_data[product.name] = {'quantity': 1, 'total': product.price}
    report = "\nОтчет по продажам товаров:\n"
    for product_name, data in sales_data.items():
        report += f"{product_name}: продано {data['quantity']} шт. на общую сумму {data['total']}\n"
    return report

def customer_report(customers):
    report = "\nОтчет по клиентам:\n"
    for customer in customers:
        report += f"{customer.name}: сделал {customer.total_orders} заказов на сумму {customer.total_order_amount}\n"
    return report

def discount_sales_report(orders):
    discount_sales_data = {}
    for order in orders:
        if order.discount:
            for product in order.products:
                if product.name in discount_sales_data:
                    discount_sales_data[product.name]['quantity'] += 1
                    discount_sales_data[product.name]['total'] += product.price
                else:
                    discount_sales_data[product.name] = {'quantity': 1, 'total': product.price}
    report = "\nОтчет по продажам товаров с учетом скидок:\n"
    for product_name, data in discount_sales_data.items():
        report += f"{product_name}: продано {data['quantity']} шт. на общую сумму {data['total']}\n"
    return report

print(sales_report(orders))
print(customer_report(customers))
print(discount_sales_report(orders))

# Вывод информации о клиентах, заказах и продуктах с использованием дандер методов
for customer in customers:
    print(customer)

for order in orders:
    print(order)

for product in [product1, product2, product3, product4, product5]:
    print(product)
