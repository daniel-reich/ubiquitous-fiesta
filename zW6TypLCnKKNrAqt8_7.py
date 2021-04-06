
def left_side(lst):
    return list(sum(1 for x in lst[:i] if x < n) for i, n in enumerate(lst))
​
​
def right_side(lst):
    return list(sum(1 for x in lst[i:] if x < n) for i, n in enumerate(lst))

