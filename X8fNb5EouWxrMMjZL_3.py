
def collatz(n, cnt = 0):
    if n == 1: return cnt
    elif n%2: return collatz(n*3+1, cnt+1)
    else: return collatz(n/2, cnt+1)

