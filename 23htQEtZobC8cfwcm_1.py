
def canConcatenate(lst, target):
    lst = sum(lst,[])
    return True if sorted(target)==sorted(lst,reverse=True) or sorted(target)==sorted(lst) else False

