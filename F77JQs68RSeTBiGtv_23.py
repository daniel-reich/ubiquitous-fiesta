
def diamond_sum(n):
    if n == 1: return (1)
    i = 2
    dSum = (n+1)/2
    while i < n:
        dSum += 2*(i*n - (n//2))
        i += 1
    dSum = dSum + i*n - n//2
    return int(dSum)

