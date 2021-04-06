
def complete_square(arr):
    if len(arr) == len(arr[0]):
        return arr
    elif len(arr) < len(arr[0]): #less rows
        d = len(arr[0])-len(arr)
        arr = arr + [[0 for _ in range(len(arr[0]))] for _ in range(d)]
        return arr
    else: #less cols
        d = len(arr) - len(arr[0])
        return [[arr[i][j] if j < len(arr[0]) else 0 for j in range(len(arr))] for i in range(len(arr))]

