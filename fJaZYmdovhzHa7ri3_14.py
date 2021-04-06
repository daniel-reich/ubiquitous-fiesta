
def max_collatz(n):
    if (n == 1):return max([0, 1])
    res = []
    while (n != 1):
        if (n % 2 == 0) :
            res.append(n)
            n=n / 2
        else:
            res.append(n)
            n=n * 3+1
    return max(res)

