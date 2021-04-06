
def clear_ordering(lst):
    min = []
    for i in lst:
        min.append(i[0])
        for a in lst:
            if i[0]==a[1]:
                min.remove(i[0])
​
    return not len(min)>1

