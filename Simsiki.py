import random


class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cart = []

    def add_to_cart(self, product, price):
        if self.balance >= price:
            self.cart.append(product)
            self.balance -= price
            print(f"{self.name} додав {product} до кошика.")
        else:
            print(f"{self.name} не може купити {product} - недостатньо коштів.")

    def view_cart(self):
        print(f"{self.name}'s кошик: {', '.join(self.cart)}")

    def checkout(self):
        print(f"{self.name} оплачує покупки та завершує замовлення.")
        self.cart.clear()


class Store:
    def __init__(self):
        self.products = {
            "Цукерки": 10,
            "Чай": 8,
            "Протеїн": 15,
            "Овочі": 12
        }

    def show_products(self):
        print("Товари в магазині:")
        for product, price in self.products.items():
            print(f"{product}: {price} грн")

    def buy(self, customer, product_name):
        if product_name in self.products:
            price = self.products[product_name]
            customer.add_to_cart(product_name, price)
        else:
            print(f"{product_name} забрали.")

store = Store()

customer1 = Customer("Іринка", 50)
customer2 = Customer("Богдаша", 20)

store.show_products()

store.buy(customer1, "Цукерки")
store.buy(customer1, "Чай")
store.buy(customer2, "Протеїн")
store.buy(customer2, "Овочі")

customer1.view_cart()
customer2.view_cart()
customer1.checkout()
customer2.checkout()
