
def partitions(n):
    arr = [0] * (n+1)
    arr[0] = 1
    for p in range(1, n+1):
        for idx, i in enumerate(range(p, n+1)):
            arr[i] += arr[idx]
    return arr[n]

