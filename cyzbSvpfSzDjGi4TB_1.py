
def harmonic(n):
    sum = 0
    for i in range(1,n+1):
        sum += 1 / i
    return round(sum, 3)

