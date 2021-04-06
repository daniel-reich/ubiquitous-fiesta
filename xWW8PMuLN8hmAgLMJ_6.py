
def postfix(expression):
    l = expression.split()
    oper = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            }
    stack = []
    while l:
        el = l.pop(0)
        if el not in oper:
            stack.insert(0, float(el))
        else:
            n2 = stack.pop(0)
            n1 = stack.pop(0)
            stack.insert(0, oper[el](n1, n2))
    return stack.pop()

