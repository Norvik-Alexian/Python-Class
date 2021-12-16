# Create a class for representing book with some attributes (author, owner, pages, price, current page) and behavior
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
