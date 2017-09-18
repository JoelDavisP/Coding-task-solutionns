class chain_iterator:
    def __init__(self,s1,s2):
        self.i = -1
        self.j = -1
        self.s1 = s1
        self.s2 = s2
        self.k = len(self.s1) + len(self.s2)
    def next(self):
        if self.k == 0:
            raise StopIteration()
        else:
            if self.i >= len(self.s1) - 1 :
                self.k -= 1
                self.j += 1
                return self.s2[self.j]
            else:
                self.k -= 1
                self.i += 1
                return self.s1[self.i]
                    
class chain:
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
    def __iter__(self):
        return chain_iterator(self.s1,self.s2)

k = chain(s1 = "GOOD", s2 = "MORNING")
for i in k:
    print i
