def hcf(a,b):
    if b == 0:
        return a
    else:
        return hcf(b, a%b)

print hcf(5,10)

print hcf(5,41)
print hcf(4,120)
print hcf(17,0)
print hcf(19,21)
print hcf(1,10)
