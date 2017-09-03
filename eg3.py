class RationalNumber(object):
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
        >>> a - b
        1/6
        >>> a * b
        1/6
        >>> a/b
        3/2
    """
    def __init__(self,num=1, den=1):
        self.num = num
        self.den = den
        assert self.den != 0
    def __add__(self,other):
        if not isinstance(other,RationalNumber):
            other = RationalNumber(other)
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return RationalNumber(num,den)
    def __mul__(self,other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)
        num = self.num * other.num
        den = self.den * other.den
        return RationalNumber(num,den)

    def __sub__(self,other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return RationalNumber(num,den)

    def __div__(self,other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)
        num = self.num * other.den
        den = self.den * other.num
        return RationalNumber(num,den)

    def __str__(self):
        if self.num == self.den:
            return "1"
        
        elif self.num == 0 or self.den == 1:
            return "%s" %(self.num)
        else:
            return "%s/%s" % (self.num,self.den)
a = RationalNumber(1,2)
b = RationalNumber(2,4)
c = RationalNumber(20,15)
print c
print a + b
print a - b
print a * b
print a / b
   
