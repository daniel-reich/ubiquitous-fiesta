
def canConcatenate(lst, target):
    return sorted([j for i in lst for j in i])==sorted(target)

