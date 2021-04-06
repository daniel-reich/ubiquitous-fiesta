
def pi(n):
    multiplier_digits = 1.1
    multiplier_taylor = 1.7
    x = 3 * 10 ** int(n * multiplier_digits + 3)
    res = x
    for k in range(1, int(n * multiplier_taylor + 3)):
        x *= 2 * k - 1
        x //= 2 * k * 4
        res += x // (2 * k + 1)
    return '3.' + str(res)[1: n + 1]

