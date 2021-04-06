
def smallest(n):
    l = [i for i in range(2, n+1)]
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                l[j] = int(l[j] / l[i])
    p = 1
    for i in l:
        p *= i
    return p

