
def postfix(expr):
    stack = []
    for a in expr.split():
        if a.isdigit():
            stack.append(int(a))
        else:
            x, y = stack.pop(), stack.pop()
            if a == '+':
                stack.append(y + x)
            elif a == '-':
                stack.append(y - x)
            elif a == '*':
                stack.append(y * x)
            elif a == '/':
                stack.append(y / x)
    return stack[0]

