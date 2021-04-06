
def amount_fib(n):
    a, b, total = 0, 1, 0
    while a < n:
        a, b = b, a + b
        total += 1
    return total

