def fib(n):
    a = 0
    b = 1
    while a < n:
        yield a
        a,b = a+b,a

