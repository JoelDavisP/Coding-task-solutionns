class MyComplex:
    def __init__(self, x, y):
        self.re = x
        self.im = y
    
    def __str__(self):
        return '(%d + %di)' % (self.re, self.im)

    def __add__(self, other):
        return MyComplex(self.re + other.re, self.im + other.im)

a = MyComplex(1, 2)
b = MyComplex(3, 4)

print a + b

