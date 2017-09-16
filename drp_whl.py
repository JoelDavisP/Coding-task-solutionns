def drp_whl(a = [1,2,5,6,9,12,14,15,18,11,9,8,19,25,29]):
    i = 0
    b = lambda x: x< 14
    while b(a[i]) == True:
        i += 1
    while True:
        yield a[i]
        i += 1
