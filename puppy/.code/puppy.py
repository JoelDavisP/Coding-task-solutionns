class Puppy:
    npuppies = 0
    def __init__(self, name):
        self.name = name
        Puppy.npuppies += 1

    def __str__(self):
        return 'I am a cute little puppy, my name is %s' % self.name

    def howMany(self):
        return Puppy.npuppies

a = Puppy('tommy')
print a # prints 'I am a cute little puppy, my name is tommy'

b = Puppy('bobby')

c = Puppy('frodo')

print a.howMany() # prints 3 (because there are 3 puppies in total)


