
def make_dartboard(n):
    i = n % 2
    d = n // 2 + 1
    res = [str(d)] if i else []
    while True:
        i += 2
        d -= 1
        if i > n: return list(map(int, res))
        sd = str(d)
        res = [sd*i] + [sd + row + sd for row in res] + [sd*i]

