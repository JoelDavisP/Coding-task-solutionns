class repeat_iterator:
    def __init__(self,n,c):
        self.n = n
        self.c = c
    def next(self):
        if self.c == 0:
            raise StopIteration()
        else:
            self.c -= 1
            return self.n
class rept:
    def __init__(self,n,c):
        self.n = n
        self.c = c
    def __iter__(self):
        return repeat_iterator(self.n,self.c)

k = rept(1000,20)
for i in k:
    print i
