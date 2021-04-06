
from itertools import combinations
def zero_indices(lst, k):
​
    def max_ones(arr):
        z, curr = 0, 0
        for i in range(len(arr)):
            if arr[i] == 1:
                curr += 1
                if curr > z:
                    z = curr
            else:
                curr = 0
        return z
​
    longest = (0, [])
    for cmb in combinations([i for i, d in enumerate(lst) if d == 0], k):
        mxz = max_ones([1 if i in cmb else lst[i] for i in range(len(lst))])
        if mxz > longest[0]:
            longest = (mxz, list(cmb))
    return longest[1]

