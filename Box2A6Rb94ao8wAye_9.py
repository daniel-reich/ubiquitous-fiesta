
def leader(arr):
    res = []
    for i in range(0, len(arr)):
        if i == len(arr)-1 or arr[i] > max(arr[i+1:]):
            res.append(arr[i])
    return res

