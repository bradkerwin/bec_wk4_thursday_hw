class Product():
    def __init__(self, product_ID, name, price, display_product_information):
        self.product_ID = product_ID
        self.name = name
        self.price = price
        self.display_product_information = display_product_information

class Book(Product):
    def __init__(self, product_ID, name, price, display_product_information, author):
        super().__init__(product_ID, name, price, display_product_information)
        self.author = author

    def display_book_info(self):
        print(f"Title: {self.name}, Product_ID: {self.product_ID}, Written by: {self.author}, Current Price: ${self.price}, Synopsis: {self.display_product_information} ")

book1 = Book(123456, "The Outsiders", 8.00, "This is a book about a group of greasers exploring adolescence and dealing with conflict from a rival gang.", "S.E. Hinton")
book2 = Book(987654, "The Great Gatsby", 11.00, "This is a novel about a man's interactions with his millionaire neighbor who is looking to reunite with his former love interest.", "F. Scott Fitzgerald")

book1.display_book_info()
book2.display_book_info()