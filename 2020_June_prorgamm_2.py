import math
import random

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


class Circle():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def contains(self, point):
        if Point(*self.center).dist(Point(*point)) <= self.radius:
            return True
        else:
            return False

    def intersects(self, circle_other):
        if abs(self.radius - circle_other.radius) <= Point(*self.center).dist(Point(*circle_other.center)) <= abs(self.radius + circle_other.radius):
            return True
        else:
            return False

    def __str__(self) -> str:
        pass

c1 = Circle((1,2) , 2)
c2 = Circle((1,2) , 2)
point = (1.4 , 2.4)
print(c1.contains(point))