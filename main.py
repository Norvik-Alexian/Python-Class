# 1. Create a class for representing book with some attributes (author, owner, pages, price, current page) and behavior
# (change owner, increase price, change current page), create several books and perform operations on them.

class Book:
    def __init__(self, author: str, owner: str, pages: int, price: int, current_page: int):
        self.author = author
        self.owner = owner
        self.pages = pages
        self.price = price
        self.current_page = current_page

    def change_owner(self, new_owner: str):
        self.owner = new_owner
        print(f'New onwer of the book is {self.owner}')

    def increase_price(self, increased_amount: int):
        self.price += increased_amount
        print(f'New price of the book is {self.price}')

    def change_current_page(self):
        self.current_page += 1
        print(f'Now we are on page {self.current_page}')


book = Book('Norvik', 'Ucraft', 120, 15, 4)
book.change_owner('Ebi')
book.increase_price(10)
book.change_current_page()


# 2. Create a class for representing shop with some attributes (employees names, products names and prices, income, owner)
# and behavior (add employee, remove employee, add products, find product by name, find products cheaper than some
# specific value, change owner, increase income), create several shops and perform operations on them

class Shop:
    def __init__(self, employees_names: list, products_names_princes: dict, income: int, owner: str):
        self.employees_names = employees_names
        self.products_names_princes = products_names_princes
        self.income = income
        self.owner = owner

    def add_employee(self, new_employee: str):
        self.employees_names.append(new_employee)
        print(f'Our new employees list is {self.employees_names}.')

    def remove_employee(self, employee_name: str):
        self.employees_names.remove(employee_name)
        print(f'Our new employees list is {self.employees_names}')

    def add_new_product(self, product_name: str, product_price: int):
        self.products_names_princes[product_name] = product_price
        print(f'Our new product and prices list is {self.products_names_princes}.')

    def find_products(self, product_name: str):
        if product_name in self.products_names_princes.keys():
            print(f'{product_name} exists in warehouse')
        else:
            print(f"Sorry we don't have {product_name} in our warehouse.")

    def cheaper_products(self, product_price: int):
        cheap_products = []
        for price in self.products_names_princes.values():
            if price < product_price:
                cheap_products.append(price)
        print(f'{cheap_products} these are list of our cheap products.')

    def change_owner(self, new_owner: str):
        self.owner = new_owner
        print(f'New onwer of the shop is {self.owner}')

    def increase_income(self, increased_amount: int):
        self.income += increased_amount
        print(f'New income is {self.income}.')


employees_names = ['Norvik', 'Pouria', 'Andranik', 'MohammadAli']
products = {'pen': 5, 'book': 15, 'notebook': 10, 'computer': 150, 'laptop': 160, 'chair': 45}
shop = Shop(employees_names, products, 2500, 'Jery')

shop.add_employee('Robert')
shop.remove_employee('Andranik')
shop.add_new_product('headphone', 70)
shop.find_products('laptop')
shop.cheaper_products(20)
shop.change_owner('Alex')
shop.increase_income(1500)


# 3. Create a class for representing a ticket with some attributes (from location, to location, transport type, duration
# in minutes, arrival time, passenger) and behavior (set from/to, change transport type, increase duration by some number,
# set passenger), create several tickets and perform operations on them.

class Ticket:
    def __init__(self, from_location: str, to_location: str, transport_type: str, duration: int, passengers: int, arrival_time: int):
        self.from_location = from_location
        self.to_location = to_location
        self.transport_type = transport_type
        self.duration = duration
        self.passengers = passengers
        self.arrival_time = arrival_time

    def increase_duration(self, increased_time: int):
        self.duration += increased_time
        print(f'Duration of this trip increased now the duration is {self.duration} hours.')

    def change_transport_type(self, new_transport: str):
        self.transport_type = new_transport
        print(f'New transportation for this trip is {self.transport_type}.')

    def passengers_amount(self, new_passengers_amount):
        self.passengers += new_passengers_amount
        print(f'Total of the passengers in this trip is {self.passengers} people.')


trip = Ticket('Yerevan', 'Canada', 'airplane', 12, 120, 3)
trip.increase_duration(3)
trip.change_transport_type('train')
trip.passengers_amount(50)


# Create a class for representing employee with some attributes (name, position, salary, workdays (weekdays), completed
# tasks names) and behavior (change position, check if salary is higher than some threshold, find how many days salary
# works per week, find if employee works on some specific weekday), create several employees and perform actions,
# check how many employees are defined.

