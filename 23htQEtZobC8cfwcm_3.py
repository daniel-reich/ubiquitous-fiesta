
def canConcatenate(lst, target):
    l = [i for innerlst in lst for i in innerlst]
    return sorted(l) == sorted(target)

