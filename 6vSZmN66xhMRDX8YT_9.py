
def advanced_sort(lst):
    l = []
    l2 = []
    for i in lst:
        if i not in l:
            l.append(i)
    for i in l:
        l2.append([i]*lst.count(i))
    return l2

