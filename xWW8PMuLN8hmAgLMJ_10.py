
def postfix(expression):
    expression = expression.replace("/", "//")
    r = ["-", "+", "//", "*"]
    ex = expression.split()
    while any(j in ex for j in r):
        for i in range(len(ex)):
            if ex[i] in r:
                new = eval(" ".join([ex[i - 2], ex[i], ex[i - 1]]))
                ex[i - 2] = str(new)
                ex.pop(i - 1)
                ex.pop(i - 1)
                break
    return int(ex[0])

