
def not_good_math(n,k):
    while k > 0:
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1
        k = k - 1
    return n

