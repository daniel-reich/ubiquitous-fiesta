
def advanced_sort(ls):
    nls = [[ls[0]] * ls.count(ls[0])]
    i = 1
    while i < len(ls):
        if ls[i] not in ls[:i]:
            nls.append([ls[i]] * ls.count(ls[i]))
        i+=1
    return nls

