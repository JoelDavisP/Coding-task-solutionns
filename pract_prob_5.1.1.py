class reverse_iter(object):
    def __init__(self, n):
        l = len(n)-1
        self.n = n
        self.start = l
        self.end = -1
    def __iter__(self):
        return self
    def next(self):
        if  self.start > self.end:
            i = self.n[self.start]
            self.start -= 1
            return i
        else:
            raise StopIteration()

y = reverse_iter([10,9,8,7,6,5,4,3,2,1,5,63,46,2,5])
z = reverse_iter(list(xrange(10)))
#while True:
 #   print y.next()
while True:
    print z.next()

