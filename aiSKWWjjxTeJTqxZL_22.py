
def complete_square(arr):
    x = len(arr[0])
    y = len(arr)
    if x == y:
        return arr
    elif x < y:
        for i in arr:
            for j in range(y-x):
                i.append(0)
        return arr
    else: 
        t = []
        for m in range(x):
            t.append(0)
        for k in range(x-y):
            arr.append(t)
        return arr

