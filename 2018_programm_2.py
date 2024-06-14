import math 
import random

class Product():
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def is_more_expensive(self, other) -> bool:
        if self.price < other.price:
            return True
        else:
            return False
        
class Book(Product):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_title(self):
        return self.title
    
    def set_price(self, percentage):
        self.price += self.price*(percentage/100)





