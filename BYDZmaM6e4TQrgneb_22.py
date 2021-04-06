
def fib_fast(num):
    n1, n2 = 0, 1
    while num > 1:
        n1, n2 = n2, n1+n2
        num -= 1
    return n2

