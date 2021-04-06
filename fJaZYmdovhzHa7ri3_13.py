
def max_collatz(n):
    res = n
    while n != 1:
        n = n*3 + 1 if n%2 else n//2
        if n > res:
            res = n
    return res

