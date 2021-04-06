
def summation(exp, n):
    res =[]
    for n in range(1,n+1):
        res.append(round(eval(exp),2))
    return round(sum(res),1)

