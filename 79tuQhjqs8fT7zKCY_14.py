
def postfix(expr):
    lst = []
    expr = expr.split(' ')
    for i in expr:
        if i.isdigit(): lst.append(i)
        else:
            a,b = lst.pop(),lst.pop()
            lst.append(str(eval(b+i+a)))
    return int(float(lst[0]))

