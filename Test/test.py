import random

class Product():
    def __init__(self, price: float):
        self.price = price

    def get_price(self) -> float:
        return self.price
    
    def set_price(self,new_price):
        self.price = new_price

    def is_cheaper(self,other) -> bool:
        return self.price <= other.price
    
    def __str__(self) -> str:
        return f"{self.price}"
    
class CD(Product):
    def __init__(self, title: str, price: int):
        super().__init__(price)
        self.title = title

    def get_title(self) -> int:
        return self.title
    
    def set_price(self, percent: float):
        new = percent*self.price + self.price
        super().set_price(new)

    def __str__(self) -> str:
        return f"{self.title}, {self.price}"

cds = []

for i in range(2):
    title = input('Δωσε τιτλο: ')
    price = float(int(input('Δωσε τιμη: ')))
    cds.append(CD(title, price))

for c in cds:
    c.set_price(random.randint(1, 100)/100)

cheaper = cds[0]
for c in cds:
    if c.is_cheaper(cheaper):
        cheaper = c

print(f"{cheaper.get_price()}")
print(f"{cheaper.get_title()}")

    



