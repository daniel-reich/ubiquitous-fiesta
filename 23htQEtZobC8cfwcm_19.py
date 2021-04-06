
def canConcatenate(lst, target):
    a = []
    for n in range(len(lst)):
        for i in lst[n]:
            a.append(i)
    return sorted(a) == sorted(target)

