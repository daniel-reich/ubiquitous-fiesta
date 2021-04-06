
brackets = {')': '(', '}': '{'}
​
def checkBalance(expression):
    stack = []
    for i in range(len(expression)):
        c = expression[i]
        if c in brackets:
            if len(stack) == 0 or stack[-1] != brackets[c]:
                return i
            stack.pop()
        elif c in brackets.values():
            stack.append(c)
    return -1 if len(stack) == 0 else len(expression)

