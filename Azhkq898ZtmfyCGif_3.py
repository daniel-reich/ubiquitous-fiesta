
def numbers_to_ranges(ls):
    lst = ls + [0]
    if len(ls) == 0:
        return []
    if len(ls) == 1:
        return [str(lst[0])]
    index = 0
    l = []
    count = 0
    for i in range(len(lst)-1):
        if lst[i + 1] - lst[i] == 1:
            count += 1
        if lst[i + 1] - lst[i] != 1:
            if count == 0:
                l.append("{}".format(lst[i]))
                index = i + 1
            else:
                l.append("{}-{}".format(lst[index], lst[i]))
                index = i + 1
​
    return l

