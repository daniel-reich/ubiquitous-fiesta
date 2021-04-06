
def left_side(lst):
    return [sorted(lst[:n]).index(lst[n-1]) for n in range(1,len(lst)+1)]
def right_side(lst):
    return [sorted(lst[n:]).index(lst[n]) for n in range(0,len(lst))]

