
def bonacci(n, k):
    arr = [0]*(n-1) + [1]
    for _ in range(k):
        arr.append(sum(arr[-n:]))
    return arr[k-1]

