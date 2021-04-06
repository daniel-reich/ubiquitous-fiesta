
def min_miss_pos(lst):
    lst = sorted(set(lst))
    last = lst[0]
    for i in lst[1:]:
        if i != last+1 and last+1 >0:
            return last+1
        last = i
    return last+1

