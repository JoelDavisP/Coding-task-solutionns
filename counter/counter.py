
class Counter(object):
    def __init__(self,val=0):
        self.value = val
    def __str__(self):
        return 'Counter: %d .' % (self.value)
    def show(self):
        print self.value
    def increment(self):
        self.value += 1
    def decrement(self):
        self.value -= 1
c = Counter()
c.show() # prints 0.
c.increment()
c.show() # prints 1
c.decrement() 
c.show() # prints 0
print c # prints 'Counter: 0' (implement the __str__ method)
c = Counter(10) # __init__ should accept an argument
c.show() # prints 10


