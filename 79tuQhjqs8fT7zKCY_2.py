
def postfix(s):
    stack_res = []
    for i in s.split():
        if i in ["*", "/", "+", "-"]:
            second = stack_res.pop()
            first = stack_res.pop()
        if i == "*":
            stack_res.append(first * second)
        elif i == "/":
            stack_res.append(first / second)
        elif i == "+":
            stack_res.append(first + second)
        elif i == "-":
            stack_res.append(first - second)
        else:
            stack_res.append(int(i))
    return stack_res.pop()

