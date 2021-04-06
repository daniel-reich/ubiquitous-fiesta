
def golomb(n):
    res, idx = [1, 2, 2], 2
    while len(res) < n:
        res += res[idx] * [idx + 1]
        idx += 1
    return res[:n]

