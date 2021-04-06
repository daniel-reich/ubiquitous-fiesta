
def golomb(n):
    a = [1] * (n + 1)
    for i in range(1, n):
        a[i + 1] = 1 + a[i + 1 - a[a[i]]]
    return a[1:]

