
def sums_of_powers_of_two(n):
    res, i = [], 0
    while n:
        if n & 1:
            res.append(pow(2, i))
        i += 1
        n >>= 1
    return res

