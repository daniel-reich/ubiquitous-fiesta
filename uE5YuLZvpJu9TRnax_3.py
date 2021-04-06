
def prefix(expr):
    '''
    Returns the result of evaluating expr, a valid arithmetic expression
    using prefix notation for operators.
    '''
    stack = []
    operators = ['/','*','+','-']
​
    for token in expr.split()[::-1]:
        if token not in operators:
            stack.append(int(token))
        else:
            if token == '/':
                token = '//'
            stack.append(eval('{} {} {}'.format(stack.pop(),token,stack.pop())))
​
    return stack[0]

