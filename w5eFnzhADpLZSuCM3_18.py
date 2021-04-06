
def multiplicity(lst):
    lst1,lst2=[],[]
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    for i in lst2:
        lst1.append([i,lst.count(i)])
    return lst1

