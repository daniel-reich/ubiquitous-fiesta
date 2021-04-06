
def get_lucky_number(size, n):
    arr = list(range(1, size+1))[::2]
    f = 1
    while arr[f] < len(arr):
        arr = [i for idx, i in enumerate(arr, 1) if idx%arr[f] != 0]
        f += 1
    return arr[n-1]

