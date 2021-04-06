
def partitions(n):
    arr = [1] + [0]*n
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            arr[i] += arr[i-k]
    return arr[n]

