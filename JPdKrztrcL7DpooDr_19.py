
def collatz(n):
    res = [0, n]
    while n != 1:
        res[0] += 1
        n = n*3 + 1 if n%2 else n//2
        if n > res[1]:
            res[1] = n
    return res

