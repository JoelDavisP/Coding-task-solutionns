class Rectangle(object):
    def __init__(self, l=0, b=0):
        self.l = l
        self.b = b
        
    def __str__(self):
        return 'Rectangle having length = %f, and breadth = %f' % (self.l, self.b)
    def __lt__(self,other):
        a1 = self.l * self.b
        print 'area of first rectangle: %f' % (a1)    
        a2 = other.l * other.b
        print 'area of second rectangle: %f' % (a2)    
        return a1 < a2
a = Rectangle(3, 4)
print a
b = Rectangle(4, 5)
print b

# prints False
print b < a
