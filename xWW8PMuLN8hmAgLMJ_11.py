
def postfix(expression):
    stack = []
    for x in expression.split():
        if x.isdigit():
            stack.append(int(x))
        else:
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(eval('{}{}{}'.format(n2,x,n1)))
    return int(stack[0])

