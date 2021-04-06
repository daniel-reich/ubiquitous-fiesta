
def golomb(n):
    start, i = [1, 2, 2], 1
    while len(start) < n:
        i += 1
        start = start + start[i] * [i + 1]
    return start[:n]

