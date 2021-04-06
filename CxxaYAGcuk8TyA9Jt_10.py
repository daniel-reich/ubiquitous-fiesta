
def check_balance(expr):
    d = {']': '[', ')': '(', '}': '{'}
    stack = []
​
    for idx, i in enumerate(expr):
        if i in {'[', '(', '{'}:
            stack.append(i)
        elif i in d:
            if not stack or stack[-1] != d[i]:
                return idx
            stack.pop()
    return idx + 1 if stack else -1

