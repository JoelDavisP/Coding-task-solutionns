# A complex number class

class MyComplex(object):
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    def __str__(self):
        return '(%f + i %f)' % (self.re, self.im)
    def __add__(self,other):
        new = MyComplex()
        new.re = self.re + other.re
        new.im = self.im + other.im
        return new

c = MyComplex(1, 2) 
d = MyComplex(3, 4)
print c.re, c.im # prints 4, 6

print c # prints (4 + 6j) # implement the __str__ method

e = c + d # implement the __add__ method

print e 

