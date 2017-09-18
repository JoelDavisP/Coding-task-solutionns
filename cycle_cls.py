class cycle_iterator:
    def __init__(self,s,cnt):
        self.s = s
        self.cnt = cnt
        self.i = -1
    def next(self):
        if self.cnt == 0:
            raise StopIteration()
        else:
            self.cnt -= 1
            self.i += 1
            return self.s[self.i % len(self.s)]
class cycle:
    def __init__(self,s,cnt):
        self.s = s
        self.cnt = cnt
    def __iter__(self):
        return cycle_iterator(self.s,self.cnt)

k = cycle(s= "ABC", cnt = 15)
for i in k:
    print i
