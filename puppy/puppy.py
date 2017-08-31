class Puppy(object):
    count = 0
    def __init__(self, name = None):
        self.name = name
        Puppy.count += 1
    def __str__(self):
        return 'I am a cute little puppy, my name is %s' %(self.name)
    def howMany(self):
        return Puppy.count
a = Puppy('tommy')
print a # prints 'I am a cute little puppy, my name is tommy'

b = Puppy('bobby')
print b
c = Puppy('frodo')
print c
print a.howMany() # prints 3 (because there are 3 puppies in total)


