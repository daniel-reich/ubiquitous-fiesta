
def post_fix(expr):
    expr = expr.split(' ')
    num = []
    for i in expr:
        if i.isdigit():
            num.append(i)
        else:
            num = [int(eval(str(num[0]) + i + num[1]))] + num[2:]        
    return num[0]

