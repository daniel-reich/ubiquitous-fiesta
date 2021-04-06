
def mdn(lst):
    lst, mid_pos = sorted(lst), len(lst) // 2
    if len(lst) % 2:
        return lst[mid_pos]
    return (lst[mid_pos] + lst[mid_pos - 1]) / 2
​
​
def iqr(lst):
    lst, mid_pos = sorted(lst), len(lst) // 2
    if len(lst) % 2:
        return mdn(lst[mid_pos + 1:]) - mdn(lst[:mid_pos])
    return mdn(lst[mid_pos:]) - mdn(lst[:mid_pos])

