
def postfix(expr):
    chars = expr.split()
    stak = []
    for char in chars:
        if (char == "+" or char == "-" or char == "*" or char == "/"):
            tempB = stak.pop()
            tempA = stak.pop()
            C = eval("{}{}{}".format(tempA,char,tempB))
            stak.append(C)
        else:
            stak.append(char)
    return int(stak[0])

