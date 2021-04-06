
def arithmetic_operation(equation):
    '''
    Returns the result of evaluating the string equation
    '''
    from operator import add, sub, floordiv, mul
​
    OPS = {'+':add, '-':sub, '*':mul, '//':floordiv}
    a,op,b = equation.split()
    
    try:
        return OPS[op](int(a),int(b)) 
    except ZeroDivisionError:
        return -1

