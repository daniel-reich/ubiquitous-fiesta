
def median(lst):
    mid = len(lst) // 2
    return lst[mid] if len(lst) % 2 else (lst[mid - 1] + lst[mid]) / 2
​
def iqr(lst):
    lst.sort()
    q, r = divmod(len(lst), 2)
    return abs(median(lst[q + r:]) - median(lst[:q]))

