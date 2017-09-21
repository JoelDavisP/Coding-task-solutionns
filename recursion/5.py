
def null(xs):
    return len(xs) == 0

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]


def cons(x, xs):
    return [x] + xs

def is_even(x):
    return x%2 == 0

def filter_even(xs):
    if null(xs):
        return []
    else:
        if is_even(head(xs)):
           return cons(head(xs),filter_even(tail(xs)))
        else:
            return filter_even(tail(xs))    
        
print filter_even([1,2,3,4])


