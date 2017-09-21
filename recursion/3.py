
def null(xs):
    return len(xs) == 0

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]


def sum_list(xs):
    if null(xs):
        return 0
    return head(xs) + sum_list(tail(xs))

print sum_list([1,2,3,6,5,4,8,9,6,3,7])
