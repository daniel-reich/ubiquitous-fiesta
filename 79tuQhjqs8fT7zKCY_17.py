
def postfix(expression):
    tokens = expression.split()
    stack = []
    ops = ['+', '-', '*', '/']
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            if token == '*':
               stack.append(a * b)
            if token == '/':
                if a * b < 0:
                    stack.append(-(abs(a) // abs(b)))
                else:
                    stack.append((abs(a) // abs(b)))
        else:
            stack.append(int(token))
    assert len(stack) == 1
    return stack[0]

