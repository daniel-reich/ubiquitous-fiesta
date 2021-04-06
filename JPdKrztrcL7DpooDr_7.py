
def collatz(n):
    cnt, hi = 0, n
    while n != 1:
        if n%2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
            if n > hi:
                hi = n
        cnt += 1
    return [cnt, hi]

