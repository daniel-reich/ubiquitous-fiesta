
def checkBalance(exp):
    stack = []
    for i, c in enumerate(exp):
        if c == '(':
            stack.append(c)
        elif c == '{':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return i
        elif c == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return i
    return len(exp) if stack else -1

