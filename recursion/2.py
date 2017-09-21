
def null(xs):
    return len(xs) == 0

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]


def my_len(xs):
    if null(xs):
        return 0
    return 1+ my_len(tail(xs))


print my_len([1,2,3,6,5,8,9,6,4,5,6,3])
