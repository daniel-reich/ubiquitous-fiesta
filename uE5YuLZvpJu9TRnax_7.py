
def calculator(a, operator, b):
    return {"+": a + b, "-": a - b, "*": a * b, "/": a // b}[operator]
​
​
def prefix(exp):
    expression = exp.split()[::-1]
    stack = []
    for e in expression:
        if "-" in e:
            if e[1:].isdigit():
                stack.append(int(e))
            else:
                stack.append(calculator(stack.pop(), e, stack.pop()))
        elif e.isdigit():
            stack.append(int(e))
        else:
            stack.append(calculator(stack.pop(), e, stack.pop()))
    return stack[0]

