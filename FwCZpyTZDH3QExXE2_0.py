
def amount_fib(n):
    count, a, b = 0, 0, 1
    while a < n:
        a, b = b, a + b
        count += 1
    return count

