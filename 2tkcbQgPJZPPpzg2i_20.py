
def sum_of_holes(N):
    d = {8: 2, 9: 1, 6: 1, 4: 1, 0: 1, 2: 0, 3: 0, 5: 0, 7: 0, 1: 0}
    res = 0
    for x in range(1, N+1):
        for y in str(x):
            if int(y) in d:
                res += d[int(y)]
​
    return res

