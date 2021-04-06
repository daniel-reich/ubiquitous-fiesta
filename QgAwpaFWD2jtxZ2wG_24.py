
def sum_digits(n):
    d = 1
    while True:
        n = n // 10
        if n == 0:
            return d
        d += 1

