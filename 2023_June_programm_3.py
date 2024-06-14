class Vec2D():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def plus(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def times(self, other):
        return Vec2D(self.x*other , self.y*other)

    def isequal(self, other):
        if self.x != other.x and self.y != other.y:
            return False
        else: 
            return True

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f'({self.x},{self.y})'

    



