
def generate_rug(n):
    mid = n//2
    base = [mid] * n
    a = [base[:]]
    
    y = 1
    for x in range(mid-1, -1, -1):
        base[y:-y] = [x] * len(base[y:-y])
        a.append(base[:])
        y += 1
    return a + a[::-1][1:]

