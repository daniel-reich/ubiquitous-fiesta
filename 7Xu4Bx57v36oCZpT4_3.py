
def where_is_waldo(lst):
    for i in lst:
        for j in i:
            if i.count(j) == 1:
                col = i.index(j) + 1
                row = lst.index(i) + 1
    return [row, col]

