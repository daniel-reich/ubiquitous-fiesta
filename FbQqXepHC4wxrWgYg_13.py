
def prime_divisors(x):
    factors1 = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors1.append(i)
        else:
            i += 1
    factors2 = [i for i in factors1 if all(i % x for x in range(2, i))]
    res = []
    for i in factors2:
        if i not in res:
            res.append(i)
    return res

