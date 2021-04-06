
def sum_holes(n):
    d = {8: 2, 9: 1, 6: 1, 4: 1, 0: 1, 2: 0, 3: 0, 5: 0, 7: 0, 1: 0}
    res = 0
​
    for y in str(n):
        if int(y) in d:
            res += d[int(y)]
​
    return res
​
​
def holey_sort(lst):
    return sorted(lst, key=lambda x: sum_holes(x))

