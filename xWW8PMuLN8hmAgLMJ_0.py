
def postfix(expression):
    arr = expression.split()
    
    stack = []
    while arr:
        token = arr.pop(0)
        if token.isnumeric():
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(eval('{}{}{}'.format(b, token, a)))
    return int(*stack)

