
def number_length(num):
    res, n = 1, num // 10
    while n:
        n //= 10
        res += 1
    return res

