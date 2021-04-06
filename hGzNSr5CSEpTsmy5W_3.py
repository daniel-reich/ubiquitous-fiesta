
def not_good_math(n, k):
    i = 0
    while i < k:
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1
        i=i+1
    return n

