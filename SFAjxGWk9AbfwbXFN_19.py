
def primes_below_num(n):
    c = 2
    l = []
    while c < n+1:
        if sum(1 for x in range(2, c + 1) if c % x == 0) == 1:
            l.append(c)
        c+=1
    return l

