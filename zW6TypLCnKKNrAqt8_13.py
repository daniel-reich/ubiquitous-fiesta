
def left_side(lst):
    return [len([x for x in lst[:k] if x < v]) for k,v in enumerate(lst, 1)]
​
def right_side(lst):
    return [len([x for x in lst[k:] if x < v]) for k,v in enumerate(lst)]

