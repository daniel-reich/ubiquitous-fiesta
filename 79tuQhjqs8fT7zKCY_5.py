
def postfix(expr):
    exp = expr.split(" ")
    S = []
    for i in exp:
        if i.isnumeric():
            S = S + [i]
        else: 
            S = S[:-2] + [str(eval(S[-2] + i + S[-1]))]
    return int(float(S[0]))

