
def advanced_sort(lst):
    newlst = [[lst[0]]]
    found = False
    for i in range(1, len(lst)):
        for j in range(len(newlst)):
            if lst[i] == newlst[j][0]:
                newlst[j].append(lst[i])
                found = True
        if not found:
            newlst.append([lst[i]])
        found = False
    return newlst

