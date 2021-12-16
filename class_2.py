# Create a class for representing shop with some attributes (employees names, products names and prices, income, owner)
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
