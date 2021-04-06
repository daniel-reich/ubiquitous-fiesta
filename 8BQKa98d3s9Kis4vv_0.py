
import numpy as np
​
def final(r, c, i):
    arr = np.zeros((r, c))
    for idx, d in i:
        if d == 'r':
            arr[int(idx)] += 1
        else:
            arr[:,int(idx)] += 1
    return arr.tolist()

