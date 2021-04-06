
def kadane(A):
    maxSoFar = 0
    maxEndingHere = 0
    start = end = 0
    beg = 0
    for i in range(len(A)):
        maxEndingHere = maxEndingHere + A[i]
        if maxEndingHere < 0:
            maxEndingHere = 0
            beg = i + 1
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
            start = beg
            end = i
    return [maxSoFar, start, end]
​
def big_sub(lst):
    ans = kadane(lst)
    if ans[0] == max(lst):
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == ans[0]:
                return [ans[0], i, i]
    return kadane(lst)

