
def not_good_math(n, k):
    i = 0
    while i < k:
        if str(n)[-1] != '0':
            n -= 1
        else:
            n = n // 10
        i += 1
    return n

