
def josephus(n, k):
    p = k
    reihe = list(range(n))
    gefunden  = []
    while len(gefunden)<n:
        i = p%len(reihe)
        if i == 0:
            i = len(reihe)
        i -= 1
        gefunden.append(reihe.pop(i))
        reihe = reihe[i::]+reihe[0:i]
    return gefunden[-1] + 1

