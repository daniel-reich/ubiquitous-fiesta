
def postfix(expression):
    '''
    Returns the evaluation of postfix notation expression as described above.
    '''
    from operator import add, mul, sub, truediv # supported operators
​
    OPERATORS = {
                 '+' : add,
                 '-' : sub,
                 '*' : mul,
                 '/' : truediv
                } # string operators mapping to actual operators
​
    stack = []  # to hold operands
    expression = expression.split()  # separate into symbols
​
    for symbol in expression:
        if symbol not in OPERATORS:
            stack.append(int(symbol))
​
        else:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[symbol](op1, op2)) # evaluate and store result
                         
    return stack.pop()  # final result

