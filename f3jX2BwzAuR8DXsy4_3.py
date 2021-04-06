
def fact_of_fact(n):
    res, n1 = 1, n + 1
    for i in range(2, n1):
        res *= pow(i, n1 - i)
    return res

