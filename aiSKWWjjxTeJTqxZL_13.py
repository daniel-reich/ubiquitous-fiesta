
def complete_square(lst):
    res = []
    if len(lst) == len(lst[0]):
        return lst
    if len(lst) > len(lst[0]):
        for x in range(0, len(lst)):
            res.extend(0 for y in range(len(lst) - len(lst[0])))
            lst[x].extend(res)
    else:
​
        for x in range(len(lst[0]) - len(lst)):
            lst.append([0 for x in range(len(lst[x]))])
    return lst

