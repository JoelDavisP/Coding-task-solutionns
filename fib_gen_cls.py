class fibiterator:
    def __init__(self,n):
        self.n = n
        self.a = 0
        self.b = 1
    def next(self):
        if self.n == 0:
            raise StopIteration()
        else:
            self.n -= 1
            a = self.a
            b = self.b
            self.a, self.b = a+b, a
            return self.b
class fibn:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return fibiterator(self.n)

k = fibn(10)
for i in k:
    print i
