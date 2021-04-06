
def priority_sort(lst, s):
    beg = []
    for x in s:
        while x in lst:
            lst.remove(x)
            beg.append(x)
    return sorted(beg) + sorted(lst)

