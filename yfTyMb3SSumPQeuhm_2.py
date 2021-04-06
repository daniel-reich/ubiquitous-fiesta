
def fibonacci(n):
    return powerMN(n)[1]
​
def powerMN(n):
    if n == 1: return (1, 1)
    M, N = powerMN(n//2)
    M, N = (M**2 + 5*N**2) >> 1, M*N
    if n & 1:
        return ((M + 5*N)>>1, (M + N) >>1)
    else:
        return (M, N)

