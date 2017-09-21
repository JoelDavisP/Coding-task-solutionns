
def null(xs):
    return len(xs) == 0

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]


def is_even(x):
    return (x%2) == 0

def sum_even(xs):
    if null(xs):
        return 0
    else:
        if is_even(head(xs)):
            return head(xs) + sum_even(tail(xs))
        else:
            return sum_even(tail(xs))

print sum_even([1,2,5,4,6,3,9,8,10,3,8,3,8,54])

