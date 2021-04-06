
def golomb(n):
    res = [0, 1, 2, 2]
    i = 3
    while len(res) <= n:
        res.extend([i] * res[i])
        i += 1
    return res[1:n+1]

