class Rectangle:
    def __init__(self, x, y):
        self.width = x
        self.height = y
        
    def area(self):
        return self.width * self.height

    def smaller(self, other):
        return self.area() < other.area()


    def __lt__(self, other):
        return self.area() < other.area()

a = Rectangle(3, 4)

b = Rectangle(4, 5)

print a.smaller(b)

print b < a
