#handling tree-like structures

my_expression = ['+', ['+', 3, 4], ['+',10,8]]

def eval(expr):
    if isinstance(expr, int):
        return expr
    else:
        if expr[0] == '+':
            return eval(expr[1]) +eval(expr[2])


    
print eval(my_expression)
